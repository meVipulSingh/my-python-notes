
# Rock, Paper, Scissors

import random


def gamewin(comp, you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("comp turn: Rock(r), Paper(p), Scissors(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("your turn: Rock(r), Paper(p), Scissors(s)? ")
a = gamewin(comp, you)

print(f"Computer Chose >>> {comp}")
print(f"You Chose >>> {you}")

if a == None:

    print("*****THE GAME IS TIE*****")
elif a:

    print("*****YOU WIN*****")
else:

    print("*****YOU LOSE*****")
