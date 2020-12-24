import tkinter as tk
import view_calc as vc
import model_calc as mc

class CalcController:
    def __init__(self):
        self.root = tk.Tk()
        self.calc = vc.ViewCalc(self.root, self)
        self.moc = mc.ModelCalc()

    def start(self):
        self.root.mainloop()

    def operacao(self, op, n1, n2):
        num1 = n1.get()
        num2 = n2.get()
        if op == "somar":
            resultado = self.moc.somar(num1, num2)
            self.calc.mostrar_resultado(resultado)
        elif op == "subtrair":
            resultado = self.moc.subtrair(num1, num2)
            self.calc.mostrar_resultado(resultado)
        elif op == "multiplicar":
            resultado = self.moc.multiplicar(num1, num2)
            self.calc.mostrar_resultado(resultado)
        elif op == "dividir":
            resultado = self.moc.dividir(num1, num2)
            self.calc.mostrar_resultado(resultado)

