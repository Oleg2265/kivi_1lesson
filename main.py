from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


Window.size = (800, 600) 

class MainScreen(Screen):
    def go_to_game_selection(self, *args):
        self.manager.current = 'game_selection'

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)


        self.title = Label(text='Гра', font_size='48sp', size_hint=(1,0.8))
        layout.add_widget(self.title)


        play_button = Button(text='Грати', font_size='54sp', size_hint=(1,0.2))
        play_button.bind(on_press=self.go_to_game_selection)
        layout.add_widget(play_button)



class GameSelectionScreen(Screen):
    def go_to_game_basketball(self, *args):
        self.manager.current = 'basketball'

    def go_to_game_football(self, *args):
        self.manager.current = 'football'

    def __init__(self, **kwargs):
        super(GameSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        basketball_button = Button(text='Грати в баскетбол', font_size='54sp', size_hint=(1, 0.2))
        basketball_button.bind(on_press=self.go_to_game_basketball)
        layout.add_widget(basketball_button)

        football_button = Button(text='Грати в футбол', font_size='54sp', size_hint=(1, 0.2))
        football_button.bind(on_press=self.go_to_game_football)
        layout.add_widget(football_button)




class BasketballScreen(Screen):

    def go_to_game_basketball_back(self, *args):
        self.manager.current = 'game_selection'


    def __init__(self, **kwargs):
        super(BasketballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)




        basketball_button_back = Button(text='повернутись', font_size='54sp', size_hint=(1, 0.2))
        basketball_button_back.bind(on_press=self.go_to_game_basketball_back)
        layout.add_widget(basketball_button_back)


        self.background = Image(source = 'img_2.png', size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(source = 'ball.png',)







class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        sm.add_widget(BasketballScreen(name='basketball'))


        return sm


if __name__ == '__main__':
    ClickerApp().run()

class ScrButton(Button):
    def __init__(self, screen, direction="right",goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Myapp(App):
    def build(self):
        txt = Label(text = "Виберіть екран")
        box_button = BoxLayout()
        box_button1 = BoxLayout(orientation = "vertical", padding=8, spacing=8)





app = Myapp()
app.run()
