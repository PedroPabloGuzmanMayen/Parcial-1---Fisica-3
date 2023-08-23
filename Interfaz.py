import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MatplotlibGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Matplotlib GUI")

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot([1, 2, 3, 4], [10, 20, 25, 30], 'b-')
        self.ax.grid(True)  # Add grid to the plot

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        self.canvas_widget.bind("<Button-1>", self.on_click)
        self.canvas_widget.bind("<B1-Motion>", self.on_drag)
        self.canvas_widget.bind("<MouseWheel>", self.on_scroll)

        self.x_range = (0, 5)
        self.y_range = (0, 35)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MatplotlibGUI(root)
    root.mainloop()
