#!/bin/python3

from random import randint
player=input("choose rock(R),paper(P),scissor(S):")
print(player,'vs')
choosen=randint(1,3)
print(choosen)
if choosen==1:
  computer='R'
elif choosen==2:
  computer="P"
else:
  computer="S"
  
print(computer)
if player==computer:
  print "DRAW"
elif player=="R" and computer=="S":
  print "PLAYER WINS"
elif player=="R" and computer=="P":
  print "Computer Wins"
elif player=="P" and computer=="R":
  print "Player Wins"
elif player=="P" and computer=="S":
  print "Computer Wins"
