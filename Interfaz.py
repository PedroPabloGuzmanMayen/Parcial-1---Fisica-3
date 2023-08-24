import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
import numpy as np


class MatplotlibGUI:

    #Esta función dibuja el anillo o el disco. El parámetro fill es un booleano el cuál indica si la figura debe ser rellenada o no (El disco se rellena par a mostrar que es sólido, el anillo no se rellena). El parámetro ratio indicará el radio de la figura
    def plotRingorDisc(self, fill, ratio):
        self.ax.clear() #Borrar todo lo que había en el plano
        self.ax.grid(True) #Colocar nuevamente la cuadrícula, pues con la función anterior es borrada
        ellipse = patches.Ellipse((0,0), 2*ratio/2, 2*ratio, fill = fill) #Usar la extensión patches de matplotlib para dibujar una elipse
        self.ax.add_patch(ellipse) #Agregar la elipse al plano
        self.canvas.draw() #Dibujar la elipse en el plano

    def plotLine(self, ratio):
        self.ax.clear() #Borrar todo lo que había en el plano
        self.ax.grid(True) #Colocar nuevamente la cuadrícula, pues con la función anterior es borrada
        ellipse = patches.Rectangle((((-2*ratio/2)/2),(-2*ratio/2)), 2*ratio/2, 2*ratio) #Usar la extensión patches de matplotlib para dibujar una elipse
        self.ax.add_patch(ellipse) #Agregar la elipse al plano
        self.canvas.draw() #Dibujar la elipse en el plano
    
        




    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz campos eléctricos")

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot() #Agregar el plano 
        self.ax.grid(True)  # Agregar cuadrícula 

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master) #Crear el objeto
        self.canvas.get_tk_widget().pack() #Agregar a la pantalla de Tkinter 

        toolbar = NavigationToolbar2Tk(self.canvas, self.master, pack_toolbar = False) #Colocar la barra de navegación
        toolbar.update()
        toolbar.pack()

        tk.Button(self.master, text= "Dibujar anillo", command = lambda: self.plotRingorDisc(False, 3)).pack() #Botones para agregar anillos
        tk.Button(self.master, text= "Dibujar disco", command = lambda:self.plotRingorDisc(True, 3) ).pack() #Botones para agregar el disco
        tk.Button(self.master, text= "Dibujar línea", command = lambda:self.plotLine(3) ).pack() #Botón para agregar la línea de carga




     

if __name__ == "__main__":
    root = tk.Tk()
    app = MatplotlibGUI(root)
    root.mainloop()
