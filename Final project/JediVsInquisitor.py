"""
File name: Jedi Vs Inquisitor
it's a game like Angles & Devil game but in Star wars mode

We Want to transfer both the Jedis (J) and the inquisitors(I) to the other side without
being eliminated by the Inquisitors(I).
the rules are: if the number of Inquisitors are more than the number of the jedi at either sides
the Inquisitors will eliminate the Jedis and the game will be lost.So find a way to transfer both Jedis
and Inquisitors without being eliminated.
Try to use the least number of boat moves
"""
SPACE = 50


def main():
    count = 0
    right_edge = ['J', 'J', 'J', 'I', 'I', 'I']
    left_edge = []
    boat = []
    switch_boat = False
    print("\nPress 'J' for Jedi or press 'I' for inquisitor and 'R' to remove from the boat ")
    print("Press Enter to move the boat to the other side\n")

    while True:
        won, count = execute(boat, right_edge, left_edge, switch_boat, count)
        if won == 'won':
            print("\n" + str(count) + " Moves")
            print("YOU DID IT, MAY THE FORCE BE WITH YOU")
            break
        if check(left_edge, right_edge, boat, switch_boat):
            print_part(boat, left_edge, right_edge, not switch_boat)
            print("The Jedis are eliminated. You Lost The Game.")
            break

        right_edge, left_edge = switch_sides(right_edge, left_edge)
        switch_boat = not switch_boat


# This function is responsible of executing all orders of the user
# The orders are: move the boat, Enter Jedis or Inquisitors to the boat and remove them from the boat
def execute(boat, right_edge, left_edge, switch_boat, count):
    print_part(boat, right_edge, left_edge, switch_boat)
    while True:
        x = input()
        if x == 'I' or x == 'J':
            add_to_boat(x, boat, right_edge, left_edge, switch_boat)

        elif x == 'R':
            won = remove_from_boat(boat, right_edge, left_edge, switch_boat, count)
            if won == 'won':
                return 'won', count

        elif x == '':
            if len(boat) > 0:
                count += 1
                print(count)
                return True, count
            else:
                print("Cannot move an empty boat")


# Print the current state of right edge, left edge and boat
# Every time it checks if the boat is switched to either side
def print_part(boat, right_edge, left_edge, switch_boat):
    if switch_boat:
        print(str(right_edge) + str(boat), str(left_edge), sep="_" * SPACE)
    else:
        print(str(left_edge), str(boat) + str(right_edge), sep="_" * SPACE)


# Add Jedis or Inquisitors to the boat
# Check that not more than two persons in the boat
def add_to_boat(x, boat, right_edge, left_edge, switch_boat):
    if len(boat) == 2:
        print("You cannot add any more to the boat")
        print("Press Enter to move the boat or 'R' to remove someone from the boat")
    else:
        boat.append(x)
        right_edge.remove(x)
        print_part(boat, right_edge, left_edge, switch_boat)


# Remove persons from the boat
# Check if the boat is empty and if all the Jedis and Inquisitors are transfered to the left side
def remove_from_boat(boat, right_edge, left_edge, switch_boat, count):
    if len(boat) > 0:
        temp = boat.pop()
        right_edge.append(temp)
        print_part(boat, right_edge, left_edge, switch_boat)
        if win(right_edge) and count % 2 != 0:
            return 'won'
    else:
        print("\nBoat is already empty\n")
        print_part(boat, right_edge, left_edge, switch_boat)


# Check the winning condition
def win(right_edge):
    count = 0
    for word in right_edge:
        count += 1
    # print("\n",count,'\n')
    if count == 6:
        return True


# Check losing condition: If number of Inquisitors is more than the number of Jedis at both riversides
def check(left_edge, right_edge, boat, switch_boat):
    r_check = {}
    l_check = {}
    left_check = False
    right_check = False

    if switch_boat:
        for word in boat:
            if word not in r_check:
                r_check[word] = 1
            else:
                r_check[word] += 1
    for word in right_edge:
        if word not in r_check:
            r_check[word] = 1
        else:
            r_check[word] += 1
    if not switch_boat:
        for word in boat:
            if word not in l_check:
                l_check[word] = 1
            else:
                l_check[word] += 1

    for word in left_edge:
        if word not in l_check:
            l_check[word] = 1
        else:
            l_check[word] += 1

    if l_check.get('I', False) and l_check.get('J', False):
        left_check = (l_check['I'] > l_check['J'])
    if r_check.get('I', False) and r_check.get('J', False):
        right_check = (r_check['I'] > r_check['J'])
    return left_check or right_check


def switch_sides(right_edge, left_edge):
    temp = right_edge
    right_edge = left_edge
    left_edge = temp
    return right_edge, left_edge


if __name__ == '__main__':
    main()
