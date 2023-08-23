import matplotlib.pyplot as plt
import numpy as np

# Create a new figure and axis
fig, ax = plt.subplots()

# Draw the outer circle (larger radius)
outer_circle = plt.Circle((0, 0), 3, fill=False, label='Outer Circle')
ax.add_patch(outer_circle)

# Draw the inner circle (smaller radius)
inner_circle = plt.Circle((0, 0), 2, fill=False, label='Inner Circle')
ax.add_patch(inner_circle)

# Draw the point outside the ring
point = plt.Circle((5, 0), 0.1, color='red', label='Point')
ax.add_patch(point)

# Add an arrow pointing to the right from the point
arrow_props = dict(arrowstyle="->", color="blue")
ax.annotate("Arrow", xy=(5, 0), xytext=(5.5, 0), arrowprops=arrow_props)

# Set axis limits
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)

# Add grid and legend
ax.grid()
ax.legend()

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Ring with Point and Arrow')

# Show the plot
plt.show()
