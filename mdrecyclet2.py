from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window
from pathlib import Path
from kivy.properties import StringProperty
from kivymd.uix.imagelist.imagelist import MDSmartTile
from kivy.uix.recycleview.views import RecycleDataViewBehavior
Window.maximize()



Builder.load_string('''
<RV>:
    id: rvv
        
    viewclass: 'myTile'
    RecycleGridLayout:
        id: rgg
        default_size: None, dp(600)
        default_size_hint: 1, None
        cols: 3
        size_hint_y: None
        height: self.minimum_height
        orientation: 'lr-tb'

<mylabel@MDLabel>:
    halign: "center"
    bold: True
    color: 1, 1, 1, 1

<myTile>:
    radius: 24
    box_radius: [0, 0, 24, 24]
    box_color: 1, 1, 1, .2
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: None, None
    size: "320dp", "320dp"

    MDIconButton:
        id:icb1
        icon: "heart-outline"
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
        pos_hint: {"center_y": .5}
        on_release: root.on_release()

    MDLabel:
        text: root.texti
        bold: True
        color: 1, 1, 1, 1


''')

class myTile (MDSmartTile):
    texti = StringProperty('')
    def on_release(self, *args):
        self.ids.icb1.icon = "heart" if self.ids.icb1.icon == "heart-outline" else "heart-outline"
        print (self.source, str(self.parent.parent.parent  ))
        #self.parent.parent.data = [{'source': str(x), 'texti': x.stem} for x in Path ("images2").iterdir()] does not work
        
        #rv = App.get_running_app().rrv.data[1]["source"]
        
        #print (rv)
        #App.get_running_app().rrv.data = 
        #self.root.ids.rvv.data =
        print (self.parent)
        print (self.parent.parent)
        self.parent.parent.data =  [{'source': str(x), 'texti': x.stem} for x in Path ("images2").iterdir()]
        self.parent.clear_widgets()

        
        #u.data = [{'source': str(x), 'texti': x.stem} for x in Path ("images2").iterdir()]
        #u.parent.refresh_view_attrs(u, "source", u.parent.data)
        
        #self.parent.data = [{'source': 'images/TheBoys.jpg', 'texti': x.stem} for x in Path ("images2").iterdir()]
        #self.parent.clear_widgets()
        #u.layout_manager.clear_selection()
        #u.refresh_from_data()
        

        #self.source = "images/TerminalList.jpg"
        #return super().on_release(*args)



class RV(RecycleView, RecycleDataViewBehavior):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'source': str(x), 'texti': x.stem} for x in Path ("images").iterdir()]


class TestApp(MDApp):
    rrv = None
    def build(self):
        self.rrv = RV()
        return self.rrv

if __name__ == '__main__':
    TestApp().run()