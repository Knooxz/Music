from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader

class MusicPlayer(App):
    def build(self):
        self.file_chooser = FileChooserListView(filters=["*.mp3"], path="/")
        self.music_list = []
        self.box_layout = BoxLayout(orientation='vertical')
        self.box_layout.add_widget(self.file_chooser)

        self.music_label = Label()
        self.box_layout.add_widget(self.music_label)

        self.play_button = Button(text='Play')
        self.play_button.bind(on_press=self.play_music)
        self.box_layout.add_widget(self.play_button)

        self.slider = Slider(min=0, max=1, value=0)
        self.slider.bind(value=self.set_volume)
        self.box_layout.add_widget(self.slider)

        return self.box_layout

    def play_music(self, instance):
        self.file_path = self.file_chooser.selection[0]

        if self.file_path not in self.music_list:
            self.music_list.append(self.file_path.split('/')[-1])
        
        self.music_label.text = self.file_path.split('/')[-1]

        if hasattr(self, 'sound'):
            self.sound.stop()

        self.sound = SoundLoader.load(self.file_path)
        if self.sound:
            self.sound.play()

    def set_volume(self, instance, value):
        if hasattr(self, 'sound'):
            self.sound.volume = value

if __name__ == "__main__":
    MusicPlayer().run()
