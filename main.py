from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.clearcolor = (255/255, 250/255, 205/255, 1.0)
Window.size = (400, 650)

#Дизайн приложения
#Builder.load_file('win.kv')

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
sr.LANGUAGE = 'ru-RU'

class BoxApp(App):
    def voice(self, instance):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-RU')
            trueText = text.capitalize()
            trueText += '.'
            self.lb1.text = str(trueText)
        except Exception:
            self.lb1.text = str('Вы ничего не говорите или у вас проблема с микрофоном!')

    def build(self):
        b1 = BoxLayout(orientation = 'vertical', padding = 20)
        g1 = GridLayout(cols = 1)
        self.lb1 = Label(text='Здравствуйте!', color = (0,0,0,1), font_size = 40, halign = 'center',
                         valign = 'center', size_hint = (1, .4), text_size = (400 - 10, 500 * .4 - 10))
        b1.add_widget(self.lb1)
        g1.add_widget(Widget())
        g1.add_widget(Button(background_down ='microphone_on.png', background_normal = 'microphone_down.png', on_press = self.voice))
        b1.add_widget(g1)
        return b1

if __name__ == '__main__':
    BoxApp().run()
