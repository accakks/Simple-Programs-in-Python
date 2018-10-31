# Simulate (or actually play) Guess the Number
#   The number lies in a given range. Choose the number in the middle.
#   If guess was too high, choose number in middle of lower half,
#   if guess was too low,  choose number in middle of upper half.
#   Halve the appropriate range & repeat unti the number is correct.
#   Authour: Alan Richmond, Python3.codes

binary = False  # set this to True or False
lonum, hinum = 1, 128  # range for the number

import random as r

the_num = r.randint(lonum, hinum)  # computer chooses a number randomly
print("I'm thinking of a number between", lonum, "and", hinum)

lo = 1
hi = hinum
guesses = 0

for i in range(lonum, hinum):  # repeat this until guess is correct:
    # note the int!
    #    guess=int(input ("What is your guess: ")) # uncomment to actually play
    if binary:
        guess = lo + (hi - lo) // 2  # integer division
    else:
        guess = r.randint(lo, hi)
    print("Guess:", guess)
    guesses += 1  # add 1 to count of guesses
    # check the guessed number
    if guess > the_num:
        print("Lower!")
        hi = guess  # bring down the upper bound
    elif guess < the_num:
        print("Higher!")
        lo = guess  # push up the lower bound
    else:
        break  # yay!

print("That took", guesses, "guesses")
# print("That took {0} guesses".format(guesses)) # alternative to previous line
