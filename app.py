from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty

from nwutils import *


from kivy.config import Config
#Config.set('graphics', 'width', '800')
#Config.set('graphics', 'height', '480')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '640')
Config.set("graphics", "show_cursor", 1)

#------------------------------------------------------------------------------------------------#
#                  CONFIGURATION SETTINGS    
#------------------------------------------------------------------------------------------------#

# workshop directory to keep all projects etc.
# PROJECTS_DIR = "/home/pi/projects/"
#PROJECTS_DIR = "/home/pi/workshop/"

# uncomment this for desktop testing
PROJECTS_DIR = "/home/ndev/Desktop/pi_components"


# dht11 project with dependencies like adafruit package and test project
DHT11_SRC_URL = "http://weavebytes.com/pitools/dht11.zip"
DHT11_SETUP_URL = "http://weavebytes.com/pitools/dht11_setup.txt"

CAMERA_SRC_URL = "http://weavebytes.com/pitools/dht11.zip"
CAMERA_SETUP_URL = "http://weavebytes.com/pitools/camera_setup.txt"

#------------------------------------------------------------------------------------------------#

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


    #----------------------- SENSOR COMPONENTS -----------------------------------------#

    def get_dht11_sensor(self):
        download_and_save(DHT11_SRC_URL, PROJECTS_DIR)
        download_and_install(DHT11_SETUP_URL)

    def get_accelerometer_sensor(self):
        print "setting accelerometer sensor"
    
    def get_blood_pressure_sensor(self):
        print "setting blood pressure sensor"
    
    def get_heart_beat_sensor(self):
        print "setting heart beat sensor"

    def get_ir_sensor(self):
        print "setting IR sensor"

    def get_light_sensor(self):
        print "setting light sensor"

    def get_pir_sensor(self):
        print "setting pir sensor"

    def get_temp_humidity_sensor(self):
        print "setting temp humidity sensor"

    def get_ultrasonia_sensor(self):
        print "setting ultrasonic sensor"
    


    #----------------------- MULTIMEDIA COMPONENTS -------------------------------------#

    def get_audio(self):
        print "setting up audio component"

    def get_audio1(self):
        print "setting up audio1 component"
    
    def get_camera(self):
        download_and_save(CAMERA_SRC_URL, PROJECTS_DIR)
        download_and_install(CAMERA_SETUP_URL)

    def get_rpi_camera(self):
        print "setting up rpi_camera component"

    #----------------------- COMMN. PROTOCOL COMPONENTS --------------------------------#

    def get_bluetooth(self):
        print "setting up bluetooth component"

    def get_gps(self):
        print "setting up GPS component"

    def get_gsm(self):
        print "setting up GSM component"

    def get_wifi(self):
        print "setting up WiFi component"

    def get_zigbee(self):
        print "setting up ZigBee component"
    


if __name__ == '__main__':
    MainApp().run()

