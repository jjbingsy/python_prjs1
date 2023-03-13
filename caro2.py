from kivy.lang import Builder
from kivymd.app import MDApp
import kivymd.uix.swiper.swiper
from kivymd.uix.screen import MDScreen
from pathlib import Path
from kivymd.uix.swiper import MDSwiper
import subprocess
from kivymd.uix.boxlayout import BoxLayout



class mess (MDScreen):
    pass


class MySwiper(MDSwiper):
    pass


class Item(object):
    def __init__(self, link, description, image_link):
        self.link = link
        self.description = description
        self.image_link = image_link




class MyMDApp(MDApp):
    pass

if __name__ == "__main__":
    MyMDApp().run()