
def generateUrl(base, i,j,k):
	ret = base + str(i) + '-chapter-' + str(j) + '-'
	if k < 10:
		ret = ret + '0' 
	ret = ret + str(k) + '/'
	return ret

import urllib2
i = 1
j = 1
k = 1
hdr = {'User-Agent':'Mozilla/5.0'}
site = generateUrl('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-' , i, j, k)
#site = + str(i) + '-chapter-' + str(j) +'-'+ str(k) +'/'
req = urllib2.Request(site, headers=hdr)
print site
response = urllib2.urlopen(req)
print response.read()