from matplotlib.widgets import Button, RadioButtons, CheckButtons
import numpy as np
import matplotlib.pyplot as plt


def init():
    x = np.linspace(0, 10, 30)
    y = np.sin(x)

    # Plotting
    fig = plt.figure()
    ax = fig.subplots()
    p, = ax.plot(x, y, 'o', color='black', label='Plot 1')
    plt.subplots_adjust(left=0.3, bottom=0.25)
    plt.scatter(x, y)

    # Grid display control
    ax_button = plt.axes([0.25, 0.1, 0.08, 0.05])
    grid_button = Button(ax_button, 'Grid', color='white', hovercolor='grey')

    def grid_display(val):
        ax.grid()
        fig.canvas.draw()  # redraw the figure

    grid_button.on_clicked(grid_display)

    # Color change control
    ax_color = plt.axes([0.02, 0.5, 0.2, 0.3])
    color_button = RadioButtons(ax_color, ['red', 'green', 'blue', 'black'],
                                [False, False, True, False], activecolor='r')

    def color_change(labels):
        p.set_color(labels)
        fig.canvas.draw()

    color_button.on_clicked(color_change)

    plt.show()


if __name__ == '__main__':
    init()
