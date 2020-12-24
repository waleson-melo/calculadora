import tkinter as tk
import view.view_calc as vc


if __name__ == "__main__":
    root = tk.Tk()
    appCalc = vc.AppCalc(root)
    root.mainloop()