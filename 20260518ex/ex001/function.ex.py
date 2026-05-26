# goods = {
#     '새우깡': 1200,
#     '비비빅': 400,
#     '초코파이': 500,
#     '맛동산': 1500
# }

totalPrice = 0 

def shrimpCrackerPrice

# totalPrice = 0

# def shrimpCrackerPrice():
#     global totalPrice        # 최상단에 위치해야함
#     totalPrice += goods['새우깡'] * shrimpCrackers
#     print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}')

# def bibibigsPrice():
#     global totalPrice
#     totalPrice += goods['비비빅'] * bibibigs
#     print(f'비비빅 구매 금액: {goods['비비빅'] * bibibigs}')

# def chocopiePrice():
#     global totalPrice
#     totalPrice += goods['초코파이'] * chocopies
#     print(f'초코파이 구매 금액: {goods['초코파이'] * chocopies}')

# def matdongsanPrice():
#     global totalPrice
#     totalPrice += goods['맛동산'] * matdongsans
#     print(f'맛동산 구매 금액: {goods['맛동산'] * matdongsans}')
   
# shrimpCrackers = int(input('새우깡 구매 개수: '))
# bibibigs = int(input('비비빅 구매 개수: '))
# chocopies= int(input('초코파이 구매 개수: '))
# matdongsans= int(input('맛동산 구매 개수: '))

# print(f'새우깡 구매 개수: {shrimpCrackers}')
# print(f'비비빅 구매 개수: {bibibigs}')
# print(f'초코파이 구매 개수: {chocopies}')
# print(f'맛동산 구매 개수: {matdongsans}')
# print('=' * 40)
# shrimpCrackerPrice()   이렇게 호출을 해야 실제로 액션이 이루어짐.
# bibibigsPrice()
# chocopiePrice()
# matdongsanPrice()
# print('=' * 40)
# print(f'총 구매 금액: {totalPrice}')
# print('=' * 40)

# '''파이썬은 totalPrice += ... 이 문장을 보는 순간, 등호(=)가 있으니까 
# "아! 이 함수 방 안에서 쓸 totalPrice라는 새로운 '지역 변수'를 만들라는 거구나!"라고 판단'''

# # 전역 변수 지역 변수?

# def hello():
#     message = '안녕하세요'
#     print(message) -> 이건 출력된다 

# hello() 
# print(message) -> 지역 변수를 인식 못 함 (Name Error)

# 전역변수

# name = '철수'

# def hello():

# # 전역변수(공공재)와 지역변수(시한부)의 우선순위

# # 1. 함수 내부에 같은 이름의 변수가 있으면 지역 변수가 우선
#  - > 지역 변수를 쓰고 시한부

# # 2. global 
# # 함수 내부에서 전역변수를 수정하고 싶을 때 사용합니다. 

# count = 0 

# def increase():
#     global count
#     count = count + 1  # <- global 덕분에 지역변수로 바뀌지 않고, 전역변수가 '그대로' 수정됨!
#     print(count)       # <- 전역변수를 수정한 결과를 출력한 것임
#                                 #UnboundLocalError#
# increase()

# global -> 함수에서만 사용
# while문과 for문은 자신만의 독립된 방(지역, Local)을 만들지 못하기 때문


'''3. 파이썬이 변수를 찾는 순서: LEGB 규칙
파이썬은 변수를 찾을 때 돋보기를 들고 안쪽에서부터 바깥쪽으로 나가면서 찾습니다. 
이 범위를 스코프(Scope)라고 하며, 앞 글자를 따서 LEGB라고 부릅니다.

L (Local): 가장 먼저 함수 내부(지역)를 찾습니다. (1순위)

E (Enclosing): 함수 안에 함수가 또 있는 중첩 함수 구조일 때, 
나를 감싸고 있는 바깥 함수를 찾습니다. (2순위)

G (Global): 함수 밖, 즉 파일 전체(전역) 영역에서 찾습니다. (3순위)

B (Built-in): 파이썬이 기본으로 제공하는 내장 함수들(예: print(), len()) 영역에서 찾습니다. (4순위)'''

# 만약 우선순위를 깨고 

'''"나 함수 안에서 새로 변수 안 만들고, 밖에 있는 전역변수 진짜로 고칠래!"'''

# 라고 하려면 키워드를 써야 합니다. 바로 global입니다.

# age = 25

# print(f'age: {age}')
# def modifyage():
#     age += 1


# student = {          # student 변수 {} 데이터의 주소값을 가지고 있다
#     '이름': '홍길동',
#     '나이': 25
# }

# print(f'나이: {student['나이']}')

# def modifyStudentAge():
#     student['나이'] += 1

# modifyStudentAge()
# print(f'나이: {student['나이']}')

# # age라는 메모리 공간에 25라는 데이터를 직접 가지고


# student01 = {
#     '이름' : '홍길동',
#     '나이' : 25
# }

# student02 = student01

