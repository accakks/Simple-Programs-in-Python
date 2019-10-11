import random

options = ['rock', 'paper', 'scissor']



again='Y'

while(again.upper()=='Y'):
	user=0
	comp=0

	while(user<3 and comp<3):
		print("Enter a response")

		x = random.choice(options)
		choice = input()

		print("You chose " + choice.upper())
		print("The computer chose " + x.upper())


		if(x.upper()==choice.upper()):
			print("Please Try again")

		elif(x.upper()=="ROCK" and choice.upper()=="SCISSOR"):
			comp+=1

		elif(x.upper()=="ROCK" and choice.upper()=="PAPER"):
			user+=1

		elif(x.upper()=="PAPER" and choice.upper()=="ROCK"):
			comp+=1

		elif(x.upper()=="PAPER" and choice.upper()=="SCISSOR"):
			user+=1

		elif(x.upper()=="SCISSOR" and choice.upper()=="ROCK"):
			user+=1

		elif(x.upper()=="SCISSOR" and choice.upper()=="PAPER"):
			comp+=1

	

		print("user: ",user)
		print("computer: ",comp)

	again = input("Play again?(Y/N)")


