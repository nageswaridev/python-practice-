password = input("Enter Password: ")

upper = False
lower = False
digit = False

for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True

if len(password) >= 8 and upper and lower and digit:
    print("Strong Password")
else:
    print("Weak Password")
