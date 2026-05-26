# quiz) 369 게임 만들기
'''
친구들까리 많이 하는 369게임을 만들어 봅시다. 
1부터 99까지 1씩 증가하면서 숫자에 3, 6, 9가 들어 있을 때마다 숫자와 함께 
'짝!'을 출력합니다

6 -> 짝!
33 -> 짝!짝!
99-> 짝!짝!
'''

# for num in range(1, 100):

#     if num <= 9:
#         if num == 3 or num == 6 or num == 9:
#             print('짝')
#         else:
#             print(num)
#     elif num >= 10:
#         if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:   
#             print('짝')
#             if num // 10 == 3 or num // 10 == 6 or num // 10 == 9:
#                 print('짝','짝')
#         elif  num // 10 == 3 or num // 10 == 6 or num // 10 == 9:
#             print('짝')
#         else:
#             print(num)

# for num in range(1, 100):

#     clap = ""

#     if num % 10 in [3, 6, 9]:
#         clap += "짝"
#     if num // 10 in [3, 6, 9]:
#         clap += "짝"

#     if clap == "":
#         print(num)
#     else:
#         print(clap)



# for num in range(1, 100):

#     if num <=9:                     # 1의 단위 
#         if num % 3 == 0:
#             print(f'{num}, 짝!')
#         else :
#             print(f'{num}')   
#     else:  
#         print('------------------------------')                         # 10의 단위
#         # print(f'{num}')             # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
#         printStr = str(num)
#         firstNum = num // 10        # 15 > 15 // 10 -> 1
#         secondNum = num % 10        # 15 > 15 % 10 -> 5   ,  30 > 0 

#         if firstNum % 3 == 0:
#             #print(f'짝!')
#             printStr += ', 짝!'
    

#         if secondNum % 3 == 0 and secondNum != 0 :
#            # print(f'짝!')
#             printStr += ', 짝!'
#         print('-------------------------------')

'''
for num in range(1, 100):

    if num <= 9:                # 1의 단위
        if num % 3 == 0:
            print(f'{num}, 짝!')
        else:
            print(f'{num}')
    else:                       # 10의 단위 
        # print(f'{num}')       # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
        printStr = str(num)
        firstNum = num // 10    # 15 > 15 // 10 -> 1
        secondNum = num % 10    # 15 > 15 % 10  -> 5, 30 > 0

        if firstNum % 3 == 0:
            # print(f'짝!')
            printStr += ', 짝!'

        if secondNum % 3 == 0 and secondNum != 0:
            # print(f'짝!')
            printStr += ', 짝!'
        
        print(f'{printStr}')
'''

# for num in range(1, 100):

#     if num <= 9:                # 1의 단위
#         if num % 3 == 0:        # 3의 배수
#             # print(f'{num}, 짝!')
#             print(num, ', 짝!', end='')
#         else:
#             print(num, end='')
#     else:                       # 10의 단위 
#         # print(f'{num}')       # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
#         # printStr = str(num)
#         print(num, end='')

#         firstNum = num // 10    # 15 > 15 // 10 -> 1
#         secondNum = num % 10    # 15 > 15 % 10  -> 5, 30 > 0

#         if firstNum % 3 == 0:
#             # print(f'짝!')
#             # printStr += ', 짝!'
#             print(', 짝!', end='')

#         if secondNum % 3 == 0 and secondNum != 0:              
#             # print(f'짝!')
#             # printStr += ', 짝!'
#             print(', 짝!', end='')
        
    # print()      

# for num in range(1 ,100):            #range list는 쉼표임
#     if num <= 9:
#         if num % 3 == 0:
#             print(f'{num}, 짝')
#         else:
#             print(num)
#     else:
#         firstNum = num // 10
#         secondNum = num % 10
#         printStr = str(num)      # num을 문자라고 상정하고 문자열을 계속 추가

#         if firstNum % 3 == 0:
#             printStr += ', 짝'
        
#         if secondNum % 3 == 0 and secondNum != 0: 
#             printStr += ', 짝'                  # 추가하는 개념으로 += 쓰이는구만

#         print(f'{printStr}')         #나중에 모아둔 문자열을 같이 출력




# quiz) 열차 교차 시간 알아내기 
'''
대전역에는 3개 노선의 열차가 오전 9시부터 오후 6시까지 교차 운행한다. 
3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막으세요.
(단 매일 오전 9시에 한빛역에서 모든 열차가 출발한다)
--------------------------------
A열차 : 첫차 오전 9시 | 마지막 차  오후 6시 | 운행 간격 10분 
B열차 : 첫차 오전 9시 | 마지막 차  오후 6시 | 운행 간격 25분
C열차 : 첫차 오전 9시 | 마지막 차  오후 6시 | 운행 간격 30분
-------------------------------
'''

