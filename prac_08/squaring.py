"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
yufei wang
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'yufei wang'


class SquareNumberApp(App):
    def build(self):
        Window.size = (300, 100)  # window sized to fit in all label text
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
