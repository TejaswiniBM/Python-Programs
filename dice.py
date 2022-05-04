#Dice Game
import random
roll='y'
s1=0
s2=0
while 1:
  roll=input("Do you want to roll dice(y/n)?")
  if roll=='y' or roll=='Y':
    u1=random.randint(1,6)
    u2=random.randint(1,6)
    s1+=u1
    s2+=u2y
  else:
    print("Score of User1:",s1)
    print("Score of User2:",s2)
    if s1>s2:
      print("User1 is Winner!!")
    elif s2>s1:
      print("User2 is winner!!")
    else:
      print("Its Tie!!")
    break;
