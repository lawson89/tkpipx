import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview


class Home(ttk.Frame):

    def test_table_update(self):
        print('hi!')
        self.update_table(rowdata=(('a', 'b'),) )

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.tableview = None
        colors = self.app.style.colors

        b1 = ttk.Button(self, text="Refresh package list", bootstyle=SUCCESS, command=self.test_table_update)
        b1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        coldata = [
            {"text": "Package", "stretch": False},
            "Version",
        ]

        dt = Tableview(
            master=self,
            coldata=coldata,
            rowdata=[],
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )

        dt.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.tableview = dt

    def update_table(self, rowdata):
        print(f'updating table {rowdata}')
        self.tableview.delete_rows()
        self.tableview.insert_rows('end', rowdata)
        self.tableview.load_table_data()


if __name__ == '__main__':
    app = ttk.Window(title='tkpipx', minsize=(200, 200))
    app.columnconfigure(0, weight=1)
    home = Home(app)
    home.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    app.mainloop()
