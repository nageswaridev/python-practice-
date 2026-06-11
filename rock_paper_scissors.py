import random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
user=input("enter rock,paper, or scissor:").lower()
if user==computer:
  print("it's a tie")
elif user=="rock" and computer=="scissors" or user=="paper" and computer=="rock" or user=="scissors" and computer=="paper":
  print("you win!")
else:
  print("computer win!")
print("computer chose:",computer)
           
           
