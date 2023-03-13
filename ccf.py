from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from os import listdir

class ImageViewerApp(App):
    def build(self):
        self.directory = "C:/Users/bing/Desktop/bing1"
        self.dropdown = DropDown()

        for directory in listdir(self.directory):
            btn = Button(text=directory, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.load_images(btn.text))
            self.dropdown.add_widget(btn)

        main_button = Button(text="Choose a directory", size_hint=(None, None))
        main_button.bind(on_release=self.dropdown.open)

        self.carousel = Carousel(direction='right')

        self.image_name = Button(text="No Image", size_hint=(None, None), disabled=True)
        self.image_name.bind(on_release=lambda x: print(self.image_name.text))

        return main_button, self.carousel, self.image_name

    def load_images(self, directory):
        self.dropdown.text = directory
        self.carousel.clear_widgets()
        for image_path in listdir(f"{self.directory}/{directory}"):
            if image_path.endswith(".jpg"):
                image = Image(source=f"{self.directory}/{directory}/{image_path}")
                self.carousel.add_widget(image)

                # Update the name of the current image
                self.image_name.text = image_path
                self.image_name.disabled = False
                self.image_name.bind(on_release=lambda x: print(self.image_name.text))

        # Close the popup after a directory is selected
        popup = self.dropdown.get_root_window().children[-1]
        popup.dismiss()

if __name__ == '__main__':
    ImageViewerApp().run()
