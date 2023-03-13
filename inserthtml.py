from bs4 import BeautifulSoup
from pathlib import Path
import sqlite3

t = list()
cnn = sqlite3.connect("Series230209.db")
cr = cnn.cursor()


iii = Path ('C:/Users/bing/Desktop/series').iterdir()
for pathe in iii:
    print (pathe.stem)
    sources = pathe.iterdir()
    myset = set()
    for source in sources:
        if source.exists():
            #contents = ''
            with open(source, mode="r", encoding='utf-8') as f:
                #soup = BeautifulSoup(f, 'lxml')  D:\htmlsource\kkaede\k1.html
                contents = f.read() #print (source)#, f.read_text())
            soup = BeautifulSoup(contents, 'html.parser')
            elements = soup.find_all(class_='text-secondary group-hover:text-primary')

            # Loop through the elements and extract the content and href
            for element in elements:
                content = element.text
                href = element['href']
                txt = content.split()[0].upper()
                cn = content.replace(txt + " ", '')
                #print(txt, cn)
                tupp = txt, cn, pathe.stem
                print (tupp)
                t.append (tupp)

cr.executemany ("INSERT OR IGNORE INTO FILMS(film_name, film_description, series_id) Values (?,?,?)", t)
cnn.commit()
cnn.close()