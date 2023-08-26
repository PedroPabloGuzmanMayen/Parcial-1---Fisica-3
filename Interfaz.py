import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
from mpl_interactions import ioff, panhandler, zoom_factory
import matplotlib.pyplot as plt
from ElectricField import ElectricField

class MatplotlibGUI:
    #Esta función dibuja el anillo o el disco, pues son figuras similares. El parámetro fill es un booleano es cuál determino si la figura debe rellenarse o no (si es disco hay que rellenar la figura, si es anillo no hay que rellenar). El parámetro ratio es el radio de la figura
    def plotRingorDisc(self, fill, ratio):
        self.ax.clear() #Borrar todo lo que hay en la gráfica
        self.ax.grid(True) #Dibujar nuevamente la cuadrícula
        ellipse = patches.Ellipse((0,0), 2*ratio/2, 2*ratio, fill=fill) #Usar la librería patches para dibujar la una elipse con centro en el origen y con el radio especificado por el usuario
        self.ax.add_patch(ellipse) #Añadir la elipse al gráfico
        self.canvas.draw() #Mostrar la elipse
    #Esta función dibuja la línea de carga. El parémetro ratio es la longitud deseada de la línea
    def plotLine(self, ratio):
        self.ax.clear() #Borrar todo lo que hay en la gráfica
        self.ax.grid(True) #Dibujar la cuadrícula
        rectangle = patches.Rectangle((((-ratio/2)/2),(-ratio/2)), ratio/2, ratio) #Usar la librería patches y dibujar un rectángulo con centro en el origen y longitud especificada por el usuario
        self.ax.add_patch(rectangle) #Añadir el rectángulo al gráfico
        self.canvas.draw() #Mostrar el rectángulo
    #Esta función dibuja el punto especificado por el usuario. EL parámetro es la coordenada x especificada por el usuario
    def plotDOt(self, x_component):
        self.ax.plot(x_component, [0], marker='o', markersize=8, color='red') #DIbujar el punto especificado
        self.canvas.draw() #Añadir a la gráfica
    #Esta función dibuja la flecha que indica el valor del campo eléctrico. El parámetro se refiere a la coordenada x
    def drawArrow(self, x_component):
        self.ax.arrow(x = x_component, y = 0, dx= x_component, dy=0) #Dibujar la flecha con base es y=0 y la coordenada especifciada por el usuario. La longitud x será igual a la coordenada x, mientras que la altura será 0
    
    def calculateElectricField(self):
        #Si el usuario no ingresa ningun valor en los debidos campos, mandar el mensaje 
        if self.option.get() == "":
            messagebox.showerror("Error", "Por favor, selecciona una opción")
        else:
            try:
                #Evaluar si los valores ingresados son números
                cordinate_value = float(self.cordinates.get())
                ratio_value = float(self.ratio.get())
                #Si los valores son números, se dibujan y calculan los campos eléctricos de cada figura 
                if self.option.get() == "Anillo":
                    self.plotRingorDisc(False, ratio_value)
                elif self.option.get() == "Disco":
                    self.plotRingorDisc(True, ratio_value)
                elif self.option.get() == "Línea":
                    self.plotLine(ratio_value)
        
                self.plotDOt([cordinate_value])
                self.drawArrow(cordinate_value)
            #Si no son valores numéricos, mostrar el error
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa valores numéricos")

    
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

