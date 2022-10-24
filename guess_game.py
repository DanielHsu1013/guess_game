import random
x = random.randint(1,100)

while True:
    y = input('Let us play a game. Guess a number form 1 to 100:')
    y = int(y)
    if y == x:
        print('you got it!')
        break
    elif y >= x:
        print('guess lower')
    else:
        print('guess higher')