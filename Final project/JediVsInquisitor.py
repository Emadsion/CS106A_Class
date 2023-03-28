"""
File name: Jedi Vs Inquisitor

it's a game like Angles & Devil game but in Star wars mode

We Want to transfer both the Jedis (J) and the inquisitors(I) to the other side without
being eliminated by the Inquisitors(I).
Rules: if the number of Inquisitors are more than the number of the jedi at either sides
the Inquisitors will eliminate the Jedis and the game will be lost. So you must find a way to transfer both Jedis
and Inquisitors without being eliminated.

Constrains: -You can't move an empty boat you need at least a person to sail it to the other edge
            -You can't add more than 2 persons inside the boat
            -You can't empty an already empty boat

Try to use the least number of boat moves
"""

# The space between the two edges of the land
SPACE = 50


def main():
    count = 0  # To count the number of boat moves
    current_edge = ['J', 'J', 'J', 'I', 'I', 'I']  # The beginning state as both the Inquisitors and Jedis
    far_edge = []
    boat = []
    # switch_boat variable is used for printing purposes
    # switch_boat == Ture --> boat at the left side *** switch_boat == False --> boat at the right side
    switch_boat = False
    print("\nPress 'J' for Jedi or press 'I' for inquisitor and 'R' to remove from the boat ")
    print("Press Enter to move the boat to the other side\n")

    while True:
        print_part(boat, current_edge, far_edge, switch_boat)
        won, count = execute(boat, current_edge, far_edge, switch_boat, count)
        if won == 'won':
            print("\n" + str(count) + " Moves")
            print("YOU DID IT, MAY THE FORCE BE WITH YOU")
            break
        if check_loss(current_edge, far_edge, boat):
            print_part(boat, far_edge, current_edge, not switch_boat)
            print("The Jedis are eliminated. You Lost The Game.")
            break

        current_edge, far_edge = switch_sides(current_edge, far_edge)
        switch_boat = not switch_boat  # Changing the boat position


# This function is responsible for executing all orders of the user The orders are: Move boat --> "Enter",
# Add Jedis (J) / Inquisitors (I) to boat --> 'I'/'J', Remove Jedis / Inquisitors from the boat --> 'R'
def execute(boat, current_edge, far_edge, switch_boat, count):
    while True:
        user_input = input()
        if user_input == 'I' or user_input == 'J':
            if user_input not in current_edge:
                print("There is no " + ("Inquisitors", "Jedis")[user_input == 'J'] + " here")
            else:
                add_to_boat(user_input, boat, current_edge)
                print_part(boat, current_edge, far_edge, switch_boat)

        elif user_input == 'R':
            remove_from_boat(boat, current_edge)
            print_part(boat, current_edge, far_edge, switch_boat)
            # Checking that all characters are transferred to the other edge
            # by checking boat moves (count) being an odd number
            # if boat moves (count) is an even number this will mean the character are still in the beginning side
            if win(current_edge) and count % 2 != 0:
                return 'won', count

        elif user_input == '':
            if len(boat) > 0:
                count += 1
                print(count)
                return True, count
            else:
                print("Cannot move an empty boat")


# Print the current state of right edge, left edge and boat
# Every time it checks if the boat is switched to either side
def print_part(boat, current_edge, far_edge, switch_boat):
    if not switch_boat:  # switch_boat == False --> the boat on the right side
        print(str(far_edge), str(boat) + str(current_edge), sep="_" * SPACE)
    else:  # switch_boat == True --> the boat at the left side
        print(str(current_edge) + str(boat), str(far_edge), sep="_" * SPACE)


# Add Jedis or Inquisitors to the boat
# Check that not more than two persons in the boat
def add_to_boat(user_input, boat, current_edge):
    if len(boat) == 2:
        print("You cannot add any more to the boat")
        print("Press Enter to move the boat or 'R' to remove someone from the boat")
    else:
        boat.append(user_input)
        current_edge.remove(user_input)


# Remove persons from the boat
# Check if the boat is empty and if all the Jedis and Inquisitors are transferred to the left side
def remove_from_boat(boat, current_edge):
    if len(boat) > 0:
        temp = boat.pop()
        current_edge.append(temp)

    else:
        print("\nBoat is already empty\n")


# Check the winning condition
def win(current_edge):
    if len(current_edge) == 6:
        return True


# For printing purposes only … exchanging the two edges info
def switch_sides(current_edge, far_edge):
    temp = current_edge
    current_edge = far_edge
    far_edge = temp
    return current_edge, far_edge


# Check losing condition: If number of Inquisitors is more than the number of Jedis at any of both edges
def check_loss(far_edge, current_edge, boat):
    current_check = {}
    far_check = {}
    current_check_loss = False
    far_check_loss = False

    # Checking the number of current edge characters
    for word in current_edge:
        if word not in current_check:
            current_check[word] = 1
        else:
            current_check[word] += 1

    # Checking the number of current edge characters
    for word in far_edge:
        if word not in far_check:
            far_check[word] = 1
        else:
            far_check[word] += 1

    # Checking the number of characters inside the boat and adding them to the current boat edge stop
    for word in boat:
        if word not in current_check:
            current_check[word] = 1
        else:
            current_check[word] += 1

    # Checking if the number of Inquisitors is more than the number of Jedis at both current edge and far edge
    if far_check.get('I', False) and far_check.get('J', False):
        far_check_loss = (far_check['I'] > far_check['J'])
    if current_check.get('I', False) and current_check.get('J', False):
        current_check_loss = (current_check['I'] > current_check['J'])

    # Return if condition of loss happens at both edges
    return far_check_loss or current_check_loss


if __name__ == '__main__':
    main()
