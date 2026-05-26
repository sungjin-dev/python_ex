# 함수(function)
# python에서는 함수가 꽃이다!

# 믹서기에 사과를 넣으면 사과주스가 되고, 오렌지를 넣으면 오렌지주스가 되듯이 
# 사용자는 함수에 값만 집어넣으면 원하는 결과를 얻을 수 있습니다. 

# 함수의 종류 : 내장 함수 vs 사용자 함수

# 내장 함수 : print() , len() 등등...


# 코드(기능) 재사용 > 함수
# 데이터 재사용 > 변수


# 함수 정의하기

'''
사용자 함수를 만든다는 것은 '함수를 정의한다.'라고 합니다. 
함수를 정의할 때 def키워드를 사용합니다. 그리고 함수명은 콜론(:), 실행부를 이용합니다.  

num = 10
def 함수명(): 
    실행부(함수 기능)
'''

def greet(): 
    print('안녕하세요.')
    print('반갑습니다.')
    print('저는 홍길동입니다.')

'''
함수명 규칙
1. 내장함수명과 동일하면 안 된다. 
2. 첫 글자는 주로 소문자로 시작한다. 
3. 첫 글자는 숫자로 시작할 수 없다.  1greet():x  g1reet():o , greet1(): o
4. 특수문자는 사용할 수 없지만 언더바(_)는 사용 가능하다. 
5. 두개 이상의 단어가 조합되는 경우 스네이크 또는 카멜표기법을 사용하자. 
    sendMessage():    calculateDistance(): 
'''

# quiz) 온도센서 작동 시스템 만들기
# 온도센서 작동을 시작하고 멈추는 함수를 정의해봅시다.
# 함수명은 함수의 기능을 이해하기 좋도록 짓습니다. 

# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다.')

# def stopTemperatureSensor():
#     print('온도센서 작동을 중지합니다.')

#  함수 호출     호출할 때는 : 안 붙음  : 이건 선언임
# startTemperatureSensor()
# stopTemperatureSensor()

# quiz) 내 노트북은 몇 인치일까?


'''
고등학교 졸업 기념으로 노트북을 하나 장만했습니다. 
노트북 사이즈에 꼭 맞는 파우치를 하나 구매하려고 하는데 사이즈 표에 인치로만 표시
되어있습니다. 
cm를 인치로 바꿔주는 함수를 만들어봅시다. 
(1inch = 0.393701cm)
'''

def convertUnit():
    lengthCM = float(input('길이(cm) 입력:'))
    print(f'인치: {lengthCM * 0.393701}inch')  # 한번도 사용 안 할거면 메모리만 잡아먹음

# convertUnit()
# convertUnit()
# convertUnit()

# quiz) 이동 거리를 계산하는 함수
'''
길동이는 5시간 동안 3km/h의 속도로 등산을 했습니다.
길동이가 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는
프로그램을 함수를 이용하여 만들어봅시다.
'''

# def calculateDistance(): 
#     print(f'이동거리: {hourData * speedData}')

# hourData = float(input('이동 시간:'))          # for while 과 달리 안 밖 모두 가능함  전역변수임
# speedData = float(input('이동 속도:'))

# calculateDistance() 

"파이썬 함수는 자기 방에 찾는 물건이 없으면, 거실(밖)로 나가서 찾아온다."

"함수 밖에서 선언한 변수는 함수 안에서 그대로 읽을 수 있다! "
"다만, 더 좋은 함수를 만들려면 함수에 직접 데이터를 던져주는 방식(매개변수)을 쓰는 것이 확장성이 좋다."

# pass 키워드
# def calculateDistance():
#     pass

#  중첩 함수
# def fun1():
#     print('fun1() CALLED!!')

# def fun2():
#     print('fun2() CALLED!!')

# def fun3():
#     fun1()
#     fun2()
#     print('fun3() CALLED!!')

# fun3()
# '''
# print('fun1() CALLED!!')
# print('fun2() CALLED!!')
# print('fun3() CALLED!!')
# '''

# def fun4():                # 무한 반복   RecursionError
#     print('fun4() CALLED!!')
#     fun4()
 
# fun4() 

