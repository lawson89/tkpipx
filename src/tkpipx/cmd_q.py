from tkinter.ttk import Widget


class AbstractCommand:
    def __init__(self, widget: Widget = None):
        pass

    def run_task(self):
        pass

    def update_ui(self):
        pass
