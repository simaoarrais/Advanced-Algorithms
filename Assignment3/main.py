"""
Created by: Simão Teles Arrais - 85132

Main python code for the Advanced Algorithms class Assigment 3.

The code was tested on python version 3.8.10.
"""
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Distinct Word Counting Program')

    # Command line arguments
    parser.add_argument('-d', '--books_dir', metavar='BOOKS_DIRECTORY', default='books', type=str, required=False,
                        help='path where the books are stored -> default: /%(default)s/')
    
    parser.add_argument('-s', '--stopw_dir', metavar='STOPWORDS_DIRECTORY', default='stopw', type=str, required=False,
                        help='path where the stop words are stored -> default: /%(default)s/')

    # Parse the command-line arguments
    args = parser.parse_args()
    books_dir = args.books_dir
    stopw_dir = args.stopw_dir

    # Check if directories are valid
    if not os.path.isdir(books_dir):
        raise parser.error("The given directory for the books is invalid!")
    
    elif not os.path.isdir(stopw_dir):
        raise parser.error("The given directory for the stop words is invalid!")


if __name__ == "__main__":
    main()
