import tkinter as tk
class ConfigGUI:

    def ConfigGUI(self, menu):

        self.window = tk.Tk()
        self.window.title = "Configuración"
        self.menu = menu
        self.option = tk.StringVar()
        tk.Label(text="Elije la distribución de carga y las mediad que deseas para el radio o la longitud de esta").pack()
        tk.Label(text="Nota: el valor de la distribución de carga ").pack()
        tk.OptionMenu(self.window, self.option, "Anillo", "Disco", "Línea")


