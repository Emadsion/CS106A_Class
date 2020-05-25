from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    karel_put_beepers()
    turn_right()
    karel_put_beepers()
    turn_right()
    karel_put_beepers()
    karl_moves()
#precondition:karel is standing at the beginning of the shape
#postcondition:Karel put beepers at three sides of the shape
def karel_put_beepers():
    for i in range(2):
        karl_moves()
        step()
    karl_moves()
#precondition:karel at the beginning of the side of the shape
#postconidtion:Karel puts beeper on a side of the shape
def karl_moves():
    while left_is_blocked():
        put_beeper()
        move()

#preconditionLkarel finished putting beeper at the end of the side of the shape
#postcondition:Karel at the beginning of the 2nd side of the shape
def step():
    turn_left()
    move()
#mkae karel turnning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()




if __name__ == "__main__":
    run_karel_program()
