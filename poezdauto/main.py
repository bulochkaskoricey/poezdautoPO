from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import mainthread
import threading
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
import webbrowser

Window.clearcolor = (255 / 255, 198 / 255, 123 / 255, 222)
Window.title = "PoezdRu"

Builder.load_string("""




<MenuScreen>:
    labelone: Label
    
    BoxLayout:
        
	    orientation: "vertical"
        spacing: 20
	    
	    
        

        Image:
            source: 'eee.png'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.7, 1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}


	    MDLabel:
	        id: Label
		    font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 1.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    text: "Что вам нужно ?"
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'white'
		    



	    MDFillRoundFlatIconButton:
		    text: "Купить билет"
		    bold: True
		    
		    background_color:'#3A79FF'
		    size_hint: (0.7, 0.5)
		    on_press: root.manager.current = 'pay'
		    color:'#E6F1FF'
		    padding_y: (9)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "1234.png"
            
            
		    


	    MDFillRoundFlatIconButton:
		    text: "Узнать погоду"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    on_press: root.manager.current = 'settings'
		    color:'#E6F1FF'
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "123.png"

	    MDFillRoundFlatIconButton:
		    text: "Сообщить об ошибке"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    on_press: root.callback3()
		    color:'#E6F1FF'
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "12345.png"
		    

	    MDFillRoundFlatIconButton:
	        id: Button_4
		    text: "О работе"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    color:'#E6F1FF'
		    on_press: root.callback4()
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "123456.png"
		    
        MDBottomNavigation:
            #panel_color: "#eeeaea"
            selected_color_background: "orange"
            text_color_active: "lightgrey"

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"
                

                MDLabel:
                    text: 'Mail'
                    halign: 'center'
                    color: 'white'
                    


            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'
                badge_icon: "numeric-5"

                MDLabel:
                    text: 'Twitter'
                    halign: 'center'
                    color: 'white'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'LinkedIN'
                icon: 'linkedin'

                MDLabel:
                    text: 'LinkedIN'
                    halign: 'center'
                    color: 'white'

<SettingsScreen>:
    txt: txt
    inf:Inf
    
    BoxLayout:
        orientation: "vertical"
	    
	    
	    spacing:20
	    
	    MDLabel:
	        id: Inf
	        text: "Укажите город в котором хотите узнать погоду:"
	        font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 1.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'white'
	    
	    
	    MDTextField:
            hint_text: "Город"
            mode: "fill"
	        id: txt
		    multiline: False
		    size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
		    on_text: 
		    

	    
        MDFillRoundFlatIconButton:
            text: 'Узнать'
            on_press: root.printTxt(txt.text)
            on_release:root.pogoda()
            background_color:'#476BD6'
            size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
		    
        MDFillRoundFlatIconButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'menu'
            background_color:'#476BD6'
		    size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        MDBottomNavigation:
            #panel_color: "#eeeaea"
            selected_color_background: "orange"
            text_color_active: "lightgrey"

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"

                MDLabel:
                    text: 'Mail'
                    halign: 'center'
                    color: 'white'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'
                badge_icon: "numeric-5"

                MDLabel:
                    text: 'Twitter'
                    halign: 'center'
                    color: 'white'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'LinkedIN'
                icon: 'linkedin'

                MDLabel:
                    text: 'LinkedIN'
                    halign: 'center'
                    color: 'white'
        
<PayScreen>:
    city1: city1
    city2: city2
    cit: gor
    
    BoxLayout:
        id: grid_id
        orientation: "vertical"
	    spacing: 20
	    
	    
	    
	    Label:
	        id: gor
	        text: "Укажите город посадки и город прибытия"
	        font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 11.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'white'
	    
	    
	    MDTextField:
            hint_text: "Город посадки"
            mode: "fill"
	        id: city1
		    multiline: False
		    padding_y: (5,5)
		    size_hint: (0.4, 0.3)
	        pos_hint: {"center_x": 0.5, "center_y":0.5}
		    on_text: 
		    
        MDTextField:
            hint_text: "Город прибытия"
            mode: "fill"
	        id: city2
		    multiline: False
		    padding_y: (5,5)
		    size_hint: (0.4, 0.3)
	        pos_hint: {"center_x": 0.5, "center_y":0.5}
		    on_text: 
		    
	    
	    MDFillRoundFlatIconButton:
            text: 'Оплатить'
            on_press: root.oplata((city1.text)and(city2.text))
            on_release: root.wert()
            on_release: root.add_buttons()
            background_color:'#476BD6'
		    size_hint: (0.4, 0.3)
	        pos_hint: {"center_x": 0.5, "center_y":0.5}
	    
	    
        MDFillRoundFlatIconButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'menu'
            background_color:'#476BD6'
		    size_hint: (0.4, 0.3)
	        pos_hint: {"center_x": 0.5, "center_y":0.5}
		            
		MDBottomNavigation:
            #panel_color: "#eeeaea"
            selected_color_background: "orange"
            text_color_active: "lightgrey"

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"
                

                MDLabel:
                    text: 'Mail'
                    halign: 'center'
                    color: 'white'
                    


            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'
                badge_icon: "numeric-5"

                MDLabel:
                    text: 'Twitter'
                    halign: 'center'
                    color: 'white'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'LinkedIN'
                icon: 'linkedin'

                MDLabel:
                    text: 'LinkedIN'
                    halign: 'center'
                    color: 'white'            
		            
<Taper>:
    
    BoxLayout:
        orientation: "vertical"
	    size_hint: (0.95, 0.95)
	    pos_hint: {"center_x": 0.65, "center_y":0.5}
	    spacing:30
	    
	    Label:
	        text: "Ваш билет:"
	        font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 11.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	    
		    
		    
		Image:
            source: 'bil.jpg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.7, 1)
	        
	    MDRectangleFlatButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'menu'
            background_color:'#476BD6'
		    size_hint: (0.7, 0.2)

""")


