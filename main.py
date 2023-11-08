from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import numpy as np
import sympy as sp
Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'Calculator App'

    BoxLayout:
        orientation: "vertical"


        MDTextField:
            id: val1
            input_filter: 'float'
            hint_text: "Enter the first value"
            color_mode: 'custom'
            helper_text_mode: "on_focus"

        MDTextField:
            id: val2
            input_filter: 'float'
            hint_text: "Enter the second value"
            color_mode: 'custom'
            helper_text_mode: "on_focus"
            
        MDTextField:
            id: val4
            hint_text: "Escreva a equação"
            color_mode: 'custom'
            helper_text_mode: "on_focus"
            
        MDTextField:
            id: val3
            hint_text: "Result"
            readonly : "True"
            color_mode: 'custom'
            icon_right_color: app.theme_cls.primary_color
            icon_right: 'equal-box'
        
        MDRoundFlatIconButton:
            id:add
            text: "Addition"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.addition()

        MDRoundFlatIconButton:
            id:sub
            text: "Substraction"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.sub()

        MDRoundFlatIconButton:
            id:add
            text: "Multification"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.multi()

        MDRoundFlatIconButton:
            id:div
            text: "Division"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.div()
            
        MDRoundFlatIconButton:
            id:int
            text: "Integração"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.integration()
            
        MDRoundFlatIconButton:
            id:der
            text: "Derivar"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.derivation()
        MDRoundFlatIconButton:
            id:laplace
            text: "Laplace"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.Laplace()
        MDSpinner:
            id: rc_spin
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .5}
            active: False

        MDLabel:
            id: result
    '''


class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name='Calculator_App'))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        self.title = 'Calculator App'
        return self.help_string

    def addition(self):
        val1 = float(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = float(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 + val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Addition is: " +str("{:.5f}".format(res))

    def sub(self):
        val1 = float(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = float(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 - val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Subtraction is: " +str("{:.5f}".format(res))

    def multi(self):
        val1 = float(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = float(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 * val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Multification is: " +str("{:.5f}".format(res))

    def div(self):
        val1 = float(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = float(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 / val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Division is: " +str("{:.5f}".format(res))
    def integration(self):
        x = sp.symbols('x')
        val4 = self.help_string.get_screen('Calculator App').ids.val4.text
        res = sp.integrate(val4, x)
        self.help_string.get_screen('Calculator App').ids.val3.text = "A integração resulta em " +str(res)
    def derivation(self):
        x = sp.symbols('x')
        val4 = self.help_string.get_screen('Calculator App').ids.val4.text
        res = sp.diff(val4, x)
        self.help_string.get_screen('Calculator App').ids.val3.text = "A derivação resulta em " +str(res)  
    def Laplace(self):
        t, s = sp.symbols('t s')
        val4 = self.help_string.get_screen('Calculator App').ids.val4.text
        res = sp.laplace_transform(val4, t, s)
        self.help_string.get_screen('Calculator App').ids.val3.text = "A derivação resulta em " +str(res)       
MainApp().run()