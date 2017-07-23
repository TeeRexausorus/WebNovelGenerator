# coding: utf8
from bs4 import BeautifulSoup
import urllib2
import re
import os.path
from ebookGen import createBook
def dl_directLink(url, chapter):
    print chapter
    print (not os.path.isfile(chapter))
    if not os.path.isfile(chapter):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        p_used = False
        for div in soup.findAll('div', attrs={'class': 'entry-content'}):
            for p in div.findAll('p'):
                p_used = True
                if p.find('a') == None:
                    p_used = False
                else:
                    url_chap = p.find('a')['href']
            if (not p_used):
                for iframe in div.findAll('iframe'):
                    print "iframe"
                    url_chap = iframe['src']
            m = re.search('https:\/\/.*', url_chap)
            print "{} - {} - {}".format(chapter, m.group(0), url_chap)
            true_url_chap = m.group(0)
            with  open(chapter, 'w') as f:
                chap = urllib2.urlopen(true_url_chap)
                for line in chap:
                    f.write(str(line))

def is_int(val):
    try:
        val = int(val)
    except ValueError:
        return False
    return True

def parse_chap_list():
    url='https://bluesilvertranslations.wordpress.com/chapter-list'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    chap_num = 0
    #print soup.find('ul')
    for li in soup.find('div', attrs={'class': 'entry-content'}).findAll('li'):
        for a in li.findAll('a'):
            href = a['href']
            print a.get_text()
            if is_int((a.get_text()).encode('utf8').strip()[:3]):
                chap_num = (a.get_text()).encode('utf8').strip()[:3]
            chapter = "input/dd-chapter-" + str(chap_num)
            print "{}***{}".format(href, chapter)
            if ('share' in href) or (os.path.isfile(chapter)):
                continue
            dl_directLink(href, chapter)
    createBook('douluoDalu', 'Douluo Dalu', 'en', 'Blue Silver Translation', 0, int(chap_num), 'dd-chapter-')

if __name__ == "__main__":
    parse_chap_list()
    
