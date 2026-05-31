'''Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.'''


# import random

# randomNum = random.randrange(4,28)


# python = 'Python is Amazing'

# index = python.index('n') 

# print(index)
#                          # start 자리 지정
# index = python.index('n', index+1)

# print(index)

# print(python.find('Java')) # -1출력
# # print(python.index('Java')) # valueError


# a = [1,2,3,4,5,6]

# del a[2:]
# print(a)   # [1,2]  

# a = [1,2,3]

# print(a.pop())  # 값 3을 빼올 수 있다

# print(a.append(4)) # 값이 none
# print(a)

# print(a.count(1))

# # 튜플은 아무것도 없어도 튜플( sort, insert remove pop 안 됨)

# t = 1,2,3

# t1 = (1, 2,'a','b')
# print(t1[1:])   # (2, 'a', 'b')  실질적으로 자르는개념이 아니라 출력만 
# print(t1)       # (1, 2, 'a', 'b')

# # 딕셔너리
# # 
# a = {1 : 'a'} 
# a['파묘'] = '살목지'  # 해당 키값이 없으면 추가해서 들어감
# print(a)
# a[3] = [1,2,3]
# print(a)

# a = {1: 'a', '파묘': '살목지', 3: [1, 2, 3]}

# del a['파묘']
# print(a)

# # print(a['hi'])  # 없는 키값이라 에러
# print(a.get('hi')) # none이라는 어쨋든 값을 반환 오류가 안 남.
# print(a.get('hi', "값이 없습니다.")) # none 대신 구체적인 출력값을 입력할 수 있다.

# # 주의사항 get()  소괄호 형태이다. 

# s1 = set([1,2,3])
# l1 = list(s1)
# print(s1)

# s1 = set("hello")  # {'l', 'h', 'e', 'o'}  그냥 집합임. 순서 이런거 없음 중복도 없음
# print(s1)  
 
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# print(s1 & s2)              # {4, 5, 6}
# print(s1.intersection(s2))  # {4, 5, 6}
# print(s1 | s2)              # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s1.union(s2))         #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s1 - s2)              # 차집합 {1,2,3}
# print(s2 - s1)              # 차집합 {8, 9, 7}  순서는 뒤죽박죽
# print(s2.difference(s1))    # 차집합 {8, 9, 7}  

# s1 = set([1,2,3]) 
# s1.update([4,5,6])  #  {1, 2, 3, 4, 5, 6}
# print(s1)
# s1.remove(2)  # 집합은 인덱스 없어서 인덱스가 아니라 진짜 그 값을 지정해서 삭제임
# print(s1)

# list1 = [1,1,1,2,2,3,3,3,4,4]
# list2 = list(set(list1))
# print(list2)

# a = 1 == 2
# print(a)
# a = 1 == 1
# print(a)

# a = [1,2,3,4,5]

# while a:
#     print(a)
#     a.pop()

# if []:
#     print('참')

# a = [1,2,3]
# print(id(a))

# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))

# print(a is b)

# # a = [1,2,3]
# # b = a[:]   # 잘라서 따로 가져오는거라 중첩구조가 아닌경우 마치 deepcopy처럼 된다.
# # a[1] = 4
# # print(a)
# # print(b)

# # 슬라이싱 b = a[:] (얕은 복사, Shallow Copy)

# a = [1, 2, [3, 4]]  # 리스트 안에 리스트가 들어있음
# b = a[:]

# b[2][0] = 99  # b 안의 리스트 요소를 변경
# print(a)  # [1, 2, [99, 4]] 💥 a도 같이 바뀌어버림!
# print(b)  # [1, 2, [99, 4]]

# # 내부 리스트([3, 4])는 새 주소로 복사되지 않고 기존의 주소를 그대로 바라보고(참조하고) 있기 때문

# a = 3
# b = 5

# a,b = b,a 

# print(a)
# print(b)

# a = [1,2,3,4]

# result = []

# for num in a:
#     result.append(num * 3)

