import kivy
from kivymd.app import MDApp
from kivymd.uix.chip.chip import MDIcon
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivy.lang import Builder
from helper import usernameHelper


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='LightGreen'
        self.theme_cls.theme_style='Dark'
        screen = Screen()
        self.username = Builder.load_string(usernameHelper)
        showbtn = MDRectangleFlatButton(
            text='show',
            pos_hint={'center_x':0.5,'center_y':0.29},
            on_release=self.show_data
        )
        self.show_user = MDLabel(
            text='',
            pos_hint={'center_x':0.5,'center_y':0.4},
            size_hint_x=None,
            width=300,
            halign='center'
        )
        screen.add_widget(self.username)
        screen.add_widget(self.show_user)
        screen.add_widget(showbtn)
        return screen
    def show_data(self, obj):
        print(self.username.text)
        self.show_user.text = f"Hello  {self.username.text}"
        self.username.text = ''

MyApp().run()