from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty


from kivy.config import Config
#Config.set('graphics', 'width', '800')
#Config.set('graphics', 'height', '480')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '640')
Config.set("graphics", "show_cursor", 1)

class IconButton(Button):
    imgSource = StringProperty("images/pi.png")
    btnText = StringProperty("ABC")

# settings widgets
class CameraSettingsWidget(Widget):
    pass

class WifiSettingsWidget(Widget):
    pass

class BluetoothSettingsWidget(Widget):
    pass

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("main.kv")

# Declare both screens
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ProgramsScreen(Screen):
    pass

class SensorsScreen(Screen):
    pass

class MultimediaScreen(Screen):
    pass

class CommnProtocolScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ProgramsScreen(name='programs'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(SensorsScreen(name='sensors'))
sm.add_widget(MultimediaScreen(name='multimedia'))
sm.add_widget(CommnProtocolScreen(name='com_protocol'))
sm.add_widget(HelpScreen(name='help'))

class MainApp(App):

    txt = 'some test'

    def build(self):
        return sm

    def on_start(self, **kwargs):
        print "-- app started --"

    def change(self, *kwargs):
        print "--change--", kwargs

    def connect_wifi(self, nw, psw):
        print "--connect_wifi--", nw, psw


if __name__ == '__main__':
    MainApp().run()

