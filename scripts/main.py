from visualization import visualize
import os

def main():
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
             G -- G [weight=0]
           }
           """
    visualize(graph_DOT, "B", "F","B", "F")


if __name__ == '__main__':
    main()
