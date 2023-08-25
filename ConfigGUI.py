import tkinter as tk
class ConfigGUI:

    def show(self):
        tk.Label(self.window, text=self.option.get()).pack()
        if(self.option.get() == "Línea"):
            print("Hola")

    def ConfigGUI(self, menu):

        self.window = tk.Tk()
        self.window.title = "Configuración"
        self.menu = menu
        self.option = tk.StringVar()
        self.option.set("Anillo")
        tk.Label(text="Elije la distribución de carga y las mediad que deseas para el radio o la longitud de esta").pack()
        tk.Label(text="Nota: el valor de la distribución de carga es: ").pack()
        tk.Label(text="Elije la disribución de carga: ").pack()
        tk.OptionMenu(self.window, self.option, "Anillo", "Disco", "Línea").pack()
        tk.Label(text= "Elije las coordenadas del punto en el que quieres medir el campo eléctrico: ").pack()
        tk.B

        self.window.mainloop()

ConfigGUI().ConfigGUI(3)


