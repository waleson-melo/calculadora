
class ModelCalc:
    def __init__(self):
        pass

    def somar(self, n1, n2):
        try:
            num1 = float(n1)
            num2 = float(n2)
            return num1 + num2
        except:
            return "Invalido"

    def subtrair(self, n1, n2):
        try:
            num1 = float(n1)
            num2 = float(n2)
            return num1 - num2
        except:
            return "Invalido"

    def multiplicar(self, n1, n2):
        try:
            num1 = float(n1)
            num2 = float(n2)
            return num1 * num2
        except:
            return "Invalido"

    def dividir(self, n1, n2):
        try:
            num1 = float(n1)
            num2 = float(n2)
            return num1 / num2
        except:
            return "Invalido"

