import pygame
import math
from dijkstra import re
from dijkstra import Graph


# class which serves as a way to save "snapshots" of the current state
class State:
    # constructor with a list of nodes and arrows
    def __init__(self, nodes, arrows):
        self.nodes = nodes
        self.arrows = arrows


class Object:
    def __init__(self, x, y, name, type='node', color=None, text=None, textPos=None, font="Arial", radius=None,
                 center=None, weight=None, visited=False):
        self.visited = visited
        self.textPos_x, self.textPos_y = textPos if textPos else (x, y)
        self.radius = radius
        self.center_x, self.center_y = center if center else (x, y)
        self.type = type
        self.font = font
        self.text = text
        self.color = color
        self.name = name
        self.x = x
        self.y = y
        self.weight = weight  # Used for edge weights


class Arrow(Object):
    def __init__(self, start_node, end_node, weight, start_pos, end_pos, name=""):
        super().__init__(x=(start_pos[0] + end_pos[0]) / 2, y=(start_pos[1] + end_pos[1]) / 2, name=name, type='edge',
                         weight=weight)
        self.start_node = start_node
        self.end_node = end_node
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.arrow_size = 15  # Length of the arrowhead
        self.shaft_length = math.sqrt(
            (end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) - self.arrow_size

    def render(self, surface, font):
        # Calculate the angle between the nodes
        angle = math.atan2(self.end_pos[1] - self.start_pos[1], self.end_pos[0] - self.start_pos[0])

        # Calculate positions for arrow start and end
        arrow_start_x = self.start_pos[0] + 13 * math.cos(
            angle)  # Move 13 pixels (scaled node radius) outward from the center of start node
        arrow_start_y = self.start_pos[1] + 13 * math.sin(angle)
        arrow_end_x = self.end_pos[0] - 13 * math.cos(
            angle)  # Move 13 pixels (scaled node radius) inward from the center of end node
        arrow_end_y = self.end_pos[1] - 13 * math.sin(angle)

        # Draw the arrow shaft (line) from the adjusted start position to the adjusted end position
        pygame.draw.line(surface, (0xFFFFFF), (arrow_start_x, arrow_start_y), (arrow_end_x, arrow_end_y), 2)

        # Draw the arrowhead (triangle) pointing towards the end node
        arrow_x1 = arrow_end_x - self.arrow_size * math.cos(angle - math.pi / 6)
        arrow_y1 = arrow_end_y - self.arrow_size * math.sin(angle - math.pi / 6)
        arrow_x2 = arrow_end_x - self.arrow_size * math.cos(angle + math.pi / 6)
        arrow_y2 = arrow_end_y - self.arrow_size * math.sin(angle + math.pi / 6)

        pygame.draw.polygon(surface, (0xFFFFFF),
                            [(arrow_end_x, arrow_end_y), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)])

        # Render and rotate the text to match the angle of the arrow
        text = font.render(f"{self.weight}", False, 0xDDF2EB)

        # Position the rotated text at the end of the arrow
        mid_x, mid_y = (arrow_start_x + arrow_end_x) / 2, (arrow_start_y + arrow_end_y) / 2
        surface.blit(text,
                     ((mid_x + 5) - text.get_width() / 2, (mid_y + 5) - text.get_height() / 2))


