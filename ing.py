#player и self.player разные имена!!!

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Tic_Tac_Toe(App):
    def build(self):
        left = BoxLayout(orientation = 'vertical')
        player = Label(text = 'Игрок')
        self.player = Label(text = 'X')
        score = Label(text = 'Счёт')
        self.score = Label(text = '0')
        left.add_widget(player)
        left.add_widget(self.player)
        left.add_widget(score)
        left.add_widget(self.score)

        right = BoxLayout(orientation = 'vertical')
        comp = Label(text = 'Комп')
        self.comp = Label(text = 'O')
        score = Label(text = 'Счёт')
        self.score = Label(text = '0')
        right.add_widget(comp)
        right.add_widget(self.comp)
        right.add_widget(score)
        right.add_widget(self.score)
        admin = BoxLayout()
        root = GridLayout(cols = 3)
        self.buttons = []
        for i in range(9):
            self.buttons.append(Button(text='', font_size = 40, on_press = self.game))
        for i in range(9):
            root.add_widget(self.buttons[i])


        admin.add_widget(left)
        admin.add_widget(root)
        admin.add_widget(right)
        return admin

    def game(self, button):
        pass

Game = Tic_Tac_Toe()
Game.run()
