from urllib import request
from bs4 import BeautifulSoup

urls = ['http://www.demorgen.be/economie/hoe-komt-immosite-realo-aan-al-die-data-over-uw-huis-b2626812/','http://www.persgroep.be/nl/onze-media/realo','http://www.hln.be/hln/nl/942/Economie/article/detail/2892203/2016/09/30/Gentse-start-up-Realo-breidt-uit-naar-Spanje.dhtml','http://datanews.knack.be/ict/nieuws/stephane-vermeiren-leidt-realo-belgium/article-normal-642369.html','http://datanews.knack.be/ict/nieuws/open-data-immosite-realo-bereikt-miljoen-bezoekers-per-maand/article-normal-651429.html']

for url in urls:
    page = request.urlopen(url)
    soup = BeautifulSoup(page,'lxml')
    string_temp = soup.find_all('p')
    string = ""
    for element in string_temp:
        string = string + str(element)

string = string.replace('</p>','')
string = string.replace('<p>','')

from matplotlib import pyplot as pp

print (string)

string_split = string.split()

from wordcloud import WordCloud,ImageColorGenerator

stopwords = ['article','zegt','sessies','we','caption','datanews','Datanews','Realo','html','itemprop','knack','Knack','keyword','tag','span','class','laatste','het','nieuws','7sur7','ad','hln','nieuw','Privacybeleid','alle','strong','zones','persgroep','privacy','_blank','cookie','cookies','target','data','onze','cookiebeleid','gebruiksvoorwaarden','link','gtm','footer','cookie','br','dat','ze','het','een','de','hij','ik','en','is','haar','niet','te','van','in','http','www','voor','aan','wat','zo','er','zijn','op','wel','al','maar','meer','mij','om','of','hem','kan','toen','href','be','de','en','van','ik','te','dat','die','in','een','hij','het','niet','zijn','is','was','op','aan','met','als','voor','had','er','maar','om','hem','dan','zou','of','wat','mijn','men','dit','zo','door','over','ze','zich','bij','ook','tot','je','mij','uit','der','daar','haar','naar','heb','hoe','heeft','hebben','deze','u','want','nog','zal','me','zij','nu','ge','geen','omdat','iets','worden','toch','al','waren','veel','meer','doen','toen','moet','ben','zonder','kan','hun','dus','alles','onder','ja','eens','hier','wie','werd','altijd','doch','wordt','wezen','kunnen','ons','zelf','tegen','na','reeds','wil','kon','niets','uw','iemand','geweest','andere',]


#from scipy.misc import imread
#logomask = imread('C:/Users/jrombouts/Downloads/unnamed.png')

cloud = WordCloud(stopwords=stopwords,background_color='white').generate(string)


pp.imshow(cloud)
pp.axis("off")
pp.show()