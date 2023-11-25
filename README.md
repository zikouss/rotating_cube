# 3D Cube Rotation Visualization in 2D using Pygame

This Python project demonstrates a 3D cube rotation visualization in a 2D environment using the Pygame library. It enables users to interact with a 3D cube, observing its rotations within a 2D representation.

## Overview

This project employs Pygame to create a window displaying a 3D cube that rotates based on user input. The cube's rotations along the x, y, and z axes are visualized in a 2D environment by projecting its vertices onto a 2D plane.

### Files

- **Cube.py:** Contains functions for cube creation, translation, rotation, drawing, and connecting points.
- **main.py:** Initializes the Pygame window and handles user input for cube rotation.
- **matrix_rotation.py:** Provides functions to generate rotation matrices for x, y, and z axes.
- **matrix_operations.py:** Includes a matrix multiplication function used for rotations.

## Setup and Usage

### Prerequisites

- Python installed on your system.
- Pygame library installed. Install it via pip: `pip install pygame`.

### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/zikouS1/rotating_cube.git
   cd rotating_cube
1. Open the main file:

   ```bash
   python main.py
