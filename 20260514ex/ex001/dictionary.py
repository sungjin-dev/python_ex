''' 컨테이너 자료형 

딕셔너리(dictionary)
    
리스트가 인덱스(index)를 이용해서 아이템을 참조 vs 딕셔너리는 키(key)를 이용

리스트는 자동으로 인덱스가 생성되지만 딕셔너리는 키를 하나하나 직접 만들어줘야함'''

'''
딕셔너리(dictionary)는 리스트와 함께 파이썬 프로그램에서 많이 사용하는 컨테이너 자료형입니
다. 리스트가 인덱스를 이용하여 아이템을 참조한다면, 딕셔너리는 인덱스 대신 키(key)를 이용하
여 아이템을 참조합니다.  키값이 하나하나 지정돼있어 딕셔너리는 속도가 빠르다 
'''

'''딕셔너리 정의

ages = {'박찬호': 48, '박지성': 40, '박세리': 50 , '이승엽' : 43, '박찌성': 40}  # 숫자라서 그냥 정수

쉼표(,) 데이터를 구분한다   키값은 유니크해야한다. 중복되면 안 된다. value값은 같아도 상관 없음'''

# print(f'ages: {ages}')
# print(f'ages type: {type(ages)}')


# scores = {'C/C++': 'A', 'Java': 'B+', '네트워킹': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}  # 문자열이라 ''사용

# print(f'scores: {scores}')


'''마지막 내용 : *******************************************
리스트, 튜플, 딕셔너리''' 

# listVar = (3, 3.14, 'hello')
# print(f'listVar: {listVar}')


# tupleVar = (3, 3.14, 'hello')
# print(f'tupleVar: {tupleVar}')

# dickVar = {
#     '홍길동': 10,
#     '박찬호': '열살',
#     '박세리': 3.14
# }
# print(f'tupleVar: {tupleVar}')

# listVar1 = [1,2,3]
# listVar2 = [1,2,3,listVar1]

# print(f'listVar1: {listVar1}')    # [1,2,3]  
# print(f'listVar2: {listVar2}')    # [1, 2, 3, [1, 2, 3]] 

# print(listVar2[3])      # [1, 2, 3]
# print(listVar2[3][1])      # 2

# print(type(listVar2[3]))           # list
# print(type(listVar2[3][1]))        # int

# dicts = {
#     'name': '박찬호',
#     'age' : 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }

# print(f'dicts: {dicts}')
# '''
# {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}
# '''

# dicts['hobby'][1]      #   ['축구', '농구', '배구']         #dicts[키]  
# print(dicts['hobby'][1])

# 딕셔너리 조회/삽입/수정/삭제
# 컴퓨터 프로그램에서 '조회/삽입/수정/삭제'를 CRUD라고 합니다. 
# CURD라는 용어는 개발자라면 반드시 알고 있어야 합니다.
# CURD는 Create, Read, Update, Delete를 말합니다. 
# 즉, 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)하는 것을 말합니다.
# 그렇다면, 딕셔너리에서 CRUD는 딕셔너리 컨테이너 자료형에
# 데이터를 추가 (Create), 조회(Read), 수정(Update), 삭제(Delete)하는 것을 말할 것입니다. 
# CRUD는 프로그래밍 뿐만 아니라 데이터베이스에서도 사용되는 용어입니다. 


''' 추가(Create)'''
# dicContainer = {
#     '이름': '홍길동',
#     '나이': 25,
#     '주소': '대전 중구',
#     '취미': ['축구','수영', '조깅'],
#     '몸무게': 87.5

# print(f'dicContainer: {dicContainer}')

# dicContainer['연락처'] = '010-1234-5678'             #[] 대괄호를 써야함   
# print(f'dicContainer: {dicContainer}')

'''조회(Read)'''

# print(f'이름: {dicContainer['이름']}')           [key]

# # 수정(Update)
# dicContainer['몸무게'] = 50 
# print(f'몸무게: {dicContainer['몸무게']}')

'''키값이 기존에 없다면 생성 및 추가, 키값이 기존에 존재한다면 변경'''

# # 삭제(Delete)
# del dicContainer['몸무게']            # 이건 완전히 삭제됨
# print(f'dicContainer: {dicContainer}')

# # 부가 기능들
# # 아이템 개수 조회
# print(f'아이템 개수: {len(dicContainer)}')

# # 전체키 & 밸류를 조회 
# # 전체키
# dicContainer = {
#     '이름': '홍길동',
#     '나이': 25,
#     '주소': '대전 중구',
#     '취미': ['축구','수영', '조깅'],
#     '몸무게': 87.5
# }
# dickeys = dicContainer.keys()
# print(f'dickeys: {dickeys}')      #  ['이름', '나이', '주소', '취미', '연락처']

# for keys in dickeys:
#     print(f' {keys} : {dicContainer[keys]}')

# # 밸류
# dicValues = dicContainer.values()
# print(f'dicValues: {dicValues}')

'''키와 밸류를 한방에 조회
 for key, value in dicContainer.items():'''
#     print(f'{key}: {value}')

# print(dicContainer.items())
# print(type(dicContainer.items()))  # <class 'dict item'


# 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''
#1
scores = {
    'C/C++': 'A',    
    'Java' : 'B',     
    '모바일': 'C',    
    '보안' : 'A+',   
    '해킹' : 'F',    
    '시스템': 'C+'    
}
#2
print(f'Java: {scores['Java']}')
print(f'시스템: {scores['시스템']}')

#3
scores['파이썬'] = 'A'
scores['OS'] = 'A+'

