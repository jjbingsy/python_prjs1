from kivy.lang import Builder
from kivymd.app import MDApp
import kivymd.uix.swiper.swiper
from kivymd.uix.screen import MDScreen
from pathlib import Path
from kivymd.uix.swiper import MDSwiper
import subprocess
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.metrics import dp
from bs4 import BeautifulSoup



def parseTitle (str1):
    x = 0
    preF = ""
    sufF = ""
    for c in str1:
        if x == 0:
            if c.isalpha():
                preF += c
            else:
                x = 1
        if x == 1:
            if c.isdigit():
                x = 2
        if x == 2:
            if c.isdigit():
                sufF += c
            else:
                x = 3
    return preF.upper() + "-" + sufF.upper()


def playSeries(path1):
    
    t = list()
    pathe = Path ('D:/htmlsource/' + path1 )
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
                txt = content.split()[0].upper().strip()
                if txt not in myset:
                    myset.add(txt)
                    t.append ((txt, content))
    return t







class myscreen(MDScreen):


    def on_destroy(self):
        if len (self.ids.myswipe.get_items() ) > 0:
            item = self.ids.myswipe.set_current(0)
            for i in self.ids.myswipe.get_items():
                print (i)
                self.ids.myswipe.remove_widget(i)
    def on_text(self):
        #pass
        mypath = Path('D:/trusti').glob ('adn-*.jpg')
        print (mypath)
        for e in mypath:
            print (e)
            m = MySwiper()
            m.tyt = str(e)
            m.children[0].source = str(e)
            print (m.children[0].source)
            self.ids.myswipe.add_widget(m)        
        #m = MySwiper() #source = "C:/Users/Security/Documents/Joseph Sy/DORS/archived/TEST/Moonfall.jpg")
        #print (str(m.children[1]))
        #m.source = "C:/Users/Security/Documents/Joseph Sy/DORS/archived/TEST/Moonfall.jpg"
        #self.root.ids.myswipe.add_widget(m) works
    def on_clear(self):
        t = ["C:/Users/bing/Desktop/mpv/mpv.exe", "--fs", "--fs-screen=0", "--loop-playlist" ]
        #self.root.clear_widgets()
        #du = myscreen()
        #self.root.add_widget(du)
        if len (self.ids.myswipe.get_items() ) > 0:
            item = self.ids.myswipe.get_current_item()
            #source = item[0].source
            i = item.tyt.split()[0].lower()
            #i = Path(item.tyt.lower()).stem
            files = Path("C:/Users/bing/Desktop/link").glob ( i + "*")
            for s in files:
                print(s)
                t.append(s)
            subprocess.run(t)

        #    self.root.ids.myswipe.remove_widget(self.root.ids.myswipe.get_current_item()) #works
    def on_swipe(self):
        u = str (self.ids.myswipe.get_current_item().children[0].source)
        self.ids.toolbar.title = self.ids.myswipe.get_current_item().tyt
        print (self.ids.myswipe.get_current_item().tyt)





class MyBox(BoxLayout):
    def __init__(self, **kargs):
        super().__init__(**kargs)

    def on_press (self, *args):
        pass


class MySwiper(kivymd.uix.swiper.swiper.MDSwiperItem):
    tyt = StringProperty("")

class MainApp (MDApp):
    menu = ObjectProperty()



    def menu_callback(self, text_item):
        #print (text_item)
        print (str(self.root.ids))
        print ("YYYA", text_item)
        if len (self.root.ids.myswipe.get_items() ) > 0:
            item = self.root.ids.myswipe.set_current(0)
            for i in self.root.ids.myswipe.get_items():
                self.root.ids.myswipe.remove_widget(i)
            
        for stem, content in playSeries (text_item):
            print ("TTESS", stem, content)
            fullpath = "D:/trusti/" + stem.upper() + ".jpg"
            if Path(fullpath).exists():    
                m = MySwiper()
                m.tyt = content
                m.children[0].source = fullpath
                #print (m.children[0].source)
                self.root.ids.myswipe.add_widget(m)        







    def callback(self, button):
        self.menu.caller = button
        self.menu.open()


    def on_start (self):

        paths = Path("D:/htmlsource").iterdir()
        




        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i.name,
                "height": dp(56),
                "on_release": lambda x=f"{i.name}": self.menu_callback(x),
             } for i in paths
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

    def build(self):
        #return super().build()
        return Builder.load_file ('swiper.kv')
        






if __name__ == "__main__":
    h = []
    h.extend ([5, 6, 4])
    print (h)
    MainApp().run()


