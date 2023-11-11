from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
import numpy as np
import sympy as sp


class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name='Calculator_App'))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string('''
ScreenManager:
    Main:
<Main>:
    name : 'SuperCalc'

    BoxLayout:
        orientation: "vertical"

        TabbedPanel:
            do_default_tab: False
            background_color: 255, 255, 255, 1
            tab_width: 200
            
            TabbedPanelItem:
                text: 'Calculadora aritmética'
                background_color: .72, 2.23, 1.46, 1
                
                BoxLayout:
                    orientation: "vertical"

                    MDTextField:
                        id: val1
                        input_filter: 'float'
                        hint_text: "Insira o primeiro valor"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"

                    MDTextField:
                        id: val2
                        input_filter: 'float'
                        hint_text: "Insira o segundo valor"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"

                    MDTextField:
                        id: val3
                        hint_text: "Resultado"
                        readonly : "True"
                        color_mode: 'custom'
                        icon_right_color: app.theme_cls.primary_color
                        icon_right: 'equal-box'

                    MDRoundFlatIconButton:
                        id:add
                        text: "Adição"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.addition()
                    
                    MDRoundFlatIconButton:
                        id:sub
                        text: "Subtração"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.sub()

                    MDRoundFlatIconButton:
                        id:add
                        text: "Multiplicação"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.multi()

                    MDRoundFlatIconButton:
                        id:div
                        text: "Divisão"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.div()
                        
                    MDSpinner:
                        id: rc_spin2
                        size_hint: None, None
                        size: dp(46), dp(46)
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        active: False

                    MDLabel:
                        id: result2
                        
            TabbedPanelItem:
                text: 'Cálculo Diferencial e Integral'
                background_color: .72, 2.23, 1.46, 1
                
                BoxLayout:
                    orientation: "vertical"
                    
                    MDTextField:
                        id: val4
                        hint_text: "Escreva a equação"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"
                        
                    MDTextField:
                        id: val5
                        hint_text: "Resultado"
                        readonly : "True"
                        color_mode: 'custom'
                        icon_right_color: app.theme_cls.primary_color
                        icon_right: 'equal-box'
                        
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
                        
            TabbedPanelItem:
                text: 'Calculadora de programador'
                background_color: .72, 2.23, 1.46, 1
                
                BoxLayout:
                    orientation: "vertical"
                    
                    MDTextField:
                        id: val6
                        input_filter: 'int'
                        hint_text: "Insira o primeiro valor"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"
                        on_text: app.autofill()

                    MDTextField:
                        id: val7
                        input_filter: 'int'
                        hint_text: "Insira o segundo valor"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"

                    MDTextField:
                        id: val8
                        multiline: "True"
                        hint_text: "Resultado:"
                        readonly : "True"
                        color_mode: 'custom'
                        icon_right_color: app.theme_cls.primary_color
                        icon_right: 'equal-box'

                    MDRoundFlatIconButton:
                        id:add
                        text: "Adição"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.addition()
                    
                    MDRoundFlatIconButton:
                        id:sub
                        text: "Subtração"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.sub()

                    MDRoundFlatIconButton:
                        id:add
                        text: "Multiplicação"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.multi()

                    MDRoundFlatIconButton:
                        id:div
                        text: "Divisão"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.div()
                    
                    MDSpinner:
                        id: rc_spin3
                        size_hint: None, None
                        size: dp(46), dp(46)
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        active: False

                    MDLabel:
                        id: result3
    ''')
        self.title = 'SuperCalc'
        return self.help_string

    def tratamentoDeTextoVazio(t,text):
        if not text:
            return 0

    def addition(self):
        val1 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text)
        val2 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text)
        res = val1 + val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def sub(self):
        val1 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text)
        val2 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text)
        res = val1 - val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def multi(self):
        val1 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text)
        val2 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text)
        res = val1 * val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def div(self):
        val1 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text)
        val2 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text)
        if val2:
            res = val1 / val2
            self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))
        else:
            self.help_string.get_screen('SuperCalc').ids.val3.text = "Por favor, insira um valor diferente de zero no segundo valor"

    def integration(self):
        x = sp.symbols('x')
        val4 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.integrate(val4, x)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "A integração resulta em " +str(res)
        
    def derivation(self):
        x = sp.symbols('x')
        val4 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.diff(val4, x)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "A derivação resulta em " +str(res)
        
    def Laplace(self):
        t, s = sp.symbols('t s')
        val4 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.laplace_transform(val4, t, s)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "A transformada é " +str(res)
        
    def autofill(self):
        val8 = "Binario: 1001\nDecimal: 9\nHexadecimal: 9\nOctal: 11"
        self.help_string.get_screen('SuperCalc').ids.val8.text = val8

if __name__ == '__main__':
    MainApp().run()