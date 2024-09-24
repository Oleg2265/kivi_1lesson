import random

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Line, Color
from random import randint


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

    def go_to_game_hockey(self, *args):
        self.manager.current = 'hockey'


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

        hockey_button = Button(text='Грати в хокей', font_size='54sp', size_hint=(1, 0.2))
        hockey_button.bind(on_press=self.go_to_game_hockey)
        layout.add_widget(hockey_button)




class BasketballScreen(Screen):
    score = NumericProperty(0)

    def go_to_game_basketball_back(self, *args):
        self.manager.current = 'game_selection'


    def __init__(self, **kwargs):
        super(BasketballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)







        self.background = Image(source = 'img_2.png',allow_stretch=True, keep_ratio=False, size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(source = 'ball.png', allow_stretch=True, size_hint = (0.2, 0.2), size=(10, 15))
        self.ball.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.ball.bind(on_touch_down = self.ball_clicked)
        layout.add_widget(self.ball)

        self.score_label = Label(text= "Score: 0 ", font_size="24sp", size_hint=(1, 0.1),)
        layout.add_widget(self.score_label)

        basketball_button_back = Button(text='повернутись', font_size='54sp', size_hint=(0.45, 0.1), pos_hint={"x": 0, "y": 0})
        basketball_button_back.bind(on_press=self.go_to_game_basketball_back)
        layout.add_widget(basketball_button_back)




    def ball_clicked(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            self.ball_click_animation()

    def ball_click_animation(self):
        anim = Animation(size=(150, 150), duration = 0.3) + Animation(size=(100,100), duration=0.3)
        anim.start(self.ball)




class HockeyballScreen(Screen):
    score = NumericProperty(0)

    def go_to_game_Hockey_back(self, *args):
        self.manager.current = 'game_selection'


    def __init__(self, **kwargs):
        super(HockeyballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)







        self.background = Image(source = 'img_5.png',allow_stretch=True, keep_ratio=False, size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(source = 'img_6.png', allow_stretch=True, size_hint = (0.2, 0.2), size=(10, 15))
        self.ball.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.ball.bind(on_touch_down = self.ball_clicked)
        layout.add_widget(self.ball)

        self.score_label = Label(text= "Score: 0 ", font_size="24sp", size_hint=(1, 0.1),)
        layout.add_widget(self.score_label)

        hockey_button_back = Button(text='повернутись', font_size='54sp', size_hint=(0.45, 0.1), pos_hint={"x": 0, "y": 0})
        hockey_button_back.bind(on_press=self.go_to_game_Hockey_back)
        layout.add_widget(hockey_button_back)


    def ball_clicked(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            self.ball_click_animation()

    def ball_click_animation(self):
        anim = Animation(size=(150, 150),opacity=0.5, duration=0.3) + Animation(size=(100, 100),opacity=1, duration=0.3)
        anim.start(self.ball)



class FootballScreen(Screen):
    score = NumericProperty(0)

    def go_to_game_football_back(self, *args):
        self.manager.current = 'game_selection'


    def __init__(self, **kwargs):
        super(FootballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)







        self.background = Image(source = 'img_3.png',allow_stretch=True, keep_ratio=False, size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(source = 'img_4.png', allow_stretch=True, size_hint = (0.2, 0.2), size=(10, 15))
        self.ball.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.ball.bind(on_touch_down = self.ball_clicked)
        layout.add_widget(self.ball)

        self.score_label = Label(text= "Score: 0 ", font_size="24sp", size_hint=(1, 0.1),)
        layout.add_widget(self.score_label)

        basketball_button_back = Button(text='повернутись', font_size='54sp', size_hint=(0.45, 0.1), pos_hint={"x": 0, "y": 0})
        basketball_button_back.bind(on_press=self.go_to_game_football_back)
        layout.add_widget(basketball_button_back)


    def ball_clicked(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            self.ball_click_animation()

    def ball_click_animation(self):
        anim = Animation(pos=(80, 10))
        anim = Animation(size=(300, 300), duration=1) + Animation(size=(100,100),pos=(400, 300), duration=1)
        anim.start(self.ball)




class ClickerApp(App):
    def build(self):

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        sm.add_widget(BasketballScreen(name='basketball'))
        sm.add_widget(FootballScreen(name="football"))
        sm.add_widget(HockeyballScreen(name="hockey"))



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
