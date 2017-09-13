import re
import sys
from ebooklib import epub
import HTMLParser
import os

reload(sys)
sys.setdefaultencoding('utf8')

def createBook(id, title, language, author, chapMin, chapMax, filenameSuffixe, bookname):
    #lstFiles = []
    lstChaps = []
    #lstFiles.sort()
    book = epub.EpubBook()
    book.set_identifier(id)
    book.set_title(title)
    book.set_language(language)
    book.add_author(author)

    #book.set_cover("image.jpg", open('cover.jpg', 'rb').read())
    book.spine = ['cover']
    for i in range(chapMin, chapMax+1):
        filename = filenameSuffixe + str(i)
        print filename
        f = open('input/'+filename, 'r')
        strFile = f.read()
        f.close()
        m = re.search('<hr ?/?>(.|\n)*<hr ?/?>', strFile)
        h = HTMLParser.HTMLParser()
        strAlmostClean = h.unescape(m.group(0))
        strAlmostClean = strAlmostClean.replace('<span style="font-weight: 400;">','')
        strAlmostClean = strAlmostClean.replace('</span>','')
        strAlmostClean.decode('utf-8')
        #fout = open('output/'+filename+'.xhtml', 'w')
        #fout.write(strAlmostClean)
        #fout.close()
        c = epub.EpubHtml(title='Chapitre ' + str(i), file_name=filename + '.xhtml', lang='hr')
        #lstFiles.append(filename+'.xhtml')
        c.content=strAlmostClean
        book.add_item(c)
        lstChaps.append(c)
        #book.spine =book.spine + ['Chapitre ' + str(i-1), c]
        book.spine =book.spine + [c]
        #print book.spine
        # define CSS style
    book.toc = lstChaps
    #print book.toc
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    epub.write_epub(bookname+'.epub', book, {})
    
if __name__ == '__main__':
    createBook('ldk', 'Legend of the Dragon King', 'en', 'Wuxia World', 1, 260, 'ldk-chapter-', 'Legend of the Dragon King')

