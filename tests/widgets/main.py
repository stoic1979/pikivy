
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory


class SomeWidget(Widget):
    pass

Factory.register('SomeWidget', SomeWidget)

class Main(App):
    pass

Main().run()
