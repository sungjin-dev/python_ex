'''
3명이 주사위를 5번씩 굴려서 나온 합을 구하는 프로그램을 만들어봅시다. 
합이 가장 큰 사람이 이기는 게임
'''

import random

class Dice:
    def __init__(self):
        self.numbers = []
    
    def playDice(self):
        self.numbers.append(random.randint(1,6))

    def getNumbers(self):
        return self.numbers
    
    def getSum(self):
        return sum(self.numbers)