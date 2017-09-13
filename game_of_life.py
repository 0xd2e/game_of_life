#!/usr/bin/python3

"""Conway's Game of Life"""


import numpy as np
from scipy.ndimage import convolve

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns


def update(iframe, world, neighborhood, show_iter, plot_options):
    """
    Inputs:

    iframe -- integer number, iteration counter

    world -- 2D numpy array of integers, main grid

    neighborhood -- 3x3 numpy array of booleans, matrix defining
                    surroundings of a cell (Moore neighborhood)

    show_iter -- boolean, show iteration counter if True

    plot_options -- dictionary with valid matplotlib plot parameters


    Recalculates world and updates plot.


    Update rules:

    ** mark cell as alive if:
       -- the cell is alive and has 2 or 3 alive cells in its neighborhood
       -- the cell is dead and has exactly 3 alive cells in its neighborhood

    ** otherwise mark the cell as dead


    This fuction does not return any value.
    """

    # Count alive cells in the neighborhood of each cell
    counts = convolve(world, neighborhood, mode='constant', cval=0)

    # Update cells on the grid
    world[:, :] = world * ((counts == 2) + (counts == 3)) + (1 - world) * (counts == 3)

    # Clear the figure before drawing on it
    plt.clf()

    if show_iter:
        plt.title('Iteration: {}'.format(iframe))

    sns.heatmap(world, **plot_options)


def play(world=None, step_number=0, show_iter=False, step_time=300):
    """
    Inputs:

    world -- main grid with initial pattern consists of ones and zeros
          -- if 2D numpy array of integers, uses provided pattern
          -- in other cases creates random pattern (default)

    step_number -- number of iterations of the animation
                -- if positive integer number, updates world a given number of times
                -- in other cases creates an infinite animation loop (default)

    show_iter -- boolean, show iteration counter if True

    step_time -- positive integer number, delay between animation frames
                 in milliseconds


    Displays animated plot.


    This fuction does not return any value.
    """

    fig = plt.figure(num="Conway's Game of Life", facecolor='white')

    plt.axis('equal')
    plt.axis('off')

    sns.set(style='white')
    sns.axes_style(style=None)
    sns.despine(top=True, right=True, left=True, bottom=True, offset=None, trim=True)

    plot_options = {
        'cmap': plt.cm.Blues,
        'cbar': False,
        'linewidths': 1.2,
        'xticklabels': False,
        'yticklabels': False,
        'square': True,
        'annot': False
    }

    neighborhood = np.array([[1, 1, 1],
                             [1, 0, 1],
                             [1, 1, 1]], dtype=np.bool)

    if not isinstance(step_number, int) or step_number < 1:
        step_number = None

    if not (isinstance(world, np.ndarray) and
            len(world.shape) == 2 and
            issubclass(world.dtype.type, np.integer) and
            np.max(world) == 1 and
            np.min(world) == 0):
        world = np.random.randint(2, size=(30, 50), dtype=np.uint16)

    anime = FuncAnimation(fig,
                          update,
                          frames=step_number,
                          interval=step_time,
                          init_func=lambda: sns.heatmap(world, **plot_options),
                          fargs=(world, neighborhood, show_iter, plot_options),
                          repeat=False,
                          blit=False)

    plt.show()


if __name__ == '__main__':
    try:
        from patterns import init_world
        play(init_world(3), 8)
    except:
        play()
