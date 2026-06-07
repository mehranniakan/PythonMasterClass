import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("Calculator")
        self.window.geometry("400x400")

        self.expression = ""

        self.app_widgets()
        self.app_alignment()

    def app_widgets(self):

        self.result_entry = tk.Entry(self.window, font=("Segoe UI", 18), justify="center")
        self.result_entry.insert(0, "0")


        ## [(Keynum, RowNum, ColNum)]
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        ## Create all Keypads
        self.keypads = {}
        for (text, r, c) in self.buttons:
            btn = tk.Button(
                self.window,
                text=text,
                font=("Segoe UI", 14),
                width=4,
                height=2,
                command=lambda t=text: self.on_button_click(t)
            )
            self.keypads[text] = btn

    def app_alignment(self):

        for c in range(4):
            self.window.grid_columnconfigure(c, weight=1, uniform="col")
        for r in range(5):
            self.window.grid_rowconfigure(r, weight=1, uniform="row")

        self.result_entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10, ipady=6)


        for (text, r, c) in self.buttons:
            self.keypads[text].grid(row=r, column=c, sticky="nsew", padx=0, pady=0)


    def on_button_click(self, t: str):
        if t == "C":
            self.expression = ""
            self._set_display("0")
            return

        if t == "=":
            if not self.expression:
                return
            try:
                # هشدار: eval برای پروژه واقعی امن نیست؛ برای تمرین/ماشین‌حساب ساده قابل قبوله
                result = eval(self.expression)
                self.expression = str(result)
                self._set_display(self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
                self._set_display("0")
            return

        self.expression += t
        self._set_display(self.expression)

    def _set_display(self, text: str):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, text)


window = tk.Tk()
app = CalculatorApp(window)
window.mainloop()
