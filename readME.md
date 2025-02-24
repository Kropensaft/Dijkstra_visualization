
# Visualization of Dijkstra's algorithm using the pyGame python library

This program visualizes a graph, allows users to find and highlight the shortest path between two nodes using Dijkstra's algorithm, and provides step-by-step updates of the algorithm's progress. It integrates interactive visualization via Pygame and supports graph input in DOT format.

---

## Features

- **Graph Visualization**:
  - Displays nodes and edges of a graph.
  - Dimmed background view for the entire graph.

- **Shortest Path Highlighting**:
  - Computes the shortest path between two nodes.
  - Highlights the path with distinct colors (nodes in green, edges in red).

- **Step-by-Step Algorithm Progress**:
  - Displays the iterative steps of Dijkstra's algorithm.

- **Graph Input in DOT Format**:
  - Easily parse and construct graphs from DOT-style strings.

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- Libraries:
  - `python3` Language support 
  - `pygame`  Main rendering engine
  - `pygame_gui` GUI elements
  - `networkx` Node placement and orientation

### Dependecies
Install dependecies using the included bash script. The script isnt OS specific and recognizes and adjusts based on your running OS:
```bash
./dependecies
```
or 
```bash
sudo ./dependencies
```

---

### Program Structure

1. **Graph Class**:
   - Represents the graph using an adjacency list.
   - Provides methods for:
     - Adding edges.
     - Parsing DOT format input.
     - Running Dijkstra's algorithm.
     - Retrieving the shortest path.

2. **Visualization Components**:
   - Uses `Node` and `Arrow` classes to represent nodes and edges for rendering.
   - Renders the graph, highlights paths, and displays weights and node labels.

3. **Interactive Features**:
   - Renders the graph and allows users to select source and target nodes.
   - Highlights the shortest path and dynamically updates based on user input.

---

### How to Run

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <https://github.com/Kropensaft/zapoctak.git>
   cd <\Downloads\zapoctak_clone>
   ```

2. Ensure the required libraries are installed.

3. Run the program:
   ```bash
   python3 main.py
   ```

---

### Input Graph Format

The program accepts graphs in DOT format:
```plaintext
node1 -- node2 [weight=3];
node2 -- node3 [weight=5];
node3 -- node1 [weight=7];
```

#### Example Graph
```python
graph G = {
A -- B [weight=4];
A -- C [weight=2];
B -- C [weight=1];
B -- D [weight=5];
C -- D [weight=8];
}
```

---

### Controls

- **Enter Source and Target**: Select the source and target nodes to find the shortest path.
- **Visualization**: Observe the algorithm steps and the final shortest path highlighted.

---

### Code Files

1. **`main.py`**:
   - The entry point of the program. Links everything together.

2. **`graph.py`**:
   - Contains the `Graph` class for graph representation and Dijkstra's algorithm implementation.

3. **`visualization.py`**:
   - Includes `Node` and `Arrow` classes for rendering the graph and its elements and is the core rendering file.

---

### Example Output

1. **Full Graph View**:
   - Displays the entire graph with all nodes and edges.
   - Dimmed view as a background.

2. **Shortest Path View**:
   - Highlights the shortest path in the graph:
     - Nodes in **green**.
     - Edges in **red**.
   - Shows edge weights and node labels.

---

### Future Improvements

1. Support for:
   - Directed graphs.
   - Additional algorithms (e.g., A*, Bellman-Ford).
2. Interactive node and edge creation.
3. Enhanced step-by-step visualization.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Developed by Vojtěch Vlachovský as a part of the mandatory curriculum project.
