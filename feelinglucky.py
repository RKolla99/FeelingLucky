import sys
import bs4
import requests
import os
from scorePara import score

if os.path.exists("paras.txt"):
    # print("removing previous txt file")
    os.remove("paras.txt")
# else:
    # print("The file does not exist") 

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) #taking argument in the terminal 
res.raise_for_status() 

soup = bs4.BeautifulSoup(res.text,'html.parser') # Retrieve top search result links.

linkElems = soup.select('.r a') # to store your addresses including the a tag
num = 4 #no of webpages to extract from
# print(type(linkElems[0]))
url = ""
f=open("paras.txt", "a+")

for i in range(1,(num+1)): 
    if (linkElems[i].get('href').find('youtube') == -1): #to remove youtube webpages as no content present in html file
        url = ('http://google.com' + linkElems[i].get('href')) #to get the address from the href tag
    print(url)
    #while not url.endswith('#'):
    # Download the page.
    res2 = requests.get(url) #the address to get the content from
    #res2.raise_for_status())
    soup2 = bs4.BeautifulSoup(res2.text,'html.parser') #stored the content in res2
    for script in soup2(["script", "style"]):
        script.extract()    # rip it out        #removing script and style contents and tags inside the body of the document
    paraElem = soup2.find('body').getText()     #taking the text from mostly the <p>  tags
    f.write(str(paraElem.encode("utf8")))    
f.close()
print("\n")

searchPhraseWord1 = sys.argv[1]
searchPhraseWord2 = sys.argv[2]
searchPhraseWord3 = sys.argv[3]

searchPhrase = searchPhraseWord1 + " " + searchPhraseWord2 + " " + searchPhraseWord3
 
searchFile = open("paras.txt", "rb")
data = searchFile.read().decode("cp1252")

paragraphs = data.split("\\n")

paragraphs = [x for x in paragraphs if x != ""]

scoreList = []
for paragraph in paragraphs:
    scoreList.append(score(paragraph, searchPhrase))

scoresWithParas = zip(paragraphs, scoreList)

scoresWithParas = [x for x in scoresWithParas if x[1] != (0, 0, 0)]

map(list, zip(*scoresWithParas))
l = [list(t) for t in zip(*scoresWithParas)]

paras1 = l[0]
scores = l[1]
index = 0

for j in range(3):
    max3 = scores[0][j]
    for i in range(1, len(scores)):
        if(scores[i][j] > max3 and scores[i][j] != 0):
            max3 = scores[i][j]
            index = i
    if(max3):
        print(paras1[index]+"\n\n\n")
