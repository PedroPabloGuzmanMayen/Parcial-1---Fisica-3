import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
from mpl_interactions import ioff, panhandler, zoom_factory
import matplotlib.pyplot as plt

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
    
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz campos eléctricos")
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.ax.grid(True)

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
        tk.Button(self.master, text="Dibujar anillo", command=lambda: self.plotRingorDisc(False, 3)).pack()
        tk.Button(self.master, text="Dibujar disco", command=lambda: self.plotRingorDisc(True, 3)).pack()
        tk.Button(self.master, text="Dibujar línea", command=lambda: self.plotLine(3)).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MatplotlibGUI(root)
    root.mainloop()

