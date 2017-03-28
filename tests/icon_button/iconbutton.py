from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty


class IconButton(Button):
    icon = StringProperty("pi.png")
    txt = StringProperty("ABC")

# you can alos just put this in your KV file
from kivy.lang import Builder
Builder.load_string("""
<IconButton>:
    on_press: print "hello"
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 37/255., 39/255., 30/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            size_hint: (1, .25)
            text: ""
        Image:
            source: "pi.png"
                
        Label:
            size_hint: (1, .5)
            text: "ABC"
""")


class TestApp(App):
    def build(self):
        return IconButton()


if __name__ in ("__main__", "android"):
    TestApp().run()
