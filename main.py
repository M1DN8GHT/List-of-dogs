"""
Module Docstring: main.py
======================

This is the main module of the read/write to the file project.
"""

__author__ = "Manase Yaya"
__version__ = "0.1"
__date__ = "October 7, 2024"
__license__ = "None"

def read_file(file_name) -> None:
    """
    Reads a text file and prints it to the console.
    """    
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def write_file(file_name) -> None:
    """
    Writes a text file and prints it to the console.
    """
    with open(file_name, "w") as f:
        f.write("Pit Bull")
    
def main():
    """
    Main entry point of the application.
    """
    write_file("dogs.txt")

    pass

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()