"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():

    number=int(input("enter the number: "))
    count=check_number(number)
    print("The process took "+str(count)+" steps to reach 1")

def check_number(n):
    count=0
    while n != 1:
        if n % 2 == 0:
            temp = n // 2
            print(str(n) + " is even, so I take half: " + str(temp))
            count += 1

        else:
            temp = 3 * n + 1
            print(str(n) + " is odd, so I make 3n + 1: " + str(temp))
            count += 1

        n = temp
    return count





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