# print(result)

# a = [1,2,3,4]

# # result = [num * 3 for num in a]
# result = [num * 3 for num in a if num % 2 == 0]
#         # 목표       어디서 추출  조건 
# result(result)

# result = []
# for num in a :
#     if num in a:
#         if num % 2 == 0:
#             result.append(num*3)

# result = [x*y for x in range(2,10) for y in range(1,10)]

# for x in range(2,10):
#     for y in range(1,10):
#         result.append(x * y)
# print(result)

# 매개변수 인자 파라미터 
# 함수 안에서 정의되어 사용되는 변수 

# def add(a, b): # a, b는 매개변수 
#     return a+b 
# print(add(3,4))  # 3, 4 는 인수(arguments)

# def say():  # 입력값이 없이 출력만 함 
#     return 'Hi'

# a = say('a')

# print(a)

# def add(a,b):
#     print('%d, %d의 합은 %d입니다' (a,b, a+b))
#     return a + b

# a = add(1,2)

# print(a)

# def sub(a, b):
#     return a - b 

# result = sub(a = 7 , b =3)  # 순서에 맞춰서 하면 되긴 하지만 직접 지정해도 된다

# def addMoney(*args):
#     result = 0
#     for i in args:
#         result = result + i    # * args 에 입력받은  모든 값을 더한다
#     return result

# addMoney(1,2,3,4,5)

# def add_mul(choice, *args):
#     if choice == "add":       # 매개변수 choice에 "add"를 입력받았을 때
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":     # 매개변수 choice에 "mul"을 입력받았을 때
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add", 1,2,3,4)  
# result = add_mul("mul", 1,2,3,4)  

# print(result)



# def print_kwargs(**kwargs):  # *두개는 딕셔너리 형태로 받는다
#     print(kwargs)
#     print(kwargs['a'])
#     print(kwargs['b'])

# print_kwargs(a=1,b=2)

# def add_and_mul(a,b):
#     return a+b, a*b

# a, b = add_and_mul(3,4)

# print(a)
# print(b )

# '''일반 매개변수, 가변 매개변수(*args), 키워드 매개변수(**kwargs)를 모두 함께 사용할 수도 있다. 이때 순서는 반드시 다음과 같아야 한다.'''

# def mixed_function(name, *args, **kwargs):
#     print(f"이름: {name}")
#     print(f"추가 인수들: {args}")
#     print(f"키워드 인수들: {kwargs}")

# mixed_function('홍길동', 1, 2, 3, age=25, city='서울')
# # 이름: 홍길동
# # 추가 인수들: (1, 2, 3)
# # 키워드 인수들: {'age': 25, 'city': '서울'}

# def say_myself(name, old, man = True):

#     print('나의 이름은 %s 입니다.' % name)
#     print('나이는 %d살입니다.' % old)

#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')

# say_myself('봉쥬리', 20, False)
 
# 기본값이 있는 변수는 맨 마지막임. 가변인자도 마찬가지

# # vartest.py

# a = 1
# def vartest(a):
#     a = a +1

# vartest(a)
# print(a)

# # 함수가 숫자나 문자열 같은 값을 받았다. 이런 값들은 함수 안에서 변경해도 함수 밖의 원래 값에는 영향을 주지 않는다. 하지만 리스트나 딕셔너리 같은 자료형은 다르다.

# def change_list(my_list):
#      my_list.append(4)  # 리스트에 값을 추가

# a = [1, 2, 3]
# change_list(a)
# print(a)
# [1, 2, 3, 4]

# Immutable (정수, 실수, 문자열, 튜플)  

# Mutable (리스트, 딕셔너리, 집합)

# append insert 변형하는거지 리턴값이 없음 

# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

# def add(a, b):
#      return a+b


# add = lambda a, b: a+b
# result = add(3, 4)
# print(result)
# 7

a = [lambda a, b : a+b, lambda a, b : a*b]

print(a[1](3,4))   # 인덱스