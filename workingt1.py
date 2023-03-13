from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from pathlib import Path
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.uix.imagelist.imagelist import MDSmartTile
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from bs4 import BeautifulSoup
import subprocess
import multiprocessing
import os

from tt import parseTitle

Window.maximize()

# def parseTitle (str1):
#     x = 0
#     preF = ""
#     sufF = ""
#     for c in str1:
#         if x == 0:
#             if c.isalpha():
#                 preF += c
#             else:
#                 x = 1
#         if x == 1:
#             if c.isdigit():
#                 x = 2
#         if x == 2:
#             if c.isdigit():
#                 sufF += c
#             else:
#                 x = 3
#     return preF.upper() + "-" + sufF.upper()


# def playSeries(path1):
    
#     t = list()
#     pathe = Path ('D:/htmlsource/' + path1 )
#     sources = pathe.iterdir()
#     myset = set()
#     for source in sources:
#         if source.exists():
#             #contents = ''
#             with open(source, mode="r", encoding='utf-8') as f:
#                 #soup = BeautifulSoup(f, 'lxml')  D:\htmlsource\kkaede\k1.html
#                 contents = f.read() #print (source)#, f.read_text())
#             soup = BeautifulSoup(contents, 'html.parser')
#             elements = soup.find_all(class_='text-secondary group-hover:text-primary')

#             # Loop through the elements and extract the content and href
#             for element in elements:
#                 content = element.text
#                 href = element['href']
#                 txt = content.split()[0].upper().strip()
#                 if txt not in myset:
#                     myset.add(txt)
#                     #print (txt, content)
#                     t.append (("d:/trustp/" + txt.strip() + ".jpg", content))
#     return t


class MyScreen (MDBoxLayout):
    pass


class myTile (MDSmartTile):
    texti = StringProperty('')
    def separate(self):
        t = ["C:/Users/bing/Desktop/mpv/mpv.exe", "--fs", "--fs-screen=0", "--loop-playlist" ]
        i = "C:/Users/bing/Desktop/mpv/mpv.exe --fs --fs-screen=0 --loop-playlist" 
        files = Path("C:/Users/bing/Desktop/link").glob ( self.texti.lower() + "*")
        print (self.texti)
        for s in files:
            t.append(s)
            i = i + " " + str(s)
        #os.system(i)
        subprocess.run(t)
        print (i, "oanother")

    def on_release(self, *args):
        #t = ["C:/Users/bing/Desktop/mpv/mpv.exe", "--fs", "--fs-screen=0", "--loop-playlist" ]
        #files = Path("C:/Users/bing/Desktop/link").glob ( self.texti.lower() + "*")
        #print (self.texti)
        #for s in files:
        #    t.append(s)
        # p = multiprocessing.Process(target=self.separate)
        # p.start()
        # p.join()
        self.separate()
        #subprocess.run(t)


class MyRec (RecycleView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        MDApp.get_running_app().rv = self
        #self.data = [{'source': str(x), 'texti': x.stem} for x in Path ("D:/series1/Shared-Room-With-My-Female-Boss").iterdir()]
        
    
    #def build(self):
    #   


class Wrk1App(MDApp):
    rv = ObjectProperty()
    def build(self):
        menu_items = [
        {
            "viewclass": "OneLineListItem",
            "text": i.name,
            "height": dp(56),
            "on_release": lambda x=f"{i.name}": self.menu_callback(x),
            } for i in Path("D:/series4").iterdir()
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=12,
        )

        return Builder.load_file ('EWrk1.kv')

    def callback (self, topmenu):
        self.menu.caller = topmenu
        self.menu.open()
    
    def menu_callback(self, txt):
        #U = playSeries(txt)
        #self.rv.ids.toolbar = txt
        newpath = Path("D:/series4") / txt
        self.rv.ids.rgg.clear_widgets()
        self.rv.data = [{'source': str(x), 'texti': x.stem} for x in newpath.iterdir()]
        self.root.ids.toolbar.title = txt
        
        #print(txt)

if __name__ == '__main__':
    Wrk1App().run()
