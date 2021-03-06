from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty

from nwutils import *

import time


from kivy.config import Config
#Config.set('graphics', 'width', '800')
#Config.set('graphics', 'height', '480')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '700')
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
DHT11_SETUP_URL = "http://weavebytes.com/pitools/dht11_setup.sh"

CAMERA_SRC_URL = "http://weavebytes.com/pitools/dht11.zip"
CAMERA_SETUP_URL = "http://weavebytes.com/pitools/camera_setup.txt"

IR_SRC_URL = "http://weavebytes.com/pitools/ir_source.zip"
IR_SETUP_URL = "http://weavebytes.com/pitools/ir_setup.txt"

PPIR_SRC_URL = "http://weavebytes.com/pitools/pir_source.zip"
PIR_SETUP_URL = "http://weavebytes.com/pitools/pir_setup.txt"

LIGHT_SRC_URL = "http://weavebytes.com/pitools/light_source.zip"
LIGHT_SETUP_URL = "http://weavebytes.com/pitools/light_setup.txt"

ULTRASONIC_SRC_URL = "http://weavebytes.com/pitools/ultrasonic_source.zip"
ULTRASONIC_SETUP_URL = "http://weavebytes.com/pitools/ultrasonic_setup.txt"

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

    def get_accelerometer_sensor(self, lblStatus):
        print "setting accelerometer sensor"
    
    def get_blood_pressure_sensor(self, lblStatus):
        print "setting blood pressure sensor"
    
    def get_heart_beat_sensor(self, lblStatus):
        print "setting heart beat sensor"

    def get_ir_sensor(self, lblStatus):
        print "setting IR sensor"
        download_and_save(IR_SRC_URL, PROJECTS_DIR)
        download_and_install(IR_SETUP_URL)

    def get_light_sensor(self, lblStatus):
        print "setting light sensor"
        download_and_save(LIGHT_SRC_URL, PROJECTS_DIR)
        download_and_install(LIGHT_SETUP_URL)

    def get_pir_sensor(self, lblStatus):
        print "setting pir sensor"
        download_and_save(PIR_SRC_URL, PROJECTS_DIR)
        download_and_install(PIR_SETUP_URL)

    def get_temp_humidity_sensor(self, lblStatus):
        print "setting temp humidity sensor"
        lblStatus.text = "Setting up Temperature & Humidity sensor, please wait..." 
        download_and_save(DHT11_SRC_URL, PROJECTS_DIR)
        download_and_install(DHT11_SETUP_URL)
        lblStatus.text = "Temperature & Humidity Sensor Installed"
        print "Temperature & Humidity Sensor Installed"

    def get_ultrasonia_sensor(self, lblStatus):
        print "setting ultrasonic sensor"
        download_and_save(ULTRASONIC_SRC_URL, PROJECTS_DIR)
        download_and_install(ULTRASONIC_SETUP_URL)

    def get_idr_sensor(self, lblStatus):
        print "setting idr sensor"
        
    def get_sound_sensor(self, lblStatus):
        print "setting sound sensor"
    


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

