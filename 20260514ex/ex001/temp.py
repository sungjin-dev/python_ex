# split(쪼갠다.)

# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# print(f'names: {names}')
# print(f'names type: {type(names)}')

# str = "박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아"
# splitedStr = str.split(" ")
# print(f'splitedStr: {splitedStr}')  # 리스트로 나옴★
# print(f'splitedStr type: {type(splitedStr)}')  

# str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
# splitedStr = str.split("+")           # list -> tuple
# print(f'splitedStr: {splitedStr}') 
# print(f'splitedStr type: {type(splitedStr)}') 

# splitedStr = tuple(splitedStr)
# print(f'splitedStr: {splitedStr}') 
# print(f'splitedStr type: {type(splitedStr)}')

# str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
# splitedStr = str.split("-")           
# print(f'splitedStr: {splitedStr}') 
# print(f'splitedStr type: {type(splitedStr)}')

# str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
# spiltedStr = str.split("+")
# print(f'splitedStr: {spiltedStr}')

# splitedStr: ['박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아']  하나의 문자열로 리스트
# splitedStr type: <class 'list'>

#  튜플 안의 아이템 유/무 확인하기    in은 있으면 T 없으면 F , not in은 없으면 T, 있으면 F

# in과 not in 키워드를 사용하면 튜플 안에 특정 아이템의 존재 유/무를 확인할 수 있습니다. 

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# print(f'{'Green' in colors}')        # True     True or False 로 결과값이 나옴

# print(f'{'Green+' in colors}')       # False

# if 'Green' in colors:
#     print('colors에는 Green이 있습니다.')
# else: 
#     print('colors에는 Green이 없습니다.')

# # not in 없으면 True 

# print(f'{'Green' not in colors}')        # False     

# print(f'{'Green+' not in colors}')       # True

# if 'Green' not in colors:
#     print('colors에는 Green이 없습니다.')
# else: 
#     print('colors에는 Green이 있습니다.')

# quiz) 학점 경고 프로그램 만들기
'''
scores는 1학기 성적을 튜플로 나타낸 것입니다. F 학점이 있으면 ‘경고’를 출력하는 프로그램을 만들자!
scores = ('A', 'A+', 'B', 'B-', 'F') 
'''

# scores = ('A', 'A+', 'B', 'B-', 'F') 

# if 'F' in scores:
#     print ('경고')
# else:
#     print('경고 없음')

# scores = ('A', 'A+', 'B', 'B-', 'F')

# if 'F' in scores:
#     print('경고!!!!')
# else:
#     print('경고 없음')

# scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
# fCnt = scores.count('F')   #2         scores.count('value')
# print(f'F학점 개수: {fCnt}') 

# 튜플 결합
# at list

# nums1 = [1,2,3]
# nums2 = [10,20,30]

# # 첫 번째 방법
# nums1.extend(nums2)
# print(f'nums1: {nums1}')

# # 두 번째 방법

# result = nums1 + nums2
# print(f'nums1: {nums1}') 
# print(f'nums2: {nums2}') 
# print(f'result: {result}') 

# at tuple  (+를 이용하면 서로 다른 튜플을 결합)
# nums1 = [1,2,3]
# nums2 = [10,20,30]

# # nums1.extend(nums2)          extend는 안 된다 tuple은 한번 선언되면 수정이 안되니까 연장 기능x

# result = nums1 + nums2
# print(f'nums1: {nums1}') 
# print(f'nums2: {nums2}')
# print(f'result: {result}') 

# num1 = 10
# num2 = num1

# print(f'num1: {num1}')   # 10
# print(f'num2: {num2}')   # 10

# num1= 100
# print(f'num1: {num1}')   # 100
# print(f'num2: {num2}')   # 10

# ------------------------------------

# nums1 = [1,2,3]
#                         # 나혼자산다
# print(f'nums1: {nums1}')         # [1,2,3]
# print(f'nums2: {nums2}')         # [1,2,3]

# nums1[0] = 100                         # 룸메임
# print(f'nums1: {nums1}')         # [100, 2, 3]
# print(f'nums2: {nums2}')         # [100, 2, 3]

# for idx, num in enumerate(nums1):
#     nums2[idx] = num        # 깊은 복사 : 따로 메모리방을 한땀 한땀 만들어서 새로운 메모리 주소 할당

# nums1 = [1,2,3]
# nums2 = nums1 
# for idx, num in enumerate(nums1):
#      nums2[idx] = num 

# idx = 0
# num = 1

# idx = 1
# num = 2

# idx = 2
# num = 3

# nums1 = [1,2,3]
# nums2 = [0,0,0]

# for idx, num in enumerate(nums1):
#     nums2[idx] = num 

# print(f'nums1: {nums1}')         
# print(f'nums2: {nums2}') 

