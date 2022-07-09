from tkpipx.cmd_q import AbstractCommand
from tkpipx.home_view import Home


class CommandList(AbstractCommand):
    def __init__(self, widget=None):
        self.widget = widget
        self.data = None

    def run_task(self):
        self.data = ('a', 'b', 'c')

    def update_ui(self):
        home: Home = self.widget
        home.u
