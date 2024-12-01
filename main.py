from kivy.app import App
from kivy.uix.label import Label

class HolaMundoApp(App):
    def build(self):
        # Crear una etiqueta con el texto "Hola Mundo"
        return Label(text='Hola Mundo', font_size='30sp', halign='center', valign='middle')

if __name__ == '__main__':
    HolaMundoApp().run()
