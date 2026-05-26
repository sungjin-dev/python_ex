#데이터 입력(input data)
#input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''


'''
print('정수를 입력하세요.')
inputInteger = input()         #6
print(inputInteger)            #6  
print(type(inputInteger))      #int
'''

'''
print('실수를 입력하세요.')
inputFloat = input()
print(inputFlaot) 
print(type(inputFlaot))
'''

'''
print('논리형 데이터 입력하세요.')
inputBoolean = input()       #True
'''

'''
inputBoolean = input('논리형 데이터 입력하세요.\n')
print(inputBoolean)          #True 
print(type(inputBoolean))    #str
'''
                     

#\n (줄바꿈(개행) 원하는 횟수만큼 중복입력하면 됨. ()

#자료(data)형을 변환해야 합니다.  data type casting
'''
userInputData =input('사용자야~~~ 정수 입력해라~')    #10
print(userInputData)                               #10
print(type(userInputData))                         #str
userInputData = int(userInputData)                 #str --> int   재할당을 통해서 덮어쓰기함
print(type(userInputData))                         #int
'''

#str -> boolean
# userInputData = input('True or False 입력하세요.')
# print(userInputData)                               #True
# print(type(userInputData))                         #str
# userInputData = bool(userInputData)
# print(type(userInputData))


#str -> flaot

# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = float(userInputData)
# print(type(userInputData))

# userInputData = 'True'
# userInputData = bool(userInputData)
# print(type(userInputData))

# x = 3
# y = float(x)
# print(y)                 #정수를 실수화 

# x = 3.141592
# y = int(x)
# print(y)                  #실수를 정수화 
# print(float(y))           #데이터 날아감

