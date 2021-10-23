from kivy.app import App
from kivy.uix.label import Label


class VillainFoxApp(App):
    def build(self):
        return Label(text="Hello, Villain Fox", halign="center")


VillainFoxApp().run()
