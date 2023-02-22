
import random

class Play:
    def __init__(self):
        print('要開始喽~')

    def guess_game(self):
        x = random.randint(1,100)
        c = 0

        while True:
            c = c + 1
            y = input('0到100，請猜一個數字~')
            y = int(y)
            if y == x:
                c = c + 1
                print('答對了~你一共猜了', c - 1, '次')
                break
            elif y >= x:
                print('再低一點~. 你已經猜了', c, '次')
            else:
                print('再高一點~. 你已經猜了', c, '次')


aws = input('想玩猜數字遊戲嗎?')
if aws == ('好啊'):
    game = Play() # create an instance of the Play class
    game.guess_game() # call the guess_game method on the instance