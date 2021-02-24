import random

name1 = input("What is your name? : ")

print("Welcome to the game "+name1)

chance1 = input(name1+ " Choose between rock, paper and scissors: ") 
chance2 = random.randint(1,3)
if chance2 == 1:
    chance2 = "rock"
elif chance2 == 2:
    chance2 = "paper"
else:
    chance2 = "scissors"


if chance1 == chance2:
    print(name1+ " ties with Computer" )
elif chance1 == "rock" and chance2== "paper":
    print("Computer chose paper, computer wins! "+name1+ "chose rock")
elif chance1 == "paper" and chance2== "rock":
    print(name1+ " wins! Computer chose rock" )
elif chance1 == "rock" and chance2== "scissors":
    print(name1+ " wins! Computer chose scissors")
elif chance1 == "scissors" and chance2== "rock":
    print("Computer chose rock, computer wins!" +name1+ " chooses scissors")
elif chance1 == "paper" and chance2== "scissors":
    print("Computer chose scissors, computer wins! " +name1+ " chooses paper")
elif chance1 == "scissors" and chance2== "paper":
    print(name1+ " wins! Computer chose paper")
else:
    print("Invalid Choice! Try again")