print(f'scores: {scores}')

#4
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

#5
# -1
scores = {
    'C/C++':'A',
    'Java': 'B+',
    '모바일': 'C', 
    '보안': 'A+',
    '해킹': 'F', 
    '시스템': 'C+'
}

# -2
print(f'Java: {scores['Java']}')    # B+
print(f'시스템: {scores['시스템']}')  # C+

# -3
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(f'scores: {scores}')

# -4
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

# -5
creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'F': 0.0,
}

totalScore = 0
averageScore = 0

for key in scores.keys():
    totalScore += creditScores[scores[key]]
    print(f'{key}:\t{scores[key]}')     # A+ > 4.5, A > 4.0, B+ > 3.5 ... 

print(f'totalScore: {totalScore}')      # 23.0
averageScore = totalScore / len(scores)
print(f'averageScore: {averageScore}')  # 2.875

'''
C/C++:  A       4.0
Java:   F       0.0
모바일: C        2.0
보안:   A+       4.5
해킹:   F        0.0
시스템: A        4.0
파이썬: A        4.0
OS:     A+      4.5

A+      : 4.5
A       : 4.0
B+      : 3.5
B       : 3.0
C+      : 2.5
C       : 2.0
F       : 0.0
'''


# dicts = {
#     'name': '박찬호',
#     'age' : 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구'],
#     (1,2,3):10                        #  tuple(변경불가능이라 가능)   # list는 안 됨
# }

# [1, 2, 3, 4, 5]는 .copy()로 깊은복사가 되는데
# [[1, 2], [3, 4]]는 .copy()를 써도 답이 없어서 copy.deepcopy()를 쓰면 깊은복사가 됩니다.


# -PC방 자리 관리 프로그램 

# 너는 PC방 사장이다.
# 손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }
# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
# 2. 사용자에게 원하는 자리 번호 입력받기
# 3.예약할 자리 번호 :
# 4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
# 5.예약 후 전체 자리 상태 다시 출력하기
#
# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }

# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }

# lastSeat = []

# for key, value in seats.items():
#     if value == '빈자리':
#         lastSeat.append(key)
# selectedSeat = int(input(f'{lastSeat}값 중 한 자리를 고르시오.'))
 


# - 배달 주문 통계 프로그램 
# 배달 앱에서 하루 주문 데이터를 분석하려고 한다.
# 주어진 주문 목록
# orders = [
#     "치킨",
#     "피자",
#     "치킨",
#     "햄버거",
#     "피자",
#     "치킨"
# ]
# 프로그램 요구사

# 1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
# 2. 가장 많이 주문된 음식 찾기
# 3. 총 주문 개수 출력하기
# 4. 사용자가 음식 이름 입력하면
# 몇 번 주문됐는지 출력하기

# -시험 결과 분석 프로그램 
# 학원에서 시험 결과를 분석하려고 한다.
# 주어진 데이터
# scores = {
#     "민수": 88,
#     "지훈": 72,
#     "수아": 95,
#     "유진": 64,
#     "서연": 100
# }

# 프로그램 요구사항
# 1.전체 학생 점수 출력하기
# 2.평균 점수 계산하기
# 3.최고 점수 학생 찾기
# 4.60점 이상은 합격, 미만은 불합격 출력하기
# 5.90점 이상 학생 수 출력하기
# 6.점수 높은 순으로 학생 출력 도전하기

# scores = {
#      "민수": 88,
#      "지훈": 72,
#      "수아": 95,
#      "유진": 64,
#      "서연": 100
#}


seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

# 1. 빈자리인 좌석 번호만 골라내기 (노트에서 설계하신 부분)
lastSeat = []
for key, value in seats.items():
    if value == '빈자리':
        lastSeat.append(key)

# 2. 사용자 입력 받기
selectedSeat = int(input(f"{lastSeat}값 중 한 자리를 고르시오: "))

# 3. 예약 로직 완성하기 (빈칸을 채우세요)
if seats[selectedSeat] == "빈자리":
    
    seats["빈자리"] = "사용중"
    print("예약 완료")
else:
    # [빈칸 B] 이미 사용 중일 때의 경고 문구를 출력하세요.
    print("이미 사용 중")
# 4. 최종 좌석 상태 확인
print(f"최종 좌석 상태: {seats}")


print("예약 완료")

orders[search_menu]

if score > 90:

"60점 이상인 합격자 수: count('합격')


seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

# 1. 빈자리인 좌석 번호만 골라내기 (노트에서 설계하신 부분)
lastSeat = []
for key, value in seats.items():
    if value == '빈자리':
        lastSeat.append(key)

# 2. 사용자 입력 받기
selectedSeat = int(input(f"{lastSeat}값 중 한 자리를 고르시오: "))

# 3. 예약 로직 완성하기 (빈칸을 채우세요)
if seats[selectedSeat] == "빈자리":
    # [빈칸 A] 해당 자리를 "사용중"으로 변경하고 "예약 완료"를 출력하세요.
    ____________________
    print("예약 완료")
else:
    # [빈칸 B] 이미 사용 중일 때의 경고 문구를 출력하세요.
    ____________________

# 4. 최종 좌석 상태 확인
print(f"최종 좌석 상태: {seats}")

if seats[selectedSeat] == "빈자리":
    seats[selectedSeat] = "사용중"  # 사용자가 입력한 '방 번호(Key)'를 찾아가서 바꿈!
    print("예약 완료")
else:
    print("이미 사용중인 자리입니다. 다른 자리를 고르세요!")  # 빈칸 B