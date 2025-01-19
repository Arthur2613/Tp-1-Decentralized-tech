Documentation: Game of Life (Python Implementation)

Overview

This is a Python-based implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Horton Conway. The game runs in the console and adheres to the standard rules of cell evolution.

Features

Grid-based Simulation: A grid represents the environment where cells live and die.

Visualization: # represents live cells, and spaces represent dead cells.

Interactivity: You can stop the simulation at any time by pressing 'q' and hitting Enter.

Rules: The game evolves based on the number of neighbors each cell has.

Rules of the Game

A live cell with fewer than 2 live neighbors dies (underpopulation).

A live cell with 2 or 3 live neighbors survives to the next generation.

A live cell with more than 3 live neighbors dies (overpopulation).

A dead cell with exactly 3 live neighbors becomes alive (reproduction).

How to Run the Project

Requirements: Python 3.x must be installed.

Steps:

Save the code into a file, e.g., game_of_life.py.

Open a terminal and navigate to the directory containing the file.

Run the script using the command:

python game_of_life.py

Press Ctrl+C or type q and hit Enter to terminate the game.
