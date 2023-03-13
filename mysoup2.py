from bs4 import BeautifulSoup

htmlsource = "seriesfrrommiss.html"

with open(htmlsource, mode="r", encoding="utf-8") as src:
    soup = BeautifulSoup (src, 'lxml',  multi_valued_attributes=None)


for i in soup.find_all(class_='text-secondary group-hover:text-primary'):
    content = i.string.strip()
    link = i['href']
    print (i.get("class"))
    print (i.attrs)
    print (i.parent.name)
    print (i.parent.string)
    print (i.parent.attrs)


for j in soup.find_all(class_='my-2 text-sm text-nord4 truncate'):
    print (j.name)
    target = j.contents[1]
    print (target['class'], target['href'], str(target.string).strip() )

    print (len(j.contents[0].string), len(j.contents[1].string))

    print (type(target['class']), type(target.string), target.get('hrg') is None )

    for ii in j.descendants:
        print (ii)

    #for k in j.children:
    #print ("child:", k)

    print ("*****************")