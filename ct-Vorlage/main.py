import ConfigParser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty

from kivy.logger import Logger

class WLAN(BoxLayout):
    wlanssid = StringProperty(None)
    wlanpsk = StringProperty(None)
    android_qrcode = ObjectProperty(None)
    ios_qrcode = ObjectProperty(None)
    windows_qrcode = ObjectProperty(None)

    def updatesettings(self):
        wlancfg = ConfigParser.RawConfigParser()
        wlancfg.read('/var/guestwlan/wlan.cfg')
        self.wlanssid = wlancfg.get('WLAN', 'wlanssid')
        self.wlanpsk = wlancfg.get('WLAN', 'wlanpsk')
        self.android_qrcode.reload()
        self.ios_qrcode.reload()
        self.windows_qrcode.reload()

class GuestWLANApp(App):
    def build(self):
        w = self.root
        w.updatesettings()

if __name__ == "__main__":
    GuestWLANApp().run()
