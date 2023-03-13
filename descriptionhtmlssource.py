from bs4 import BeautifulSoup
from pathlib import Path
import shutil


t = list()
sourcepath = Path("D:/trustp")
destpath = Path ("D:/series4")
iii = Path ('C:/Users/bing/Desktop/series').iterdir() #C:\Users\bing\Desktop\series\Fucked-In-Front-Of-My-Husband
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
                #print(txt, str(source).split('\\')[-2])
                subdir = str(source).split('\\')[-2]
                ss = sourcepath / (txt + ".jpg")
                d1 = destpath / subdir 
                d1.mkdir(parents=True, exist_ok=True)
                dd = d1 / ss.name

                if ss.exists():
                    shutil.copy (ss, dd)
                    print (dd)
                





            
