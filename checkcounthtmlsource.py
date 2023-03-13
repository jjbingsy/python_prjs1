from bs4 import BeautifulSoup
from pathlib import Path

#file_path = "d:/htmlsource/A.Kaede-Karen/k5.html"
rmain = Path("C:/Users/bing/Desktop/series").iterdir()

def int_to_string(n):
    return '{:05d}'.format(n)

listing = []
for mainpaths in rmain:

    paths = Path(mainpaths).iterdir()

    for source in paths:
        with open(source, "r", encoding='utf-8') as file:
            html_content = file.read()    
            soup = BeautifulSoup(html_content, "lxml")
            spans = soup.find('span', attrs={'aria-current':'page'})
            i = 1
            try:
                i = int(spans.get_text())
            except:
                pass

            mains =   str(source.parent) + "   " + int_to_string(i)
            listing.append(mains)

listing.sort()
for e in listing:
    print (e)



