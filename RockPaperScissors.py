#!/bin/python3

from random import randint

def rps():
    playerCh = input('Choose rock, paper or scissors')
    print('You chose '+playerCh)

    computerCh = randint(1,3)

    if computerCh == 1:
        computerCh = 'rock'
        print('Computer chose '+ computerCh )
    elif computerCh == 2:
        computerCh = 'paper'
        print('Computer chose '+ computerCh )
    else:
        computerCh = 'scissors'
        print('Computer chose '+ computerCh )
    return(computerCh, playerCh)

c, p = rps()

if c == p: 
  print('Tie')
elif c == 'rock' and p == 'paper':
  print('Player Wins')
elif c == 'rock' and p == 'scissors':
  print('Computer Wins')
elif c == 'paper' and p == 'rock':
  print('Computer Wins')
elif c == 'paper' and p == 'scissors':
  print('Player Wins')
elif c == 'scissors' and p == 'rock':
  print('Player Wins')
elif c == 'scissors' and p == 'paper':
  print('Computer Wins')
  

  
  

  



  



