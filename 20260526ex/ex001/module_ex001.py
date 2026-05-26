# 가위 바위 보를 선택하세요
# 0.가위 1.바위 2. 보

# com 바위
# user 가위
# 컴퓨터 승리

import random

userChoice = []
ComNum = []
data = ['가위', '바위', '보']

def userRPSdata(rsp):
    global userChoice
    userChoice = rsp

def setRNumber():
    global ComNum
    ComNum = random.randrange(0,3)
    
def getRNumber():
     
    return data[ComNum]

def compareNumber():
    global userChoice
    global ComNum

    if data[ComNum] == userChoice[0]:
        return '무승부'

    if data[ComNum] == '가위':
        if userChoice[0] == '보':
            return '컴퓨터 승리!'
        if userChoice[0] == '바위':
            return '사용자 승리!'
        
    if data[ComNum] == '바위':
        if userChoice[0] == '가위':
            return '컴퓨터 승리!'
        if userChoice[0] == '보':
            return '사용자 승리!'
        
    if data[ComNum] == '보':
        if userChoice[0] == '가위':
            return '사용자 승리!'
        if userChoice[0] == '바위':
            return '컴퓨터 승리!'

            

    



