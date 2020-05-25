"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    count=0

    while True:
        first_num=random.randint(10,99)
        second_num=random.randint(10,99)
        sum=first_num+second_num
        print("what is "+str(first_num)+" + "+str(second_num)+"?")
        answer=int(input("Your answer: "))
        if answer==sum:
            count+=1
            print("Correct!  You've gotten "+str(count)+" correct in a row.")
        else:
            count=0
            print("Incorrect.  The expected answer is "+str(sum)+" ")

        if count==3:
            print("Congratulations!  You mastered addition. ")
            break


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
