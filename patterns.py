#!/usr/bin/python3

"""Collection of simple pattern for Conway's Game of Life"""


import numpy as np


def init_world(pattern=0):
    """
    Input:

    pattern -- integer, pattern number
            -- constants: 1
            -- oscillators: 2, 3, 11
            -- moving patterns: 4
            -- othe patterns: 5, 6, 7, 8, 9, 10
            -- the default pattern


    Collection of initial patterns for Conway's game of life..


    Returns 2D numpy array of integers
    with pattern consists of ones and zeros.
    """

    integer = np.uint16
    world_size = (29, 49)

    if pattern == 1:

        # Constant (stable) patterns
        world = np.zeros((25, 25), dtype=integer)

        # "Block"
        world[1:3, 1:3] = 1

        # "Block"
        world[4:6, 6:8] = 1

        # "Tub"
        world[18, 15] = 1
        world[20, 15] = 1
        world[19, 14] = 1
        world[19, 16] = 1

        # "Boat"
        world[16, 6] = 1
        world[17, 7] = 1
        world[16, 8] = 1
        world[15, 6:8] = 1

        # "Loaf"
        world[3, 17:19] = 1
        world[4:6, 19] = 1
        world[4, 16] = 1
        world[5, 17] = 1
        world[6, 18] = 1

        # "Beehive"
        world[22, 4] = 1
        world[22, 7] = 1
        world[21, 5:7] = 1
        world[23, 5:7] = 1

        world[10, 11:13] = 1
        world[11:13, 10] = 1
        world[11:13, 13] = 1
        world[13, 11:13] = 1

    if pattern == 2:

        # Oscillator patterns
        world = np.zeros((30, 30), dtype=integer)

        # "Toad"
        world[2, 19:22] = 1
        world[3, 18:21] = 1

        # "Beacon"
        world[10:12, 22:24] = 1
        world[12:14, 24:26] = 1

        # "Pentadecathlon"
        world[17:25, 4:7] = 1
        world[18, 5] = 0
        world[23, 5] = 0

        # "Fountain"
        world[25, 19:26] = 1
        world[25, 22] = 0
        world[24, 19] = 1
        world[24, 25] = 1
        world[23, 21] = 1
        world[23, 23] = 1
        world[21, 19] = 1
        world[21, 25] = 1
        world[22, 20:22] = 1
        world[22, 23:25] = 1

        world[4:7, 4:7] = 1
        world[5, 5] = 0

    elif pattern == 3:

        # Another oscillator pattern
        world = np.zeros((18, 20), dtype=integer)

        world[4:6, 5:11] = 1
        world[7:13, 5:7] = 1
        world[11:13, 8:14] = 1
        world[4:10, 12:14] = 1

    elif pattern == 4:

        world = np.zeros(world_size, dtype=integer)

        # "Lightweight spaceship"
        world[6, 3:7] = 1
        world[5, 2] = 1
        world[3, 2] = 1
        world[3, 5] = 1
        world[4:6, 6] = 1

        # "Glider"
        world[12, 4:7] = 1
        world[11, 6] = 1
        world[10, 5] = 1

    elif pattern == 5:

        world = np.zeros(world_size, dtype=integer)

        # "The R-pentomino"
        world[14, 30:32] = 1
        world[15, 29:31] = 1
        world[16, 30] = 1

    elif pattern == 6:

        world = np.zeros(world_size, dtype=integer)

        world[1::2, ::2] = 1
        world[::2, 1::2] = 1

    elif pattern == 7:

        world = np.zeros(world_size, dtype=integer)

        world[1::2, ::2] = 1
        world[::3, 1::3] = 1

    elif pattern == 8:

        world = np.zeros(world_size, dtype=integer)

        world[:, 1::2] = 1

    elif pattern == 9:

        world = np.zeros(world_size, dtype=integer)

        world[:, 15:18] = 1
        world[14:17, :] = 1

        world[:, 16] = 0
        world[15, :] = 0

    elif pattern == 10:

        world = np.zeros(world_size, dtype=integer)

        # Checkerboard
        world[0::2, 0::2] = 1
        world[1::2, 1::2] = 1

    elif pattern == 11:

        # Another oscillator pattern
        world = np.zeros((17, 17), dtype=integer)

        # Pulsar
        world[2, 4:7] = 1
        world[2, 10:13] = 1
        world[7, 4:7] = 1
        world[7, 10:13] = 1
        world[9, 4:7] = 1
        world[9, 10:13] = 1
        world[14, 4:7] = 1
        world[14, 10:13] = 1
        world[4:7, 2] = 1
        world[10:13, 2] = 1
        world[4:7, 7] = 1
        world[10:13, 7] = 1
        world[4:7, 9] = 1
        world[10:13, 9] = 1
        world[4:7, 14] = 1
        world[10:13, 14] = 1

    else:

        world = np.zeros(world_size, dtype=integer)

        world[:, 19] = 1
        world[15, :] = 1

    return world
