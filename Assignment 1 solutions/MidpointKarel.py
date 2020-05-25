from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    blue_in_corners()
    all_blue()
    beeper()
    go_to_corner()
    remove_colors()
    goto_midpoint()

#Precondition:Karel is facing west
#Postcondition:Karel paint the corners blue
def blue_in_corners():
    paint_corner(BLUE)
    while front_is_clear():
        move()
    paint_corner(BLUE)
    turn_around()
#karel moves to each two horizental corners and paint the red block before the blue corner untill it reaches midpoint
def all_blue():
    if front_is_clear():
        move()
    while corner_color_is(BLANK):
        move()
        if corner_color_is(BLUE):
          paint_blue()
    turn_around()
#Precondition:Karel is standing on blue corner
#Postcondition:Karel paint the block before the blue corner blue
def paint_blue():
    turn_around()
    move()
    paint_corner(BLUE)
    move()
#precondition:Karel is on the block before midpoint
#postcondition:Karel moves to midpoint and put the beeper
def beeper():
    if front_is_clear():
        move()
    put_beeper()
#karel goes to the corner and face the clear side
def go_to_corner():
    while front_is_clear():
        move()
    turn_around()
#precondition:Karel in the corner facing the clear side
#postcondition:Karel is removing all the paint
def remove_colors():
    while front_is_clear():
        paint_corner(BLANK)
        move()
    paint_corner(BLANK)
    turn_around()
#karl goes to the midpoint
def goto_midpoint():
    while no_beepers_present():
        move()


def turn_around():
    turn_left()
    turn_left()
    # Yay I did it ^^



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
