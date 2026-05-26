# 가위 바위 보를 선택하세요
# 0.가위 1.바위 2. 보

# com 바위
# user 가위
# 컴퓨터 승리

import random

userChoice = []
ComNum = []
data = ['가위', '바위', '보']

def userRSPdata(ns):
    global userChoice
    userChoice = ns

def setRNumbers():
    global ComNums
    ComNums = random.randrange(0,3)
    return data[ComNums]

def compareNumbers():
    global userChoice
    global ComNums

    if data[ComNums] == userChoice[0]:
        return '무승부'

    if data[ComNums] == '가위':
        if userChoice[0] == '보':
            return '컴퓨터 승리!'
        if userChoice[0] == '바위':
            return '사용자 승리!'
        
    if data[ComNums] == '바위':
        if userChoice[0] == '가위':
            return '컴퓨터 승리!'
        if userChoice[0] == '보':
            return '사용자 승리!'
        
    if data[ComNums] == '보':
        if userChoice[0] == '가위':
            return '사용자 승리!'
        if userChoice[0] == '바위':
            return '컴퓨터 승리!'

            

    



