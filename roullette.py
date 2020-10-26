#!/bin/python3
import random
import os


class myParam:
    def __init__(self, rangeWhile, token):
        self.rangeWhile = rangeWhile
        self.token = token


class Bet:
    def __init__(self, typeBet, tokenBet, num):
        self.typeBet = typeBet
        self.tokenBet = tokenBet
        self.num = num


betList = []
param = myParam(36, 50)

while True:
    os.system('clear')
    for bet in betList:
        #print(f"you put {bet.tokenBet} chips on the number")
        print("you put", bet.tokenBet, "chips on the number",
              bet.num, "in a", bet.typeBet)
    #print(f"\nYou have {param.token} tokens") --> pas besoin de faire str(param.token)
    print('\nYou have', str(param.token), 'tokens\n')
    if param.token > 0:
        print('press 1 for play single number')
        print('press 2 for play single col')
        print('press 3 for play single tier')
    if betList:
        print('press 4 for drop the ball\n')

    playerChoise = int(input())

    if playerChoise == 1 and param.token > 0:
        simple = int(input('Choose a number beetwen 1 and 36\n'))
        tokenbet = int(input('how much tokens do you want to bet\n'))
        # 0 >= simple < 37
        if simple <= 0 or simple > 36 or (param.token - tokenbet) < 0:
            print('error')
            continue
        param.token = param.token - tokenbet
        betList.append(Bet("simple bet", tokenbet, simple))
    elif playerChoise == 2 and param.token > 0:
        cols = int(input('Choose a cols 1, 2 or 3\n')) - 1
        tokenbet = int(input('how much tokens do you want to bet\n'))
        # 0 > cols < 3
        if cols < 0 or cols > 2 or (param.token - tokenbet) < 0:
            print('error')
            continue
        param.token = param.token - tokenbet
        betList.append(Bet("cols bet", tokenbet, cols))
    elif playerChoise == 3 and param.token > 0:
        tiers = int(input('Choose a tiers 1, 2 or 3\n')) - 1
        tokenbet = int(input('how much tokens do you want to bet\n'))
        #meme logique qu'au dessus
        if tiers < 0 or tiers > 2 or (param.token - tokenbet) < 0:
            print('error')
            continue
        param.token = param.token - tokenbet
        betList.append(Bet("tiers bet", tokenbet, tiers))
    else:
        b = random.randint(0, param.rangeWhile)
        c = int((b - 1) / 12)
        d = int((b - 1) % 3)
        print('The number is !!!!!!!!!!!!! ', str(b))
        for bet in betList:
            if bet.typeBet == "simple bet":
                if bet.num == b:
                    #f string comme au dessus
                    print("you win", bet.tokenBet * 36, "chips on the number",
                          bet.num, "in a", bet.typeBet)
                    param.token = param.token + bet.tokenBet * 36
                else:
                    #f string comme au dessus
                    print("you lose", bet.tokenBet, "chips on the number",
                          bet.num, "in a", bet.typeBet)
            if bet.typeBet == "cols bet":
                if bet.num == d:
                    #f string comme au dessus
                    print("you win", bet.tokenBet * 2, "chips on the number",
                          bet.num, "in a", bet.typeBet)
                    param.token = param.token + bet.tokenBet * 2
                else:
                    #f string comme au dessus
                    print("you lose", bet.tokenBet, "chips on the number",
                          bet.num, "in a", bet.typeBet)
            if bet.typeBet == "tiers bet":
                if bet.num == c:
                    #f string comme au dessus
                    print("you win", bet.tokenBet * 2, "chips on the number",
                          bet.num, "in a", bet.typeBet)
                    param.token = param.token + bet.tokenBet * 2
                else:
                    #f string comme au dessus
                    print("you lose", bet.tokenBet, "chips on the number",
                          bet.num, "in a", bet.typeBet)
        input()
