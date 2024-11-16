# Graph Visualization with Dijkstra's Algorithm

This project provides a visualization of graphs using **Dijkstra's Algorithm** to find the shortest path between nodes. The graph is represented using the DOT format, and the visualization is rendered using **Pygame**.

## Features

- **Graph Visualization**: Visualize nodes and edges in a directed graph.
- **Arrow Representation**: Edges are represented as arrows pointing from one node to another.
- **Node and Edge Rendering**: Nodes are rendered as circles, and edges as arrows with optional weight labels.
- **Customizable**: Supports customizable node and edge appearances, including scaling of nodes and placement of edge weights.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6+
- Pygame
- Regular expressions (`re` module, which is part of Python's standard library)

### Install Pygame:

To install the required dependencies, you can use `pip` to install Pygame:

```bash
pip install pygame

How to Use
1. Prepare DOT Input
The graph is described using the DOT format, a plain text graph description language. Example:

css
Copy code
