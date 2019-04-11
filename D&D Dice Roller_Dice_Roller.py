"""
Dice roller simulates dice rolls for dices used in Dungeons & Dragons.
Dice with 4, 6, 8, 10, 12, 20 and 100 sides can be simulated.
Displays individual rolls as well as the result, including modifier, if any.
"""

from random import randint
from time import sleep


def dice_roll():
    dice_type = int(input("Enter 4 for d4\nEnter 6 for d6\nEnter 8 for d8\nEnter 10 for d10\n"
                          "Enter 12 for d12\nEnter 20 for d20\nEnter 100 for d100\nChoose a die to throw: "))
    number_of_dice = int(input("Choose how many dice to throw: "))
    modifier = int(input("Add a modifier if applicable: "))
    sleep(1)
    print("Rolling dice...")
    sleep(1)
    total_roll = 0
    for i in range(1, number_of_dice+1):
        roll = randint(1, dice_type) + modifier
        sleep(1)
        print(roll, end=' ')
        total_roll += roll
    print("\nResult: {}, +{}".format(total_roll, modifier))
    sleep(1)
    print("Exiting...")
    return


dice_roll()
