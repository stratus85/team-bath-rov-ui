import os

from data_interface import DataInterface
from window import Window

path_dir = os.path.dirname(os.path.realpath(__file__))


class Copilot(Window):
    def __init__(self, *args):
        super().__init__(f"{path_dir}\\copilot.ui", *args)

    def update_data(self, data: DataInterface):
        # Display latest data for window
        pass
        # print(data.ambient_temperature)
