from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
#precondition:Karel is at the start of the world
#postcondition:Karel bulids each column to the end
    while front_is_clear():
        bulid()
        next_column()
    bulid()
#precondition:Karel is at the desired column facing north
#postcondition:Karel build the column and return to the ground
def bulid():
    filling_column()
    go_back()
#precondition:Karel is at the desired column facing north
#postcondition:Karel puts the beepers in each block of the column to the end
def filling_column():
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if no_beepers_present():
        put_beeper()
    turn_around()
#precondition:Karek has finished puting the beepers and facing south
#postconditio:Karel returned to the ground
def go_back():
    while front_is_clear():
        move()
    turn_left()
#precondition:Karel is at ground facing east
#postcondition:Karel moves to the next desired column
def next_column():
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()






# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
