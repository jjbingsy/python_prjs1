from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty

class Menu1App(MDApp):
    dropdown = ObjectProperty()
    def on_start(self):
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.dropdown = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

    def callback(self, button):
        self.dropdown.caller = button
        self.dropdown.open()

    def menu_callback(self, text):
        print (text)


# if __name__ == "__main__":
#     Menu1App().run()    

# https://www.javdatabase.com/idolimages/thumb/iroha-natsume.webp

import requests

# Make a request to the image URL
response = requests.get('https://www.javdatabase.com/idolimages/thumb/iroha-natsume.webp')

# Check the status code of the response
if response.status_code == 200:
    # Open a file and write the image content to it in binary mode
    with open('image.webp', 'wb') as f:
        f.write(response.content)
    print('Image saved successfully.')
else:
    print('Failed to download image.')