# student01['나이'] = 100
# print(student02['나이'])    #100

# import copy

# student02 = copy.deepcopy(student01)

# student01['나이'] = 1000
# print(student02['나이'])    #25


# funcs = []
# for i in range(3):   0 1 2
#     funcs.append(lambda: i * 2)

# 0 2  

# print(funcs[0](), funcs[1]())


# x = "global"

# def outer():         # 독립된 방
#     x = "outer"
#     def inner():     # 독립된 방 , 설계도일 뿐임
#         global x
#         x = "inner"
#     inner()          # 시동 버튼, 실제 액션
#     print(x, end=' ')

# outer()
# print(x)

# 💡 답변: "정의(설계)"와 "호출(실행)"은 완전히 다른 단계

# def inner():로 함수를 선언하는 것은 "나중에 작동시킬 기계의 설계도(또는 매뉴얼)"를 
# 뇌 속에 기억만 해두는 행동


# 답 : outer inner

# return 

'''return은 함수 내부에서 작업을 마치고 결과값을 
함수 바깥으로 전달하면서 함수의 실행을 즉시 종료시키는 역할

return을 만나면 뒤에 코드가 얼마나 더 남아있든 상관없이 
그 즉시 함수가 끝납니다.

return  # 값을 지정하지 않고 종료만 함 -> none 도출

return 뒤에 쉼표(,)로 구분해서 여러 값을 적으면, 하나의 튜플(Tuple)로 묶여서 반환

return: 함수가 끝난 후 결과값을 진짜 데이터로 반환

'''

# sum = 10

# def calculate():
#     sum = 20
#     return sum

# calculate()
# print(sum([1, 2]))          # sum은 sum(1,2) x  , sum[1,2] 이런식으로 대괄호로 해야한다. 리스트 함수 내 아이템을 모두 더하는 의미


'''이 문제가 주는 교훈 (필기노트 박제용)
파이썬에서 기본으로 제공하는 내장 함수 이름들(sum, list, dict, int, str, max, min, id 등)은 
절대로 변수 이름으로 사용하면 안 된다! 
변수 이름으로 쓰는 순간, 진짜 원래 함수 기능을 파일 안에서 영영 쓸 수 없게 가려져 버린다.'''

'''
연습 문제!

기능 구현하기 (Advanced Task)
---

중첩 데이터 평면화 (Flattening): {"a": 1, "b": {"c": 2, "d": 3}}를 {"a": 1, "b.c": 2, "b.d": 3}
으로 변환하는 재귀 함수를 만드세요.


2. 값 기준 그룹화 (Grouping): pets = [("dog", "A"), ("cat", "B"), ("dog", "C")] 
리스트를 {"dog": ["A", "C"], "cat": ["B"]} 딕셔너리로 변환하세요.

pets = {
    "dog", ["A", "C"]
    "cat", "A"
}
---
3. 가장 빈번한 K개 요소: 텍스트 문자열에서 가장 많이 등장하는 
단어 상위 3개를 {단어: 빈도수} 형태로 반환하는 기능을 만드세요.

---
4. 딕셔너리 차집합: 두 딕셔너리 dict1, dict2를 비교하여 키와 값이 
모두 같은 아이템만 제외하고 dict1에 남아있는 요소만 추출하세요.

---
5. JSON 데이터 스키마 검증: 기준이 되는 template = {"name": str, "age": int}가 있을 때, 
특정 딕셔너리가 이 데이터 타입들을 준수하는지 확인하는 함수를 만드세요.
---
6. LRU 캐시 시뮬레이션: collections.OrderedDict를 사용하여 최대 3개의 아이템만 저장하고, 
가장 오래된 아이템을 삭제하는 간단한 캐시 구조를 만드세요.
---
7. 중첩 값 합산: sales = {"A": {"m1": 10, "m2": 20}, "B": {"m1": 5}}에서 모든 하위 수치들의 총합(35)을 구하세요.
---
8. 키 변경하기: 딕셔너리의 특정 키 이름을 변경하세요. (예: {"old": 1} -> {"new": 1}, 값은 유지)
---
9. 조건부 딕셔너리 병합: 두 딕셔너리를 합치되, 같은 키가 있다면 더 큰 값을 선택하도록 만드세요.
---
10. 인버티드 인덱스 (Inverted Index): {"doc1": "apple banana", "doc2": "banana cherry"}를 
입력받아 각 단어가 어느 문서에 등장하는지 {단어: [문서리스트]} 형태로 변환하세요. (편집됨) '''

# dict1 = {}
# dict2 = {}

# for key1, value1 in dict1.items():
    
#     for key2, value2 in dict2.items():
#         if key1 == key2 and value1 == value2:
#             del dict1[key1]  
# print(dict1)


dict1 = {}
dict2 = {}

for key1, value1 in dict1.items():
    if key1 in dict2 and dict2[key1] == value1:
        del dict1[key1]

print(dict1)