import database
import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

class TestScreen(GridLayout):

        def __init__(self, **kwargs):
            super(TestScreen, self).__init__(**kwargs)
            self.cols = 2
            self.row = 2
            self.size_hint = (0.6 , 0.7)
            self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
            self.add_widget(Label(
                text='User Name'
            ))
            self.username = TextInput(
                multiline=False,
                padding_y = (30, 30),
                size_hint = (1, 0.7),
                font_size = 30
            )
            
            self.add_widget(self.username)
            self.add_widget(Label(text='password'))
            self.password = TextInput(
                password=True,
                multiline=False,
                padding_y = (30, 30),
                font_size = 30,
                size_hint = (1, 0.7),
                )
            
            self.add_widget(self.password)
            self.logo = Image(source="ces.jpeg")
            self.add_widget(self.logo)
            self.hello = Button(text="Login", on_release=self.auth)
            self.add_widget(self.hello)

        def auth(self, button):
            print('button pressed:', button)

            can_log_in = False
            
            for dictionary in database.database:
                if self.username.text == dictionary["user"] and self.password.text == dictionary["password"]:
                    can_log_in = True
                    break
                    
            if can_log_in:
                SecondScreen()
            else:
                popup = Popup(title="Invalid Credentials",
                    content=Label(text="Invalid Username or Password"),
                    size=(150, 150),
                    size_hint=(0.4, 0.4),
                    auto_dismiss=True)
                popup.open()


class SecondScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2


class CesApp(App):

    def build(self):
        return TestScreen()


if __name__ == '__main__':
    CesApp().run()
  