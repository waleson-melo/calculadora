import tkinter as tk

class ViewCalc:
    def __init__(self, root, controller):
        self.controller = controller
        # Criando a janela
        root.title("Calculadora")
        root.resizable(False, False)

        # Container
        self.container1 = tk.Frame(root)
        self.container1["pady"] = 10
        self.container1["padx"] = 10
        self.container1.pack()

        self.container2 = tk.Frame(root)
        self.container2["pady"] = 10
        self.container2["padx"] = 10
        self.container2.pack()

        self.container3 = tk.Frame(root)
        self.container3["pady"] = 7
        self.container3["padx"] = 7
        self.container3.pack()

        self.container4 = tk.Frame(root)
        self.container4["pady"] = 10
        self.container4["padx"] = 10
        self.container4.pack()

        # Label e Entry
        self.lbl_numero1 = tk.Label(self.container1)
        self.lbl_numero1["text"] = "Número 1:"
        self.lbl_numero1.pack(side = "left")

        self.ent_numero1 = tk.Entry(self.container1)
        self.ent_numero1.pack(side = "left")

        self.lbl_numero2 = tk.Label(self.container2)
        self.lbl_numero2["text"] = "Número 2:"
        self.lbl_numero2.pack(side = "left")

        self.ent_numero2 = tk.Entry(self.container2)
        self.ent_numero2.pack(side = "left")

        # Resultado
        self.lbl_mensagem = tk.Label(self.container3)
        self.lbl_mensagem["text"] = "Resultado:"
        self.lbl_mensagem.pack(side = "left")

        self.lbl_resultado = tk.Label(self.container3)
        self.lbl_resultado["text"] = ""
        self.lbl_resultado.pack(side = "left")

        # Button
        self.btn_somar = tk.Button(self.container4)
        self.btn_somar["text"] = "+"
        self.btn_somar["width"] = 2
        self.btn_somar["command"] = lambda op = "somar", n1 = self.ent_numero1, n2 = self.ent_numero2 : self.controller.operacao(op, n1, n2)
        self.btn_somar.pack(side = "left")

        self.btn_subtrair = tk.Button(self.container4)
        self.btn_subtrair["text"] = "-"
        self.btn_subtrair["width"] = 2
        self.btn_subtrair["command"] = lambda op = "subtrair", n1 = self.ent_numero1, n2 = self.ent_numero2 : self.controller.operacao(op, n1, n2)
        self.btn_subtrair.pack(side = "left")

        self.btn_multiplicar = tk.Button(self.container4)
        self.btn_multiplicar["text"] = "*"
        self.btn_multiplicar["width"] = 2
        self.btn_multiplicar["command"] = lambda op = "multiplicar", n1 = self.ent_numero1, n2 = self.ent_numero2 : self.controller.operacao(op, n1, n2)
        self.btn_multiplicar.pack(side = "left")

        self.btn_dividir = tk.Button(self.container4)
        self.btn_dividir["text"] = "/"
        self.btn_dividir["width"] = 2
        self.btn_dividir["command"] = lambda op = "dividir", n1 = self.ent_numero1, n2 = self.ent_numero2 : self.controller.operacao(op, n1, n2)
        self.btn_dividir.pack(side = "left")

    def mostrar_resultado(self, resultado):
        self.lbl_resultado["text"] = resultado
        

