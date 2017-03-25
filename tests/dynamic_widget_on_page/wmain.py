from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.uix.widget import Widget

class MyMainWidget(Widget):
    pass

#Factory.register('MyMainWidget', MyMainWidget)

Builder.load_file("wmain.kv")

class HomeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))



class AddWidgetApp(App):

    def build(self):
        #You need to actually DO something in `build` for your app to work.
        #app = MyMainWidget()
        #return app

        return sm

if __name__ == '__main__':
    AddWidgetApp().run()
