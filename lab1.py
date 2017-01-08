import re
import requests
homeURL = 'http://www.mosigra.ru/'
URLlist = [homeURL]
mailList = []
n = 0
def findMails(URLParameter):
	global URLlist, mailList, n
	n += 1
	r = requests.get(URLParameter)
	html = r.text
	URLlistNew = list(set(re.findall('href="(.*?)"',html)))
	mailListNew = list(set(re.findall(r'mailto:[a-zA-Z0-9-\.@_]+',html)))
	for mail in mailListNew:
		mail = mail[7:]
		mailList.append(mail)
	for URL in URLlistNew:
		if URL not in URLlist:
			URLlist.append(URL)
			if URL[:len(homeURL)] == homeURL and n < 3:
				findMails(URL)
findMails(URLlist[0])
print(set(mailList))