class Button:
    def __init__(self, x, y, width, height, text, font, color, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.action = action

    def render(self, surface):
        # Draw the button
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Draw the text on the button
        text_surf = self.font.render(self.text, False, (0xFFFFFF))
        surface.blit(text_surf, (
            self.x + (self.width - text_surf.get_width()) / 2, self.y + (self.height - text_surf.get_height()) / 2))

    def is_clicked(self, pos):
        # Check if the button was clicked
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


# Function to reParse the DOT graph input in order to visualize the graph
def parseInput(input_string):
    edges = []
    # Regular expression to match lines in the format: A -- B [weight=3]
    pattern = r'(\w+)\s--\s(\w+)\s\[weight=([0-9.]+)\]'

    # Iterate through each line in the input string
    for match in re.finditer(pattern, input_string):
        nodeA = match.group(1)
        nodeB = match.group(2)
        edgeWeight = float(match.group(3))
        edges.append((nodeA, nodeB, edgeWeight))  # Store as a tuple

    return edges


def renderGraph(graph, surface, font, screen, distances, source_node):
    node_positions = {}
    nodes = set()
    edges = []

    # Function to assign positions in a circular layout
    def assign_positions(nodes, radius, center_x, center_y):
        angle_step = (2 * math.pi / len(nodes)) if nodes else 0
        for idx, node in enumerate(nodes):
            angle = idx * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            node_positions[node] = (x, y)

    # Determine the size of the circle (based on the number of nodes)
    radius = min(surface.get_width(), surface.get_height()) / 3
    center_x, center_y = surface.get_width() / 2.7, surface.get_height() / 2.4

    # Collect unique nodes and edges
    for A, B, weight in graph:
        nodes.add(A)
        nodes.add(B)
        edges.append((A, B, weight))

    # Assign positions for all nodes
    assign_positions(nodes, radius, center_x, center_y)

    # Create node objects
    node_objects = {
        node: Object(
            x=node_positions[node][0],
            y=node_positions[node][1],
            name=node,
            type='node',
            radius=13,
            font=font,
            text=str(distances.get(node, '\N{INFINITY}')),  # Use distances as text
            textPos=(node_positions[node][0] + 20, node_positions[node][1] - 10)  # Offset text for readability
        )
        for node in nodes
    }

    # Create edge (arrow) objects
    arrow_objects = [
        Arrow(
            start_node=nodeA,
            end_node=nodeB,
            weight=weight,
            start_pos=node_positions[nodeA],
            end_pos=node_positions[nodeB],
            name=f"{nodeA}-{nodeB}"
        )
        for nodeA, nodeB, weight in edges
    ]

    def renderNode(node_obj):
        x, y = node_obj.x, node_obj.y
        node_radius = node_obj.radius
        scaled_radius = int(node_radius * 1.3)  # Scale up by 30%
        pygame.draw.circle(surface, 0x88958d, (int(x), int(y)), scaled_radius)
        # Render node ID
        NodeID = font.render(f"{node_obj.name}", False, 0x606d5d)
        screen.blit(NodeID, (x - scaled_radius / 2.4, y - scaled_radius / 2.2))
        # Render text (distance or label)


    # Render all nodes and edges
    for node_obj in node_objects.values():
        renderNode(node_obj)
    for arrow_obj in arrow_objects:
        arrow_obj.render(surface, font)


    return node_objects, arrow_objects


def render_table(distances, nodes, surface, font, screen, table_background_color, table_border_color):
    # Define margins for spacing within the table
    margin = 1
    num_rows = len(nodes)
    num_cols = 2  # One column for node name and one for its distance or value
    cell_width = screen.get_width() // 20  # Adjust the width of the table
    cell_height = screen.get_height() // (num_rows + 1)  # Adjust the height based on the number of nodes

    # Define position to place the table in the upper-right corner
    table_x = screen.get_width() - (cell_width * num_cols) - margin  # Right-aligned
    table_y = margin  # Top-aligned

    # Loop through each node and draw the table cells
    row = 0  # Row index to go through each node
    for node_name, node_obj in nodes.items():
        for col in range(num_cols):
            x = table_x + col * cell_width
            y = table_y + row * cell_height

            # Draw the cell background (white)
            pygame.draw.rect(surface, table_background_color,
                             (x + margin, y + margin, cell_width - 2 * margin, cell_height - 2 * margin))
            # Draw the cell border (black)
            pygame.draw.rect(surface, table_border_color,
                             (x + margin, y + margin, cell_width - 2 * margin, cell_height - 2 * margin), 2)

            # Render the node name in the first column
            if col == 0:
                value = node_name  # Use the node name
            else:
                # Use the distance or '∞' if the distance is not available
                value = f"{distances.get(node_name, '\N{INFINITY}')}"

            # Render the value in the cell
            text = font.render(value, False, (0, 0, 0))  # Black color for text
            text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
            surface.blit(text, text_rect)

        row += 1  # Move to the next row


def visualize(graph, source_node, target_node):
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    _clock = pygame.time.Clock()

    title = "Visualization of Dijkstra's algorithm"
    pygame.display.set_caption(title)

    data = parseInput(graph)
    font = pygame.font.SysFont("Arial", 14, italic=True)

    # Initialize the graph and add edges
    g = Graph()
    for nodeA, nodeB, weight in data:
        g.add_edge(nodeA, nodeB, weight)

    # Get distances using the Dijkstra algorithm
    distances, _, steps = g.dijkstra(source_node, target_node)

    # Create a button at the bottom
    button_font = font
    # Create a button at the bottom of the screen
    buttonPrev = Button(x=50, y=screen.get_height()-50, width=100, height=40, text="Previous Step", font=font, color=(0, 8, 8))
    buttonNext = Button(x=screen.get_width() - 150, y=screen.get_height()-50, width=100, height=40, text="Next Step", font=font,
                        color=(0, 8, 8))

    # Snapshot management
    snapshots = []
    current_snapshot_index = 0

    # Function to take a snapshot of the current graph state
    def take_snapshot(nodes, arrows):
        state = State(nodes=list(nodes.values()), arrows=arrows[:])
        snapshots.append(state)

    # Function to render a snapshot
    def render_snapshot(index):
        if 0 <= index < len(snapshots):
            state = snapshots[index]
            screen.fill(0x606d5d)  # Clear screen

            # Render all nodes in the snapshot
            for node in state.nodes:
                # Render node using its properties
                pygame.draw.circle(screen, node.color or 0x88958d, (int(node.x), int(node.y)), int(node.radius * 1.3))
                NodeID = font.render(f"{node.name}", False, 0xDDF2EB)
                screen.blit(NodeID, (node.x - node.radius / 2.4, node.y - node.radius / 2.2))

            # Render all arrows in the snapshot
            for arrow in state.arrows:
                arrow.render(screen, font)

            pygame.display.update()

    # Event loop for visualization
    while True:
        screen.fill(0x606d5d)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonPrev.is_clicked(event.pos) and current_snapshot_index > 0:
                    current_snapshot_index -= 1
                    render_snapshot(current_snapshot_index)
                    print("previous button clicked")
                if buttonNext.is_clicked(event.pos) and current_snapshot_index < len(snapshots) - 1:
                    current_snapshot_index += 1
                    render_snapshot(current_snapshot_index)
                    print("next button clicked")



        # Render the graph and capture state at initialization
        nodes, arrows = renderGraph(data, screen, font, screen, distances, source_node)

        #render table of nodes and its values :
        render_table(distances, nodes, screen, font, screen, 0xDDF2EB, 0x606d5d)

        take_snapshot(nodes, arrows)  # Save the current state
        currentIndexSurface = font.render("current step: " + str(current_snapshot_index), False, 0xDDF2EB)
        screen.blit(currentIndexSurface, (screen.get_width() / 2 - buttonPrev.width / 2, buttonPrev.y))
        # Render the buttons
        buttonPrev.render(screen)
        buttonNext.render(screen)

        pygame.display.flip()
        pygame.display.update()
        _clock.tick(60)
