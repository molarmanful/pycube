# pycube

[![Documentation Status](https://readthedocs.org/projects/pycube/badge/?version=latest)](https://pycube.readthedocs.io/en/latest/?badge=latest)

A Rubik's Cube simulation made with Processing.py.


## Installation

Requirements:

- Processing.py 3.x
- PeasyCam library (installed from the Processing IDE)

## Controls

`pycube` has 2 modes: keyboard and mouse.

Pressing `Enter` switches between the modes. `Space` scrambles the cube and prepares it for a timed attempt. `Tab` auto-solves the cube. `/` switches between displaying times and statistics. `Q` opens a tutorial website in your browser.

### Mouse Mode

Click on any of the faces to turn them, and drag **from outside** the cube to turn the whole cube. Left-clicks rotate the face clockwise, and right-clicks rotate the face counterclockwise.

### Keyboard Mode

 Key | Move
--- | ---
`Shift` + key | Counterclockwise turn
`R` | Right face
`L` | Left face
`U` | Top face
`D` | Bottom face
`F` | Front face
`B` | Back face
`M` | Middle slice
`E` | Equatorial slice
`S` | Standing slice
`X` | Rotate around X-axis
`Y` | Rotate around Y-axis
`Z` | Rotate around Z-axis

## Timing

To begin a timed attempt, press `Space` to scramble the cube. The timer starts when the first move is made. If the auto-solver is triggered, then a time of `DNF` ( **D**id **N**ot **F**inish) is recorded. The timer ends when the cube is solved.

## Credits

Made by Benjamin Pang and Yusuf Jimoh. Distributable under the MIT License.
