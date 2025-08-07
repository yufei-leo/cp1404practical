"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
yufei wang

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_KM_CONVERSION = 1.60934


class ConvertMilesKm(App):
    output_distance = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_distance = "Enter a distance and press enter"
        return self.root

    def handle_increment(self, increment):
        try:
            current_input = float(self.root.ids.input_distance.text)
        except ValueError:
            self.root.ids.input_distance.text = '0.0'
            current_input = float(self.root.ids.input_distance.text)
        current_input += increment
        self.root.ids.input_distance.text = str(current_input)

    def convert(self):
        try:
            current_input = float(self.root.ids.input_distance.text)
            current_input *= MILES_KM_CONVERSION
            self.output_distance = str(current_input)
        except ValueError:
            self.output_distance = '0.0'


ConvertMilesKm().run()