#  재귀 함수 : 가장 대표적인 재귀함수 펙토리얼(factorial) stack구조

# def factorial(n):
#     print('+')
#     # 종료 조건
#     if n == 1:
#         return 1
#     # 자기 자신을 다시 호출

#     return n * factorial(n-1)

# 재귀함수 stack 구조 
# 
# factorial(3) 실행 -> 화면에 +가 출력 ->  n != 1, return 3 * factorial(2) -> factorial(2) ? 일단 대기
# factorial(2) 실행 -> 화면에 +가 출력 ->  n != 1, return 2 * factorial(1) -> factorial(1) ? 일단 대기
# factorial(1) 실행 -> 화면에 +가 출력 ->  n == 1, 1을 들고 퇴근

'''💡 여기까지의 중간 점검:
화면에는 +가 총 3번 출력되었고, 컴퓨터 메모리에는 factorial(3)과 factorial(2)가 일을 다 끝내지 못한 채 굳어있음'''

'''붕괴 단계: 꼭대기부터 도미노처럼 계산하기 (반환 단계)
이제 맨 꼭대기 층에서 1이라는 명확한 숫자가 내려왔으니, 대기하고 있던 아래층 상자들이 도미노처럼 차례대로 풀리기 시작'''

# factorial(1) = 1  -> factorial(2) = 2 * 1 = 2 -> factorial(3) = 3 * 2 -> 따라서 6이 된다. 

'''주의사항

1. 종료 조건 (Base Case): 반드시 멈추는 구간(n == 1)이 있어야 함
2. 반복 구역 (Recursive Case): 문제를 더 작은 단위로 쪼개어 자기 자신에게 토스하는 구간(factorial(n-1))


#quiz) 다국어 인사말 프로그램 by 함수
'''
출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램을
함수를 이용해서 만들어봅시다. 
1. 한국     2.USA   3.Japan
'''

# def introKor():
#     print('안녕')

# def introUSA():
#     print('Hello')

# def introJapan():
#     print('こんにちは')

# selectedMenuNum = int(input('where are you from? 1.한국   2.USA   3.Japan'))

# if selectedMenuNum == 1:
#     introKor()

# elif selectedMenuNum == 2:
#     introUSA()

# elif selectedMenuNum == 3:
#     introJapan()

# quiz) 계산기 프로그램 by 함수

'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램을
함수를 이용해서 만들어봅시다. 
'''
   # 최대한 부품화해서 기능을 세분화할 것
def add(): 
    print(f'덧셈 결과: {inputNumber1 + inputNumber2}')
def sub():
    print(f'뺄셈 결과: {inputNumber1 - inputNumber2}')
def mul():
    print(f'곱셈 결과: {inputNumber1 * inputNumber2}')
def div():
    print(f'나눗셈 결과: {inputNumber1 / inputNumber2}')

def calculator(): 
    if selectedOperator == 1:           # 덧셈
        add()
    elif selectedOperator == 2:         # 뺄셈
        sub()
    elif selectedOperator == 3:         # 곱셈
        mul()
    elif selectedOperator == 4 :         # 나눗셈
        div()        

inputNumber1 = float(input('숫자를 입력하세요.'))
selectedOperator = int(input('연산자를 선택하세요. 1. 덧셈 2. 뺄셈 3.곱셈  4.나눗셈'))
inputNumber2 = float(input('숫자를 입력하세요.'))

calculator()

# TDD : 실제 코드를 작성하시 전에 테스트 케이스를 먼저 작성하는 소프트웨어 개발방법론

'''실패하는 테스트 작성(RED) -> 테스트 통과 코드 작성(Green) -> 리팩토링(Refactor)의 짧은 주기를 반복 
고품질의 버그없는 코드'''

# 부품? 인터페이스? (끼워넣을 수 있는?)

'''"부품화(함수 세분화)를 잘해두고 매개변수/리턴이라는 규격(인터페이스)을 잘 맞춰두면, 
언제든 필요한 곳에 쏙 끼워 넣을 수 있는 고품질의 코드가 된다. 
이것이 잘 되어야 TDD(테스트 주도 개발)도 가능하다!"'''






