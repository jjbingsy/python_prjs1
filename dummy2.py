import os
import random
from kivymd.app import MDApp
from kivymd.uix.grid import MDGridView
from kivymd.uix.screen import MDScreen
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView

class GridMDApp(MDApp):
    def build(self):
        screen = MDScreen()
        scroll = ScrollView()
        grid = MDGridView()
        grid.cols = 4
        grid.spacing = [10, 10]

        images_directory = 'images'
        image_files = os.listdir(images_directory)
        random_images = random.sample(image_files, 16)

        for image in random_images:
            grid.add_widget(AsyncImage(source=os.path.join(images_directory, image)))

        scroll.add_widget(grid)
        screen.add_widget(scroll)
        return screen

if __name__ == '__main__':
    GridMDApp().run()
