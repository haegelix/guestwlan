from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class WLAN(BoxLayout):
    wlanssid = StringProperty(None)
    wlanpsk = StringProperty(None)

class GuestWLANApp(App):
    def build(self):
        w = self.root
        w.wlanssid = 'heise-gaeste'
        w.wlanpsk = 'kamvetkeub'

if __name__ == "__main__":
    GuestWLANApp().run()
