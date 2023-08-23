import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt  # Import the plt module

class MatplotlibGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Matplotlib GUI")

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)  # Add grid to the plot

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        self.canvas_widget.bind("<Button-1>", self.on_click)
        self.canvas_widget.bind("<B1-Motion>", self.on_drag)
        self.canvas_widget.bind("<MouseWheel>", self.on_scroll)

        self.x_range = (0, 5)
        self.y_range = (0, 35)

        # Create buttons
        self.draw_ring_button = tk.Button(master=self.master, text="Dibujar anillo de carga", command=self.draw_ring)
        self.draw_ring_button.pack()

        self.draw_rectangle_button = tk.Button(master=self.master, text="Dibujar liena de carga", command=self.draw_rectangle)
        self.draw_rectangle_button.pack()

    def on_click(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_drag(self, event):
        dx = (event.x - self.last_x) / self.fig.dpi
        dy = (event.y - self.last_y) / self.fig.dpi
        self.last_x = event.x
        self.last_y = event.y

        self.x_range = (self.x_range[0] - dx, self.x_range[1] - dx)
        self.y_range = (self.y_range[0] + dy, self.y_range[1] + dy)

        self.ax.set_xlim(self.x_range)
        self.ax.set_ylim(self.y_range)
        self.canvas.draw()

    def on_scroll(self, event):
        if event.delta > 0:
            factor = 1.2
        else:
            factor = 1 / 1.2

        x_center = (self.x_range[0] + self.x_range[1]) / 2
        y_center = (self.y_range[0] + self.y_range[1]) / 2

        self.x_range = (x_center - (x_center - self.x_range[0]) * factor,
                        x_center + (self.x_range[1] - x_center) * factor)
        self.y_range = (y_center - (y_center - self.y_range[0]) * factor,
                        y_center + (self.y_range[1] - y_center) * factor)

        self.ax.set_xlim(self.x_range)
        self.ax.set_ylim(self.y_range)
        self.canvas.draw()

    def draw_ring(self):
        # Clear previous drawings
        self.ax.clear()
        self.ax.grid(True)

        # Draw the ring centered on the origin
        self.ax.add_patch(plt.Circle((0, 0), 3, fill=False, color='r', label='Ring'))

        # Set axis limits and labels
        self.ax.set_xlim(self.x_range)
        self.ax.set_ylim(self.y_range)
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')

        self.canvas.draw()

    def draw_rectangle(self):
        # Clear previous drawings
        self.ax.clear()
        self.ax.grid(True)

        # Draw the rectangle centered on the origin
        self.ax.add_patch(plt.Rectangle((-0.25, -5), 0.5, 10, fill=False, color='g', label='Rectangle'))

        # Set axis limits and labels
        self.ax.set_xlim(self.x_range)
        self.ax.set_ylim(self.y_range)
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = MatplotlibGUI(root)
    root.mainloop()

