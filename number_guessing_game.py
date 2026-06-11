import random
secret_num=random.randint(1,10)
while True:
  guess=int(input("enter a number(1-10):"))
  if guess<secret_num:
    print("Too low")
  elif guess>secret_number:
    print("Too high")
  else:
    print("your guess is correct!")
    break
    
  
