import random
computer_num=random.randint(1,50)
print(computer_num)
n=0
chances=0
while chances!=3:
    user_num = int(input("Enter a number:"))
    if user_num<computer_num:
        chances=chances+1
        n=n+1
        if chances == 3:
            print("Your chances are over")
        else:
            print(f"Enter a Higher number and you {3-chances} chances")
    elif user_num>computer_num:
        n=n+1
        chances=chances+1
        if chances == 3:
            print("Your chances are over")
        else:
            print(f"Enter a lower number and you {3-chances} chances")
    else:
        print("The number guessed is correct")
        n=n+1
        chances=chances+1
        break
print(f"number of guessess:{n}")
