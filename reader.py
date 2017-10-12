fo = open("http_access_log", "r");

requests = 0
for line in fo:
	requests+=1
	print(line)
print (requests)
fo.close()
