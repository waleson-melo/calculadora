import tkinter as tk
import view_calc as vc

class CalcController:
    def __init__(self):
        self.root = tk.Tk()
        self.calc = vc.ViewCalc(self.root, self)

    def start(self):
        self.root.mainloop()

    def operacao(self, op, n1, n2):
        pass

