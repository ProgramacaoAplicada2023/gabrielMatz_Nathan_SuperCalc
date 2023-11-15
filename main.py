from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
import numpy as np
import sympy as sp
import math as mt

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
                    MDRoundFlatIconButton:
                        id:div
                        text: "Exponencial"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.exp()
                    MDRoundFlatIconButton:
                        id:div
                        text: "Logaritmo"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.log()                  
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
                        text: "Integração em x"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.integration()
                        
                    MDRoundFlatIconButton:
                        id:der
                        text: "Derivação em x"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.derivation()
                        
                    MDRoundFlatIconButton:
                        id:laplace
                        text: "Transformada de Laplace em t"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.Laplace()
                    MDRoundFlatIconButton:
                        id:Fourier
                        text: "Série de Fourier em t"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.Fourier()
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
                        hint_text: "Conversão:"
                        readonly : "True"
                        color_mode: 'custom'
                        icon_right_color: app.theme_cls.primary_color
                        icon_right: 'equal-box'
                    MDTextField:
                        id: val9
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
                        on_press: app.addition2()
                    
                    MDRoundFlatIconButton:
                        id:sub
                        text: "Subtração"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.sub2()

                    MDRoundFlatIconButton:
                        id:add
                        text: "Multiplicação"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.multi2()

                    MDRoundFlatIconButton:
                        id:div
                        text: "Divisão"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.div2()
                    MDRoundFlatIconButton:
                        id:bit1
                        text: "Operação binária 1 valor"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.bit1()
                    MDRoundFlatIconButton:
                        id:bit2
                        text: "Operação binária 2 valores"
                        icon:"calculator"
                        pos_hint: {"center_x": .5, "center_y": .6}
                        on_press: app.bit2()
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
            return 0.0
        return text

    def addition(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text))
        res = val1 + val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def sub(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text))
        res = val1 - val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def multi(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text))
        res = val1 * val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))

    def div(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text))
        if val2:
            res = val1 / val2
            self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))
        else:
            self.help_string.get_screen('SuperCalc').ids.val3.text = "Por favor, insira um valor diferente de zero no segundo valor"

    def exp(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val2.text))
        res = val1**val2
        self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))
    def log(self):
        val1 = float(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val1.text))
        val2 = self.help_string.get_screen('SuperCalc').ids.val2.text
        if not val2:
            val2 = 10
        else:
            val2 = float(val2)
        if val2 > 0 and val2 != 1:
            if val1 > 0:
                res = mt.log(val1, val2)
                self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))
            else:
                self.help_string.get_screen('SuperCalc').ids.val3.text = "Por favor, insira um valor positivo no primeiro valor"
        else:
            self.help_string.get_screen('SuperCalc').ids.val3.text = "Por favor, insira um valor válido para a base (positivo e diferente de 1)"
    def integration(self):
        x = sp.symbols('x')
        val4 = (self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.integrate(val4, x)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "" +str(res)
        
    def derivation(self):
        x = sp.symbols('x')
        val4 = (self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.diff(val4, x)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "" +str(res)
        
    def Laplace(self):
        t, s = sp.symbols('t s')
        val4 = self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.laplace_transform(val4, t, s, noconds=True)
        self.help_string.get_screen('SuperCalc').ids.val5.text = "A transformada é " +str(res)
        
    def Fourier(self):
        t, s = sp.symbols('t s')
        val4 = (self.help_string.get_screen('SuperCalc').ids.val4.text)
        res = sp.fourier_series(val4, (t, -np.pi, np.pi))
        res=res.truncate()
        self.help_string.get_screen('SuperCalc').ids.val5.text = "" +str(res)
        
    def autofill(self):
        val6 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text))
        binary_val = bin(val6)
        decimal_val = str(val6)
        hex_val = hex(val6)
        octal_val = oct(val6)
        val8 = (f"Binario: {binary_val}\nDecimal: {decimal_val}\nHexadecimal: {hex_val}\nOctal: {octal_val}")
        self.help_string.get_screen('SuperCalc').ids.val8.text = val8
    def addition2(self):
        val1 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text))
        val2 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val7.text))
        res = int(val1 + val2)
        binary_val = bin(res)
        decimal_val = str(res)
        hex_val = hex(res)
        octal_val = oct(res)
        val9 = (f"Binario: {binary_val}\nDecimal: {decimal_val}\nHexadecimal: {hex_val}\nOctal: {octal_val}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)

    def sub2(self):
        val1 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text))
        val2 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val7.text))
        res = int(val1 - val2)
        binary_val = bin(res)
        decimal_val = str(res)
        hex_val = hex(res)
        octal_val = oct(res)
        val9 = (f"Binario: {binary_val}\nDecimal: {decimal_val}\nHexadecimal: {hex_val}\nOctal: {octal_val}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)


    def multi2(self):
        val1 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text))
        val2 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val7.text))
        res = int(val1 * val2)
        binary_val = bin(res)
        decimal_val = str(res)
        hex_val = hex(res)
        octal_val = oct(res)
        val9 = (f"Binario: {binary_val}\nDecimal: {decimal_val}\nHexadecimal: {hex_val}\nOctal: {octal_val}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)


    def div2(self):
        val1 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text))
        val2 = int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val7.text))
        if val2:
            res = int(val1 / val2)
            self.help_string.get_screen('SuperCalc').ids.val3.text = str("{:.5f}".format(res))
        else:
            self.help_string.get_screen('SuperCalc').ids.val3.text = "Por favor, insira um valor diferente de zero no segundo valor"
        binary_val = bin(res)
        decimal_val = str(res)
        hex_val = hex(res)
        octal_val = oct(res)
        val9 = (f"Binario: {binary_val}\nDecimal: {decimal_val}\nHexadecimal: {hex_val}\nOctal: {octal_val}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)
    def bit1(self):
        val1 = (int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text)))
        res1 = ~val1
        res2 = val1 << 2
        res3 = val1 >> 2
        val9 = (f"Not: {res1}\nShift esquerda: {res2}\nShift Direita: {res3}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)
    def bit2(self):
        val1 = (int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val6.text)))
        val2 = (int(self.tratamentoDeTextoVazio(self.help_string.get_screen('SuperCalc').ids.val7.text)))
        res1 = val1 & val2
        res2 = val1 | val2
        res3 = val1 ^ val2
        val9 = (f"And: {res1}\nOr: {res2}\nXor: {res3}")
        self.help_string.get_screen('SuperCalc').ids.val9.text = val9
        self.help_string.get_screen('SuperCalc').ids.val9.text = str(val9)
if __name__ == '__main__':
    MainApp().run()