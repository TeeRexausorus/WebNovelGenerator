import re
import sys
from ebooklib import epub
import HTMLParser
import os
import os.path

reload(sys)
sys.setdefaultencoding('utf8')

def createBook(id, title, language, author, filenameSuffixe):
	#lstFiles = []
	lstChaps = []
	#lstFiles.sort()
	book = epub.EpubBook()
	book.set_identifier(id)
	book.set_title(title)
	book.set_language(language)
	book.add_author(author)
	#book.set_cover("image.jpg", open('cover.jpg', 'rb').read())
	book.spine = ['cover', 'nav']
	flag = 1
	j = 1
	k = 1
	filename = 'input/ast'+ '-chapter-' + str(j)
	#print 'for ' + filename
	while(os.path.isfile(filename)): #j
		filename = 'input/ast'+ '-chapter-' + str(j)
		if (os.path.isfile(filename)):
			print( filename)
			f = open(''+filename, 'r')
			strFile = f.read()
			#print '>' + strFile
			f.close()
			m = re.search('<hr ?\/?>((.|\n)*?)(?=<a)', strFile)
			h = HTMLParser.HTMLParser()
			strAlmostClean = h.unescape(m.group(1))
			strAlmostClean.decode('utf-8')
			if (flag==1):
				flag = 0
			c = epub.EpubHtml(title='Chapitre ' + str(j)+'-'+str(k), file_name=filename + '.xhtml', lang='hr')
			#lstFiles.append(filename+'.xhtml')
			c.content=strAlmostClean
			book.add_item(c)
			lstChaps.append(c)
			#book.spine =book.spine + ['Chapitre ' + str(i), c]
			book.spine =book.spine + [c]
			#print book.spine
			# define CSS style
			k = k + 1
			#end of if
		j = j + 1
		filename = 'input/ast-chapter-'+str(j)
			#end of while j loop
	#end of for loop
	book.toc = lstChaps
	#print book.toc

	style = 'BODY {color: white;}'
	nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

	# add CSS file
	book.add_item(nav_css)
	book.add_item(epub.EpubNcx())
	book.add_item(epub.EpubNav())
	epub.write_epub(title +'.epub', book, {})

if __name__ == '__main__':
	createBook('Ancient Strengthening Technique', 'Ancient Strengthening Technique', 'en', 'Wuxia World', 'ast-chapter-')