# nums1[0] = 100
# print(f'nums1: {nums1}')         
# print(f'nums2: {nums2}')


# print('deep copy -----------------')

# import copy

# a = [1,2,3,4,5]

# b = copy.deepcopy(a)     #    b = a.copy()     list2 = list1.copy()

# import copy

# a = [1,2,3,4,5]

# b = copy.deepcopy(a)

# print(b)

# b[0] = 100

# print(f'a : {a}')
# print(f'a : {b}')

# 슬라이싱                  (n : m-1)  n에서 m까지 

# animals = ('호랑이', '사자', '곰', '여우', '늑대')
# print(f'animals: {animals}')

# print(f'animals[:3]: {animals[:3]}')        # ('호랑이', '사자', '곰')
# print(f'animals[1:4]: {animals[1:4]}')      # ('사자', '곰', '여우')
# print(f'animals[:-2]: {animals[:-2]}')      # ('호랑이', '사자', '곰')
# print(f'animals[-1:-2]: {animals[-1:-2]}')    # () 
# print(f'animals[-3:-1]: {animals[-3:-1]}')    # ('곰', '여우') 

# animals = ('호랑이', '사자', '곰', '여우', '늑대', '양')

# print(f'animals[:-2]: {animals[:-2]}')      # ('호랑이', '사자', '곰', '여우')
# print(f'animals[-1:-2]: {animals[-1:-2]}')    # () 
# print(f'animals[-3:-1]: {animals[-3:-1]}')    # ('여우', '늑대')

# print(f'animals[:-2]: {animals[:-2+len(animals)]}')      # ('호랑이', '사자', '곰', '여우')
# print(f'animals[-1:-2]: {animals[-1+len(animals):-2+len(animals)]}')    # () 
# print(f'animals[-3:-1]: {animals[-3+len(animals):-1+len(animals)]}')    # ('여우', '늑대')

# 공식 : animals[-1+len(animals):-2+len(animals)] 이런식으로 음수값에 전체 길이를 더해주면 됩니다.


# 1. 1단계: 번호 매기기 (뒤에서부터 -1, -2...)
# 리스트나 튜플의 가장 마지막 글자를 -1이라고 생각하세요. 왼쪽으로 갈수록 숫자가 작아집니다.

# 2. "n번 위치에서 시작해서, m번 위치 '직전' -1 느낌 ? 에서 멈춘다."
# ->항상 왼쪽에서 '오른쪽★'으로만 흐릅니다.

# 문제 발생: -1에서 -2로 가려면 왼쪽(역방향)으로 가야 합니다. 
# 하지만 슬라이싱은 기본적으로 오른쪽(정방향)으로만 움직입니다.
# 결과: 갈 곳이 없으므로 빈 값 ()이 나옵니다.


# 슬라이싱 연습하기
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''

# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
# print(f'fruits[2:5]: {fruits[2:5]}') 
# print(f'fruits[:4]: {fruits[:4]}') 
# print(f'fruits[3:]: {fruits[3:]}') 


 # 리스트와 튜플간 변환(형변화, casting)

'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
또한 리스트로 선언된 데이터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
 '''

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# Orange => 오렌지 
# colors[1] = '오렌지'

# colors = list(colors)
# print(f'colors type: {type(colors)}')

# colors[1] = '오렌지'
# print(f'colors: {colors}')

# idx = colors.index('오렌지')
# colors[idx]

# colors = tuple(colors)
# print(f'colors: {colors}')

# quiz) 튜플 정렬하기

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# colors = list(colors)
# print(f'colors: {colors}')
# colors.sort()   
# print(f'colors: {colors}')                 
# colors = tuple(colors)            
# print(f'colors: {colors}')


# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# cs = tuple(sorted(colors))   # 기존 데이터는 그대로 있음
# print(f'cs: {cs}')

# cs = sorted()    #  기본적으로 list 함수로 나오는데 이후 수정을 완료하고 tuple 붙이는게 좋음

# 튜플에 저장된 아이템을 조회 [] o    () x 



# 활당 (대인) 연산

# num = 10

# 구조분해할당
# [1, 2] > a = 1, b =2

# nums = [1, 2]
# a = nums[0]
# b = nums[1]

# a, b = [1, 2]   # a = 1, b = 2
# print(a)
# print(b)

# x, y = (10, 20)
# print(x)
# print(y)

# # 순서 바꾸는 방법

# a = 1
# b = 2
# a, b = b, a

# print(a)
# print(b)

# #

# a, *rest = [1, 2, 3, 4]

# print(a)
# print(rest)

# '''
# a = 1
# rest = [2, 3, 4]
# '''
# a = list([a])  이후 리스트 함수로 만들고 싶으면 