# # 1분 단위  60*9 = 540분
#                             #최소공배수 느낌
# trianA = 10
# trianB = 25

# trianC = 30

# for n in range(1, 541):

#     if n % trianA == 0 and n % trianB == 0 and n % trianC == 0:
#         print('trainA <->trainB <->trainC')
#         # print(9 + n//60, end='') 
#         # print('시', end='')         
#         # print(n % 60, end='')  
#         # print('분')
#         print(f'{9+n//60}시 {'00' if n % 60 == 0 else str(n % 60)}분')   
#     elif n % trianA == 0 and n % trianB == 0: 
#         print('trainA <->trainB') 
#         # print(9 + n//60, end='') 
#         # print('시', end='')         # 시
#         # print(n % 60, end='')  
#         # print('분') 
#         print(f'{9+n//60}시 {n % 60}분') 
#     elif n % trianB == 0 and n % trianC == 0:
#         print('trainB <->trainC') 
#         # print(9 + n//60, end='') 
#         # print('시', end='')         
#         # print(n % 60, end='')  
#         # print('분')
#         print(f'{9+n//60}시 {n % 60}분')          
#     elif n % trianC == 0 and n % trianA == 0:
#         print('trainC <->trainA')   
#         # print(9 + n//60, end='') 
#         # print('시', end='')         
#         # print(n % 60, end='')  
#         # print('분')
#         print(f'{9+n//60}시 {n % 60}분')

'''      

rainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB <-> trainC')
        # print(9 + n // 60, end='')        # 시
        # print('시', end='')
        # print(n % 60, end='')             # 분
        # print('분')
        print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')
    elif n % trainA == 0 and n % trainB == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')        # 시
        # print('시', end='')
        # print(n % 60, end='')             # 분
        # print('분')
        print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')
    elif n % trainB == 0 and n % trainC == 0:
        print('trainB <-> trainC')
        # print(9 + n // 60, end='')        # 시
        # print('시', end='')
        # print(n % 60, end='')             # 분
        # print('분')
        print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')
    elif n % trainC == 0 and n % trainA == 0:
        print('trainC <-> trainA')
        # print(9 + n // 60, end='')        # 시
        # print('시', end='')
        # print(n % 60, end='')             # 분
        # print('분')
        print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')        
  '''    

# quiz) 로그인 기능 만들기

'''
시스템 관리자(administrator) 로그인 기능을 만들어 봅시다.
관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면 '암호를 다시 확인하세요!'를 출력하고
다시 암호를 물어봅니다. 
5회 이상 로그인에 실패하면 '로그인 실패!! 횟수 초과!!!' 메시지를 출력하고 종료합니다.
암호가 올바르다면 '로그인 됐습니다.'를 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다. 
'''

# ADMIN_PW = 'dwac1234'

# count = 1

# while True:

#     if count > 5:
#         print(f'로그인 실패!! 횟수 초과!!!')
#         break
#     userPw= input('암호 입력: ')

#     if  userPw == ADMIN_PW:
#         print(f'로그인 됐습니다.')
#         break

#     elif userPw != ADMIN_PW:
#         print(f'암호를 다시 확인하세요!')
        
        # count +=1 


                                                 # input 을 while문 안에 넣어서 활용 
# ADMIN_PW = 'dwac1234'        # 이렇게 비밀번호를 변수명을 해놔야 나중에 하나하나 바꿀필요가 없음 

# count = 1

# while True:

#     if count > 5:
#         print('로그인 실패!! 횟수 초과!!!')

#     inputPw = input('비밀번호 : ')               # 위치가 중요한게 만약 input을 위로 올리면 
                                                  #  6회도 가능한 경우가 생김
#     if inputPw != ADMIN_PW:
#         print(f'암호를 다시 확인하세요!')   
#         count += 1

#     elif inputPw == ADMIN_PW:
#         print(f'로그인 됐습니다.')
#         break
'''
while not False :       무한루프 됨
    print('hello')

while not 0:           무한루프 됨
    print('hello') 
'''
# 0 은 False 취급
# not 0 은 True 취급

# quiz) 팩토리얼 만들기
'''
사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만드시오>
팩토리얼(factorial, !) n!은 1부터 양의 정수 n까지의 모든 정수를 곱한 값을 말한다.
(예를 들어, 4!은 1x2x3x4 = 24이다.)
'''

