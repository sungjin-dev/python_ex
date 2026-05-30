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

a = [1,2,3,4,5]

while a:
    print(a)
    a.pop()

if []:
    print('참')

a = [1,2,3]
print(id(a))

a = [1,2,3]
b = a
print(id(a))
print(id(b))

print(a is b)

# a = [1,2,3]
# b = a[:]   # 잘라서 따로 가져오는거라 중첩구조가 아닌경우 마치 deepcopy처럼 된다.
# a[1] = 4
# print(a)
# print(b)

# 슬라이싱 b = a[:] (얕은 복사, Shallow Copy)

a = [1, 2, [3, 4]]  # 리스트 안에 리스트가 들어있음
b = a[:]

b[2][0] = 99  # b 안의 리스트 요소를 변경
print(a)  # [1, 2, [99, 4]] 💥 a도 같이 바뀌어버림!
print(b)  # [1, 2, [99, 4]]

# 내부 리스트([3, 4])는 새 주소로 복사되지 않고 기존의 주소를 그대로 바라보고(참조하고) 있기 때문

a = 3
b = 5

a,b = b,a 

print(a)
print(b)
