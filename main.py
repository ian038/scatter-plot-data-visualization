from matplotlib.widgets import Button, RadioButtons, CheckButtons
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import widgets


def init():
    x = np.arange(50)
    y = x + 10 * np.random.randn(50)

    # Plotting
    fig = plt.figure()
    ax = fig.subplots()
    p, = ax.plot(x, y, 'o', color='black')
    plt.subplots_adjust(left=0.4, bottom=0.25)
    plt.scatter(x, y)
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_title('Simple Scatter Plot')
    ax.autoscale(enable=True)

    # Grid display control
    ax_button = plt.axes([0.4, 0.1, 0.08, 0.05])
    grid_button = Button(ax_button, 'Grid', color='white', hovercolor='grey')

    def grid_display(val):
        ax.grid()
        plt.draw()  # redraw plot
    grid_button.on_clicked(grid_display)

    # Color change control
    rax = plt.axes([0.1, 0.5, 0.2, 0.3], facecolor='lightgoldenrodyellow')
    rax.set_title('Color Controls')
    color_button = RadioButtons(rax, ('Red', 'Green', 'Blue', 'Black'),
                                [False, False, False, True], activecolor='r')

    def color_change(label):
        p.set_color(label)
        plt.draw()
    color_button.on_clicked(color_change)

    plt.show()


if __name__ == '__main__':
    init()
