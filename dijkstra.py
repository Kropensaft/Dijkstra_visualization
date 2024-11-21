import re  # Import the regular expression module to parse the DOT string
from heapq import heapify, heappop, heappush  # Import functions to work with a priority queue


class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to store the graph

    def add_edge(self, from_, to_, weight):
        # If the 'from_' node is not in the graph, add it with an empty dictionary
        if from_ not in self.graph:
            self.graph[from_] = {}
        # If the 'to_' node is not in the graph, add it with an empty dictionary
        if to_ not in self.graph:
            self.graph[to_] = {}
        # Add the edge between 'from_' and 'to_' with the specified 'weight'
        self.graph[from_][to_] = weight
        self.graph[to_][from_] = weight  # Since the graph is undirected, add the reverse edge too

    def from_dot_string(self, dot_string):
        # Define a regular expression to match the DOT format for edges with weights
        edge_pattern = re.compile(r'(\w+)\s*--\s*(\w+)\s*\[weight=(\d+(\.\d+)?)\];')
        # Loop through all matches of the regex in the DOT string
        for match in edge_pattern.finditer(dot_string):
            # Extract the 'from_node', 'to_node', and 'weight' from the match
            from_node, to_node, weight = match.group(1), match.group(2), float(match.group(3))
            # Add the edge to the graph
            self.add_edge(from_node, to_node, weight)

    def dijkstra(self, source: str, target: str):

        steps = []

        # Initialize the distances for all nodes as infinity
        distances = {node: float("inf") for node in self.graph}

        #set the 0th step as initialization
        steps.append(({node : float("inf") for node in self.graph}))
        distances[source] = 0  # Set the distance to the source node as 0


        #set the value of source node to 0
        steps.append({source : 0})

        priority_queue = [(0, source)]  # Initialize the priority queue with the source node
        heapify(priority_queue)  # Heapify the priority queue to make it a valid min-heap
        visited = set()  # Set to track visited nodes



       #implement a counter for each step / iteration
       #log the values of each node and whether it has been visited or not

        # While the priority queue is not empty
        while priority_queue:
            currentDist, currentNode = heappop(priority_queue)  # Pop the node with the smallest distance

            if currentNode in visited:
                continue  # Skip the node if it has already been visited
            visited.add(currentNode)  # Mark the node as visited

            # For each neighbor of the current node
            for neighbor, weight in self.graph[currentNode].items():
                # Calculate the temporary distance to the neighbor
                temporary_distance = currentDist + weight

                # If the new distance is shorter than the existing distance, update it
                if temporary_distance < distances[neighbor]:
                    # Update the distance for the neighbor
                    distances[neighbor] = temporary_distance

                    # Create a new snapshot for the current step
                    new_step = steps[-1].copy()  # Copy the previous step
                    new_step[neighbor] = temporary_distance  # Update the modified variable (neighbor's distance)
                    steps.append(new_step)  # Append the new step

                    # Push the neighbor into the priority queue with the updated distance
                    heappush(priority_queue, (temporary_distance, neighbor))

        # Initialize a dictionary to store the predecessors for each node
        predecessors = {node: None for node in self.graph}
        # For each node and its corresponding distance
        for node, distance in distances.items():
            # Check the neighbors of the node to find the predecessor
            for neighbor, weight in self.graph[node].items():
                # If the neighbor's distance equals the current node's distance plus the edge weight
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node  # Set the predecessor

        return distances, predecessors, steps   # Return both the distances and the predecessors

    def shortest_path(self, source: str, target: str):
        # Call dijkstra to get distances and predecessors from the source node
        _, predecessors, _ = self.dijkstra(source, target)
        path = []  # Initialize an empty list to store the path
        current_node = target  # Start from the target node

        # Backtrack from the target node using the predecessors dictionary
        while current_node:
            path.append(current_node)  # Add the current node to the path
            current_node = predecessors[current_node]  # Move to the predecessor node

        path.reverse()  # Reverse the path to get it from source to target
        return path  # Return the reversed path

