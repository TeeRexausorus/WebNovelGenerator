import urllib2
import httplib
def generateUrl(base, i,j,k):
	ret = base + str(i) + '-chapter-' + str(j) + '-'
	if k < 10:
		ret = ret + '0'
	ret = ret + str(k)
	return ret

def getPage(base, i, j, k, pageName):
	hdr = {'User-Agent':'Mozilla/5.0'}
	site = generateUrl(base , i, j, k)
	req = urllib2.Request(site, headers=hdr)
	returnCode = 400
	try:
		response = urllib2.urlopen(req)
		print str(i) + " " + str(j) + " " + str(k)
		with open('input/' + generateUrl(pageName, i, j, k), 'w') as f:
			f.write(response.read())
		returnCode = response.getcode()
	except urllib2.HTTPError, e:
		print ('HTTPError = ' + str(e.code))
	except urllib2.URLError, e:
		print ('URLError = ' + str(e.reason))
	except httplib.HTTPException, e:
		print ('HTTPException')
	except Exception:
		import traceback
		print ('generic exception: ' + traceback.format_exc())
	print returnCode
	return returnCode

base = 'https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-'
pageBaseName = 'hjc-book-'
book = 1
chapter = 1
part = 5
responseCode = 200
response = getPage(base, book, chapter, part, pageBaseName)
part = part + 1

while responseCode == 200: #i
	while responseCode == 200: #j
		while responseCode == 200: #k
			responseCode = getPage(base, book, chapter, part, pageBaseName)
			part = part + 1
		chapter = chapter + 1
		part = 1
		responseCode = getPage(base, book, chapter, part, pageBaseName)
	book = book + 1
	part = 1
	responseCode = getPage(base, book, chapter, part, 'hjc-book-')
