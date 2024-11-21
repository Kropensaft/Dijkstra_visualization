from visualization import visualize
import os


def main():

    from_file = int(input("read from file? "))

    if from_file:
        # Define the graph file path
        file = input("select your input file: ")
        file_path = f"input_files/{file}"
        source = input("select your source node: ").upper()
        target = input("select your target node: ").upper()
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return

        # Open and read the graph definition
        try:
            with open(file_path, "r") as graph_file:
                graph_DOT = graph_file.read()

            # Call the visualization function
            visualize(graph_DOT, f"{source}", f"{target}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else :
        graph_DOT = """
           graph G {
             A -- B [weight=3];
             B -- D [weight=3.5];
             B -- E [weight=2.8];
             C -- A [weight=3];
             C -- E [weight=2.8];
             C -- F [weight=3.5];
             D -- C [weight=9];
             D -- G [weight=10];
             E -- G [weight=7];
             F -- G [weight=2.5];
           }
           """
        visualize(graph_DOT,"B", "F")
if __name__ == '__main__':
    main()
