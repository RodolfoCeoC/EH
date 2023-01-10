import urllib.request

web = open('web.html','wb')
consult = urllib.request.urlopen('https://example.com')
consult = consult.read()
web.write(consult)
web.close()