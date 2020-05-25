"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    origin = 20
    player1 = 1
    player2 = 2
    while origin > 0:
        print("There are {} stones left".format(origin))
        choice=int(input("Player {} would you like to remove 1 or 2 stones? ".format(player1)))
        print()
        if choice ==1 or choice==2:
            origin -= choice
            #swaping players
            temp = player1
            player1 = player2
            player2 = temp
        else:
         print("Invalid option, Please try again")
            

    print("Player {} wins!".format(player1))





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
