import random

# I created this as a way to practice powers of 2 for a CS class

def powerof2():

    keep_going = True

    userRange = input("What range of powers of 2? ")
    userRange = int(userRange)

    while keep_going:
        for i in range(userRange):
            power = random.randint(0,10)
            ans = int(input("What is 2**" + str(power) + ": "))
            correct = 2**power
            if ans == correct:
                print("Correct!")
            else:
                print("Wrong!")
                print(str(correct))
        keep_going = input("Would you like to play again? (True or False)")
        userRange = input("What range of powers of 2? ")
        userRange = int(userRange)
        
powerof2()