class MenuScreen(Screen):

    def callback3(self):
        self.labelone.text = "Если вы нашли ошибку, то \nсоветуем написать нам по \nданной ссылке:@mavrikbot \nМодерация обязательно ответит и\nпоможет вам в решении вашей проблемы. \nС уважением команда разработчиков !"

    def callback4(self):
        self.labelone.text = "NATRY inc. \nВерсия 0.7 (Betta)"



class SettingsScreen(Screen):
    pass

    def printTxt(instance, text):
        OWM_Mark = text


        from pyowm import OWM
        global watter
        owm = OWM('825cef665073edbb21d9f7d82d226b4d')

        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(OWM_Mark)
        w = observation.weather

        # температура
        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']
        # скорость ветра
        wi = w.wind()['speed']
        # Влажность
        humi = w.humidity
        # облачность
        cl = w.clouds
        # время
        ti = w.reference_time('iso')

        watter = (f"В городе {OWM_Mark} \nтемпература {t1}, \nощущается как {t2}, \nмаксимальная темпа {t3}, \nминимальная темпа {t4}")

    def pogoda(self):
        self.inf.text = watter


class PayScreen(Screen):
    pass

    def oplata(instance, text):
        city1 = text
        city2 = text
        global pr
        if city1 + city2 == 'СочиСочи':
            pr = ("Стоимость билета по маршруту Москва Сочи: 3486 рублей\nОплатить ?")


        elif city1 + city2 == 'АдлерАдлер':
            pr = ('Стоимость билета по маршруту Москва Адлер: 3486 рублей\nОплатить ?')

        elif city1 + city2 == 'НорильскНорильск':
            pr = ('Стоимость билета по маршруту Москва Норильск: 3486 рублей\nОплатить ?')

        elif city1 + city2 == 'АнапаАнапа':
            pr = ('Стоимость билета по маршруту Москва Анапа: 3486 рублей\nОплатить ?')


        else:
            pr = ("Такого маршрута нету\nПовторите попытку")



    def wert(self):
        self.cit.text = pr





    def add_buttons(self):
        new_btn = MDRectangleFlatButton(text = "Да" ,size_hint = (0.7, 0.2),pos = (20,100))
        new_btn.bind(on_press=self.on_press_button)
        new_btn.bind(on_press=self.oner)

        self.ids.grid_id.add_widget(new_btn)

        return MDRectangleFlatButton
    def on_press_button(self, instancce):
        self.manager.current = 'top'

    def oner(self, instancce):
        webbrowser.open('https://my.qiwi.com/Mykhayl-LQRB1GqfiH', new=2)


class Taper(Screen):
    pass


class MyApp(MDApp):
    running = True

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(PayScreen(name='pay'))
        sm.add_widget(Taper(name='top'))
        self.theme_cls.theme_style = "Dark"
        return sm


    def process(self):
        text = self.root.ids.Inp.text


    def on_stop(self):
        self.running = False


if __name__ == '__main__':
    MyApp().run()
