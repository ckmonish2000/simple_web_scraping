from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<h1>sup</h1>
<div>
<p class="title" id="story"><b>The Dormouse's story</b></p>
<p>second</p>
</div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<div data-hello="hi">"hello sucker"</div>
<div id="hellooo">"hello suckerr"</div>
<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,"html.parser")

#direct

# print(soup.body)
# print(soup.head.title)

#find
el=soup.find('div')

# print(el)
# el=soup.find_all('a')
# print(el[1])


# id and classes

# el=soup.find(id='story')
# print(el)

# el=soup.find(class_='title')
# print(el)


# data attribute

# el=soup.find(attrs={"data-hello":"hi"})
# print(el)


# select

# el=soup.select('#story')
# print(el)

# el=soup.select('.story')[0]
# print(el)
  

# get text


# el=soup.find(id='hellooo').get_text()
# print(el)

# el=soup.select('.story')
# for x in el:
#     print(x.get_text())


# navigation

# el=soup.body.contents[1].find_next_sibling()


# el=soup.find(id='story').find_previous_sibling()

# el=soup.find(id='story').find_parent()

el=soup.find(id='story').find_next_sibling('p')

print(el)