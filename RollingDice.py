import random

again = True

while again:
    print(random.randint(1,6))
    roll = input("Want to roll dice (Y/N):")
    if roll.lower() == 'y':
        continue
    else:
        break


