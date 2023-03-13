from kivy.lang import Builder
from kivymd.app import MDApp
import kivymd.uix.swiper.swiper
from kivymd.uix.screen import MDScreen
from pathlib import Path




class myscreen(MDScreen):
    pass

class MySwiper(kivymd.uix.swiper.swiper.MDSwiperItem):
    tyt = "L"

class MainApp (MDApp):
    def build (self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file ('swiper.kv')
    def on_swipe(self):
        u = str (self.root.ids.myswipe.get_current_item().children[0].source)
        print (u, self.root.ids.myswipe.get_current_item().tyt)
    def on_clear(self):
        #self.root.clear_widgets()
        #du = myscreen()
        #self.root.add_widget(du)
        if len (self.root.ids.myswipe.get_items() ) > 0:
            self.root.ids.myswipe.set_current(0)

        #    self.root.ids.myswipe.remove_widget(self.root.ids.myswipe.get_current_item()) #works
    def on_text(self):
        #pass
        mypath = Path('images').glob ('*.jpg')
        print (mypath)
        for e in mypath:
            print (e)
            m = MySwiper()
            m.tyt = "dummy"
            m.children[0].source = str(e)
            print (m.children[0].source)
            self.root.ids.myswipe.add_widget(m)        
        #m = MySwiper() #source = "C:/Users/Security/Documents/Joseph Sy/DORS/archived/TEST/Moonfall.jpg")
        #print (str(m.children[1]))
        #m.source = "C:/Users/Security/Documents/Joseph Sy/DORS/archived/TEST/Moonfall.jpg"
        #self.root.ids.myswipe.add_widget(m) works



MainApp().run()