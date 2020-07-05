import sys
from crossword import *
from generate import *

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)

    print("Before:")
    for var in creator.domains:
        print(f"\t{var} : {creator.domains[var]}")

    creator.enforce_node_consistency()
    
    print("Before:")
    for var in creator.domains:
        print(f"\t{var} : {creator.domains[var]}")


if __name__ == "__main__":
    main()