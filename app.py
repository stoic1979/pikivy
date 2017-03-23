from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set("graphics", "show_cursor", 1)

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("main.kv")

# Declare both screens
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(DashboardScreen(name='dashboard'))
sm.add_widget(SettingsScreen(name='settings'))

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

