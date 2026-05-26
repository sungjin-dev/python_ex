'''
리스트와는 다르게 튜플에 포함된 아이템을 수정할 수 없음
'''

# tuple() 

# fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')

# print(f'fruits: {fruits}')
# print(f'fruits type: {type(fruits)}')       #tuple

'''튜플 조회'''


'''
튜플은 아이템의 수정이 불가능하기 때문에 아이템의 삽입, 삭제, 정렬 등의 기능은 없고 
조회하는 기능을 주로 사용합니다. 
'''

# fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
# print(f'{fruits[3]}')       # 참외

''' quiz) 튜플에서 인덱스가 홀수인 아이템 조회하기 '''

# sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

# for idx, item in enumerate(sports):
#     if idx % 2 == 1:
#         print(f' item : {item}, idx: {idx}')  

# for idx, item in enumerate(sports):
#     if idx % 2 == 1:
#         print(f'idx: {idx}, item: {item}')

'''
특정 아이템의 인덱스(index) 조회
튜플 내 특정 아이템의 인덱스를 확인할 때는 index() 함수를 이용합니다.
'''   

# fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나') 
# print(f'idx: {fruits.index('바나나')}')  #7  


'''
quiz) 아이템 값으로 인덱스 출력하기
튜플에서 사용자가 선수 이름을 입력하면 이름에 해당하는 인덱스를 출력해봅시다.
'''  
  
# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')


# sportsPlayer = str(input('선수 이름 입력:'))
# idx = names.index(sportsPlayer)
# print(f'sportsPlayer Num: {idx}')

# idx = names.index(input())

# print(idx)

# inputData = input('선수 이름 입력:')
# print(f'이름: {inputData}, 인덱스: {names.index
#                                (inputData)}')

# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# inputData = input('선수 이름 입력:')
# print(f' 이름 : {inputData}, 인덱스: {names.index(inputData)}')

# names.index('value')