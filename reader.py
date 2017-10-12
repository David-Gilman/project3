import urllib.request
import datetime

while True:
	try:
		fo = open("http_access_log", "r");
		break
	except IOError:
		urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")

requests = 0
log = []
files = {}
for line in fo:
	log.append(line[11:37],)
	

print(log[0])
fo.close()
