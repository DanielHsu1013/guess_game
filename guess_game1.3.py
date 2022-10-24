import random
start = input('please enter the start value:')
start = int(start)
end = input('please enter the end value:')
end = int(end)

x = random.randint(start,end)

c = 0

while True:
    c = c + 1
    y = input('Guess a number')
    y = int(y)
    if y == x:
        c = c + 1
        print('you got it! you have guess for', c - 1, 'times')
        break
    elif y >= x:
        print('guess lower. you have guess for', c, 'times')
    else:
        print('guess higher you have guess for', c, 'times')