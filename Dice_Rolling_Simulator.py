###DICE ROLLING SIMULATOR
#This Programm contains the code for a dice rolling simulator.
#The simulator will produce an integer number between 1 and x.
#x is choosen by the user.

#importing the function randint from the module random.
from random import randint

#The menue shown at the beginning.
#The input will return what the max. sides of the die will be (x)!
def menu():
    print "Welcome to the \"Dice Rolling Simulator\"!"
    print ""
    print "The Simulator will show a random number between 1 and x."
    print "You decide what number x is!"
    return input("What should x be? ")

#Variables for the randint function
num1 = 1
x = menu()

#all it needs to really roll the die.
def roll_die():
    print "The die shows the number: ", randint(num1, x)

#askink the user to press a key to roll the die.
def ask_roll():
    return input("To roll the die press 1: ")

#asking to press a key to roll it again.
def ask_roll_again():
    return input("If you want to roll the die again press 1 else press 0: ")

#first roll, press key
roll = ask_roll()
#Variable for the while-loop
loop = 1
#looping the code to have an easy chance at rolling the die again
while loop == 1:

    if roll == 1:
        roll_die()
    else:
        print "Ups! You pressed the wrong key!"
        print "Thank you for using the \"Dice Rolling Simulator\"!"
        break

    roll_again = ask_roll_again()
    if roll_again == 1:
        continue
    else:
        loop = loop -1
        print "Thank you for using the \"Dice Rolling Simulator\"!"
