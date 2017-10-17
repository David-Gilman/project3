#iremote - - [13/Feb/1995:10:48:26 -0700] "GET index.html HTTP/1.0" 200 9902
import datetime
import re
import calendar
import time

while True:
	try:
		fo = open("http_access_log", "r");
		print("Searching log...")
		break
	except IOError:
		import urllib.request
		print("Log not found")
		print("Downloading log...")
		urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")
		print("Log retrieved")

requests = 0
unsuccess = 0
redirect = 0
weeks = 0
months = 0
files = {}
weekday = {}
for i in range(0,7):
	weekday[i] = 0
conv = dict((v,k) for k,v in enumerate(calendar.month_abbr)) 
reg = re.compile('.*\[([^:]*):(.*) \-\d{3,4}\].*')

for line in fo:
#	try:
		if line.split()[8][0] == "4": unsuccess+=1
		elif line.split()[8][0] == "3": redirect+=1 
		if line.split()[6] in files: files[line.split()[6]]+=1
		else: files[line.split()[6]] = 1
		requests+=1
		#event = time.strptime(reg.match(line))
		print(re.split('[/ :]',(line.split()[3])))
		event = datetime(int((re.split('[/ :]',line.split()[3])[2])),conv[re.split('[/ :]',(line.split()[3])[1])][0],int((re.split('[/ :]',line.split()[0])[2])))
		print(event)
		weekday[event.weekday()] = weekday[event.weekday()] + 1 
	#except:
#		pass


print("Total requests: " + str(requests))
print("Unsucesful requests: " + str(round((unsuccess/requests),4)*100) + "%")
print("Redirected requests: " + str(round((redirect/requests),4)*100) + "%")
print("Most requested file: " + max(files, key=files.get))
print("Least requested file: " + min(files, key=files.get))
print(weekday)

fo.close()
