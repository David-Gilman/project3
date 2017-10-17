# iremote - - [13/Feb/1995:10:48:26 -0700] "GET index.html HTTP/1.0" 200 9902
import calendar
import re
from datetime import datetime
from timeit import default_timer as timer

def main():
    while True:
        try:
            fo = open("http_access_log", "r")
            print("Searching log...")
            break
        except IOError:
            import urllib.request
            print("Log not found")
            print("Downloading log...")
            urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")
            print("Log retrieved")

    start = timer()
    requests, fail, redirect, bad = 0, 0, 0, 0
    files, weekday, week, month = {}, {}, {}, {}
    for i in range(0, 7): weekday[i] = 0
    for i in range(0, 52): month[i] = 0
    for i in range(0, 12): month[i] = 0
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    conv = dict((v, k) for k, v in enumerate(calendar.month_abbr))
    reg = re.compile('.*\[([^:]*):(.*) -\d{3,4}\].*')

    for line in fo:
        try:
            if line.split()[8][0] == "4":
                fail += 1
            elif line.split()[8][0] == "3":
                redirect += 1
            if line.split()[6] in files:
                files[line.split()[6]] += 1
            else:
                files[line.split()[6]] = 1
            requests += 1
            event = datetime.strptime(reg.match(line).groups()[0], '%d/%b/%Y')
            weekday[event.weekday()] = weekday[event.weekday()] + 1
        except IndexError:
            bad += 1
            pass

    end = timer()
    print(str(round(end - start)) + " Seconds for processing")
    print("")
    print("1. Total requests: " + str(requests))
    print("2. Requests per day: ", )
    for i in range(7):
        print('\t' + str(days[i]) + ': ' + str(weekday[i]))
    print("Unsuccessful requests: " + str(round((fail / requests), 4) * 100) + "%")
    print("Redirected requests: " + str(round((redirect / requests), 4) * 100) + "%")
    print("Most requested file: " + max(files, key=files.get))
    # print("Least requested file: " + min(files, key=files.get))
    print("Invalid log entries: " + str(bad) + " representing " + str(round((bad / (bad + requests)), 4) * 100) + "%")

    fo.close()


if __name__ == '__main__':
    main()
