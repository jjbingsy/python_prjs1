
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from pathlib import Path
import os
import pyperclip
import webbrowser
from kivy.core.window import Window


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


from tt import resetLink
from tt import parseTitle
resetLink()


soft_links_dir = Path("F:/data/link.windows")
jpg_files_dir = Path("F:/data/trusti")



for soft_link in soft_links_dir.iterdir():

    if soft_link.is_symlink():
        film = parseTitle(soft_link.stem.upper())
        image = film + ".jpg"
        i = jpg_files_dir / image


        if not i.exists():
            print (i, "image doesnot exist!")
def getNoVidList():
    iii = list()
    for img in jpg_files_dir.iterdir():
        s = soft_links_dir.glob(img.stem + '*')
        i = 0
        for cnt in s:
            i += 1
        if i < 1:
            if "preffd" not in img.stem.lower():
                iii.append (img.stem.lower())
    return iii

# function to get list of button names
    return ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5"]

class ButtonApp(MDApp):

    # function to print text of button when pressed
    def button_callback(self, instance):
        film = instance.text
        pyperclip.copy(film.upper())
        webbrowser.open ("https://jav.guru/?s=" + film)
        webbrowser.open ("https://missav.com/en/search/" + film)


    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.theme_style = "Dark"
        
        # set the background color of the window to match the theme
        Window.clearcolor = self.theme_cls.bg_dark

        # create a grid layout to hold the buttons
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)

        # set the height of the grid layout to accommodate all buttons
        grid.bind(minimum_height=grid.setter('height'))

        # get the list of button names
        button_names = getNoVidList()

        # create a button for each name in the list
        for name in button_names:
            button = MDRectangleFlatButton(text=name)
            button.bind(on_press=self.button_callback)
            grid.add_widget(button)

        # create a scroll view to hold the grid layout
        scroll_view = ScrollView()
        scroll_view.add_widget(grid)

        return scroll_view

ButtonApp().run()

    








    
    #     target_path = soft_link.resolve()
    #     target_file, target_ext = target_path.with_suffix("").name, target_path.suffix
    #     jpg_path = jpg_files_dir / (target_file + ".jpg")
    #     if jpg_path.exists():
    #         print(f"Found corresponding .jpg file for {soft_link.name}: {jpg_path.name}")
    #     else:
    #         print(f"No corresponding .jpg file found for {soft_link.name}")
