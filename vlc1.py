#D:/newtrust/ADN-096.mp4

#self.player.set_media(vlc.Media("D:/newtrust/ADN-096.mp4"))

import kivy
import vlc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.lang import Builder

class VideoPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super(VideoPlayer, self).__init__(**kwargs)

        # create the player instance
        self.player = vlc.MediaPlayer()
        self.player.set_media(vlc.Media("D:/newtrust/ADN-096.mp4"))

        # create the Play button
        self.play_button = Button(text="Play")
        self.play_button.bind(on_press=self.play)
        
        # create the time label
        self.time_label = Label(text="0:00")
        
        # add the Play button and time label to the layout
        self.add_widget(self.play_button)
        self.add_widget(self.time_label)

    def play(self, instance):
        # start playing the video
        self.player.play()
        
        # start the clock to update the time label
        Clock.schedule_interval(self.update_time_label, 1/30.)

    def update_time_label(self, dt):
        # update the time label with the current position of the video
        time = self.player.get_time() / 1000.
        minutes = int(time // 60)
        seconds = int(time % 60)
        self.time_label.text = f"{minutes}:{seconds:02d}"

class VideoPlayerApp(App):
    def build(self):
        Builder.load_file('VideoPlayer.kv')
        return VideoPlayer()

if __name__ == "__main__":
    VideoPlayerApp().run()
