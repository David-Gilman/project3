#remote - - [13/Feb/1995:10:48:26 -0700] "GET index.html HTTP/1.0" 200 9902
#local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150
import urllib.request
import datetime

while True:
	try:
		fo = open("http_access_log", "r");
		break
	except IOError:
		urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")

requests = 0
unsuccess = 0
redirect = 0
log = []
files = {}
for line in fo:
	try:
		if line.split()[8][0] == "4": unsuccess+=1
		elif line.split()[8][0] == "3": redirect+=1 
		if line.split()[6] in files: files[line.split()[6]]+=1
		else: files[line.split()[6]] = 1
		requests+=1
	except:
#		print(line)
		pass
#	break
#	log.append(line[11:37],)

print(requests)
fo.close()
