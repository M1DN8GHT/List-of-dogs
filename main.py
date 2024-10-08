"""
Module Docstring: main.py
======================

This is the main module of the read/write to the text file project.
"""

__author__ = "Manase Yaya"
__version__ = "0.1"
__date__ = "October 8, 2024"
__license__ = "None"

def read_file(file_name) -> None:
    """
    Reads a text file and prints it to the console.
    """    
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def new_file(file_name) -> None:
    """
    Creates a new text file and writes data to it, Or overwrites an existing file.
    """
    with open(file_name, "w") as f:
        f.write("Maine Coon")
    
def append_file(file_name, data) -> None:
    """
    Appends data to an existing text file.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "a") as f:
        if lines and lines[-1].strip()
        if lines and last_line !="":
            f.write("\n")
        f.write(data)  
def main():
    """
    Main entry point of the application.
    """
    append_file("cats.txt", "Burmese")

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()

