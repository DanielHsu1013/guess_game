import random
x = random.randint(1,100)

c = 0

while True:
    c = c + 1
    y = input('Guess a number form 1 to 100:')
    y = int(y)
    if y == x:
        c = c + 1
        print('you got it! you have guess for', c - 1, 'times')
        break
    elif y >= x:
        print('guess lower. you have guess for', c, 'times')
    else:
        print('guess higher you have guess for', c, 'times')