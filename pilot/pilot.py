import os

from data_interface import DataInterface
from window import Window

path_dir = os.path.dirname(os.path.realpath(__file__))


class Pilot(Window):
    def __init__(self, *args):
        super().__init__(f"{path_dir}\\pilot.ui", *args)

    def update_data(self):
        # Display latest data for window
        pass
        # print(data.ambient_temperature)
