import requests
from bs4 import BeautifulSoup
from csv import writer

res=requests.get('https://www.webs.com/themes');
print(res)

soup=BeautifulSoup(res.text,'html.parser')

# el=soup.body.contents
el=soup.select('#webs-nav')
a=[]
for x in el:
    print(x.get_text().replace('\n',''))
    a.append(x.get_text())
    

print(a)