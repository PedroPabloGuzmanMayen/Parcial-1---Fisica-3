import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
from mpl_interactions import ioff, panhandler, zoom_factory
import matplotlib.pyplot as plt
from ElectricField import ElectricField

class MatplotlibGUI:
    def plotRingorDisc(self, fill, ratio):
        self.ax.clear()
        self.ax.grid(True)
        ellipse = patches.Ellipse((0,0), 2*ratio/2, 2*ratio, fill=fill)
        self.ax.add_patch(ellipse)
        self.canvas.draw()

    def plotLine(self, ratio):
        self.ax.clear()
        self.ax.grid(True)
        rectangle = patches.Rectangle((((-2*ratio/2)/2),(-2*ratio/2)), 2*ratio/2, 2*ratio)
        self.ax.add_patch(rectangle)
        self.canvas.draw()

    def plotDOt(self, x_component, y_component):
        self.ax.plot(x_component, y_component, marker='o', markersize=8, color='red')
        self.canvas.draw()
    def drawArrow(self, x_component):
        self.ax.arrow(x = x_component, y = 0, dx= 5, dy=0)
    
    def calculateElectricField(self):
        #Serie de condiciones las cuáles no permiten errores en el programa
        if self.option.get() == "":
            messagebox.showerror("Error", "Por favor, selecciona una opción")
        elif not self.cordinates.get() or not self.ratio.get():
            messagebox.showerror("Error", "Por favor, ingresa valores en los campos de coordenadas y radio")
        elif not self.cordinates.get().isdigit():
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos ")
        elif not self.ratio.get().isdigit():
            messagebox.showerror("Error", "Por favor, ingresa valores numericos")
        elif int(self.cordinates.get()) < 0:
            messagebox.showerror("Coordenadas negativas", "Por favor, ingresa solamente valores positivos")
        #Si no hay ningún problema con los valores ingresados por el usuario, se ejecutará este trozo de código
        else:
            if self.option.get() == "Anillo":
                self.plotRingorDisc(False, float(self.ratio.get()))
            elif self.option.get() == "Disco":
                self.plotRingorDisc(True, float(self.ratio.get()))
            elif self.option.get() == "Línea":
                self.plotLine(int(self.ratio.get()))
            self.plotDOt([int(self.cordinates.get())], [0]) #El punto siempre se dibuja, no importa la opción del usuario
            self.drawArrow(int(self.cordinates.get()))

    
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz campos eléctricos")
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.ax.grid(True)
        tk.Label(text="Elije la distribución de carga y las mediad que deseas para el radio o la longitud de esta").pack()
        tk.Label(text="Nota: el valor de la distribución de carga es: 1e-06 C ").pack()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Habilitar zoom mediante el mouse de la computadora
        zoom_factory(self.ax, base_scale=1.1)
        #Habilitar la barra de herramientas
        toolbar = NavigationToolbar2Tk(self.canvas, self.master, pack_toolbar=False)
        toolbar.update()
        toolbar.pack()
        toolbar.pan() #Habilitar la navegación mediante el mouse
        #Definir los botones para dibujar las distribuciones de carga
        self.option = tk.StringVar() #Variable para almacenar la opción seleccionada en el menu desplegable
        tk.Label(text="Elije la disribución de carga: ").pack()
        tk.OptionMenu(self.master, self.option, "Anillo", "Disco", "Línea").pack()
        tk.Label(text= "Elije las coordenadas del punto en el que quieres medir el campo eléctrico: ").pack() 
        self.cordinates = tk.Entry(self.master) #Campo de texto para ingresar la coordenada deseada
        self.cordinates.pack()
        tk.Label(text="Elije el radio o longitud del campo").pack()
        self.ratio = tk.Entry(self.master) #Campo de texto para ingresar el radio o longitud 
        self.ratio.pack()
        tk.Button(text= "Calcular campo eléctrico", command = lambda: self.calculateElectricField()).pack() #Botón para calcular el campo




if __name__ == "__main__":
    root = tk.Tk()
    app = MatplotlibGUI(root)
    root.mainloop()

