import sys
import bs4
import requests

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
    res2.raise_for_status()
    soup2 = bs4.BeautifulSoup(res2.text,'html.parser') #stored the content in res2
    for script in soup(["script", "style"]):
        script.extract()    # rip it out        #removing script and style contents and tags inside the body of the document
    paraElem = soup2.find('body').getText()     #taking the text from mostly the <p>  tags
    f.write(paraElem)
    
f.close()
    
    #print(paraElem) 
    #print(" \n \n  end of  page ",(i)," \n \n")