# userInputIntegerData = int(input('양수 입력:'))
# result = 1
# for num in range(1, userInputIntegerData + 1):
#     result *= num
# print(f'{userInputIntegerData}의 팩토리얼은 {result}이다.')

# quiz) 숫자 맞추기 게임을 만들자

'''
0부터 100사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오. 
다음은 프로그램 개발에 필요한 요구사항이다.
--- 요구사항 ---
- 1부터 100까지의 난수를 발생시킨다.
- 사용자가 입력한 숫자가 난수와 일치하면 ‘정답입니다.’를 출력하고 게임을 종료한다.
- 사용자가 입력한 숫자가 난수와 일치하지 않으면 ‘틀렸습니다. 다시 입력하세요.’를 출력하고, 다시 물어본다.
- 기회는 10회로 제한한다. 만약 열 번을 넘어가면 ‘게임에 졌습니다.’를 출력하고 게임을 종료한다.
- 사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다. 
- 게임이 종료하기 전 난수를 출력한다. 
'''

# import random
# randomNum = random.randint(1, 100)

# count = 1

# while True:

#     if count > 10:
#         print('게임에서 졌습니다')
#         print(f' 정답 : {randomNum}')
#         break

#     userR = int(input('숫자를 입력하세요.'))        

#     if userR != randomNum :
#         print('틀렸습니다. 다시 입력하세요')
#         if userR > randomNum:
#             print('더 작습니다')
#         elif userR < randomNum:
#             print('더 큽니다')
#         count += 1                  

#     elif userR == randomNum :
#         print('정답입니다')
#         break
 
'''
import random
randomNum = random.randint(1, 100)

count = 1

while True:
    userR = int(input('숫자를 입력하세요.'))    #이런식으로 input 위치가 위에 있을 경우 11회도 가능
                                              count +=1 로 인해서 증가해서 바로 break가 걸리는게 아니라
                                             일단 input 숫자 입력으로 한번 더 칠 수 있게 됨. 
    if count > 10:
        print('게임에서 졌습니다')
        print(f' 정답 : {randomNum}')
        break      

    if userR != randomNum :
        print('틀렸습니다. 다시 입력하세요')
        if userR > randomNum:
            print('더 작습니다')
        elif userR < randomNum:
            print('더 큽니다')
        count += 1

    elif userR == randomNum :
        print('정답입니다')
        break'''

# quiz) 다음 요구조건을 참고하여 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램을 만드시오.

'''
 - 가로 길이는 1부터 2의 배수로 증가한다.     1,2,4,6,8,10
 - 세로 길이는 1부터 3의 배수로 증가한다.     1,3,6,9,12
 - 사각형의 넓이가 150 보다 크면 프로그램을 종료한다. 
 - 가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''

num = 1
width = 1
height = 1

minArea = width * height

maxArea = width * height
  
while True: 
    width = num * 2
    height = num * 3
    area = width * height 

    if area > 150:
        break

    if num == 1:       #하지만 실무에서는 "데이터의 첫 번째 항목을 초기값으로 잡는 방식"이 훨씬 더 안전하고 전문적인 코드로 평가받습니다!
        minArea = area
        maxArea = area

    else:
        if minArea > area:
            minArea = area 

        if maxArea < area:
            maxArea = area      

        print(f'area: {area}')
    
    num += 1

print(f'가장 작은 : {minArea}, 가장 큰 : {maxArea}')




# 주의점 : 변수 업데이트: 값을 저장할 때는 반드시 = (하나)를 쓰세요.
# 컴퓨터는 코드를 위에서 아래로 한 줄씩 읽습니다.

# 초기값

# width = 1
# height = 1

# # 가장 작은 사각형 넓이
#                                 # min이랑 max랑 따로 구분해서 변수명
# minArea = width * height

# maxArea = width * height

# while True:

#     area = width * height   # 사각형 넓이

#     if area > 150:
#         break

#     print(f'가로: {width}, 세로: {height}, 넓이: {area}')

#     if area < minArea:      # 최소 넓이              최소공배수 구할 때도 이런 방식으로!
#         minArea = area                     # 처음에 저장되고 끝

#     if area > maxArea:      # 최대 넓이 
#         maxArea = area                      # 계속 변함

#     if width == 1:          # width가 1인 경우
#         width = 2
#     else:                   # width가 1이 아닌 경우
#         width += 2
        
#     if height == 1:          # width가 1인 경우
#         height = 3
#     else:                   # width가 1이 아닌 경우
#         height += 3

# print(f'가장 작은 넓이: {minArea}')  
# print(f'가장 큰 넓이: {maxArea}')  


   






    

