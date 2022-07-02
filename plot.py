from matplotlib.widgets import Button, RadioButtons, CheckButtons
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 30)
y = np.sin(x)

# Plotting
fig = plt.figure()
ax = fig.subplots()
plt.plot(x, y, 'o', color='black')
plt.subplots_adjust(left=0.3, bottom=0.25)
plt.scatter(x, y)

# Button
ax_button = plt.axes([0.25, 0.1, 0.08, 0.05])

# properties of the button
grid_button = Button(ax_button, 'Grid', color='white', hovercolor='grey')


def grid(val):
    ax.grid()
    fig.canvas.draw()  # redraw the figure


# enable/disable grid
grid_button.on_clicked(grid)

plt.show()
