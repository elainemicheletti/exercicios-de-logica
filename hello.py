## Basic Python Exercises - sys.argv
##
## propriedade sys,argv

import sys

# define main() function that prints a litter greeting

def main():

# get the name from the command line, using 'world' as a fallback

    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = "Alice"

    print('Hello', name)

# this is the standard boilerplate that calls the main() function

if __name__ == '__main__':
    main()