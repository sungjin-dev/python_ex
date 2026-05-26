import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):    # setter  set + UNumbers
    global userNums     # 함수 내부에서 데이터를 입력하는 장치가 없기 때문에
    userNums = ns

def getUNumbers():      # getter   get + UNumbers
    return userNums

def setRNumbers():
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:   # count가 중복된 데이터를 찾는거니까 
            collect.append(item)
    
    return collect
