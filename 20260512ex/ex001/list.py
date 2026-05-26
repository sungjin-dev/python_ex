# # 리스트(list)
# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(f'fruits: {fruits}')
# print(f'type of fruits: {type(fruits)}')

# # 리스트와 데이터

# '''
# 리스트에 포함되는 데이터는 어떤 자료형이드 상관없습니다. 
# 예를 들어 정수, 실수, 문자(열)이 하나의 리스트로 묶일 수도 있습니다.   
# '''

# complexList = [10, 3.14, 'a', 'hello']
# #이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는
# #파이썬과 javasript뿐이다. java는 안 된다. 

# print(f'complexList: {complexList}')
# print(f'type of complexList: {type(complexList)}')

# type of complexList: <class 'list'>

# ✅ list는 여러 자료형을 한 번에 저장할 수 있는 자료구조다.  ''''''' 이런 식으로 전부 해버리면 다 문자열
                                                            # 따라서 [2.8, '1', 5 ] 이런식으로 와야 
# ✅ 그리고 type()으로 보면 항상 <class 'list'>로 나온다.

# member = []
# print(f'member: {member}')
# print(f'type of member: {type(member)}')

#  ex) 다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자.

'''attendList = ['이순철','김병헌','김민우','박찬호','김민태']

how to 리스트의 아이템 조회

특정 아이템 조회'''


# #           0       1      2      3      4     5       6        7
# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(f'fruits[1]: {fruits[1]}')
# print(f'fruits[0]: {fruits[0]}')
# print(f'fruits[7]: {fruits[7]}')
# print(f'fruits[8]: {fruits[8]}') #  index error

# 만약 리스트에서 존재하지 않는 인덱스를 참조하면 어떻게 될까요?
# print(f'fruits[8]: {fruits[8]}')
# 당연히 에러가 발생합니다. 다음 코드로 확인해봅시다. (In)

# print()  -> 개행을 하니까 주의 할 것

# 리스트 길이(아이템 개수) 조회

'''
리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len()함수를 사용하면 알 수 있습니다. 
다음은 len() 함수를 이용해서 리스트의 길이를 확인하는 코드입니다. 
'''

# numbers = [1,2,3,4,5]

# print(f'numbers: {numbers}')
# print(f'numbers length: {len(numbers)}')

# numbers = [1,2,3,4,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,77]
# # 첫 번째 데이터 조회:
# print(f'첫 번째 데이터:{numbers[0]}')

# # 마지막 데이터 조회:  len(numbers) - 1     # 0부터 시작이니까 len()값에서 -1을 해줘야 한다. 
# print(f'마지막 데이터: {numbers[len(numbers)-1]}')   numbers[]  []칸에 해당 인덱스를 입력해서 출력하면 그 아이템이 나옴   

# len() 함수는 문자열의 길이를 조회하는데에도 사용된다.       
# str = 'hell  lll lll lllo'  #공백도 문자다
# print(len(str))     숫자면 len(num)   문자열이면 len(str)

# quiz) 입력한 글자 수 확인하기

# '''
# 사용자로부터 메시지를 입력 받고, 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어봅시다.
# '''

# msg = str(input('메시지 입력: '))

# msglen = len(msg)
# print(f'문자열 길이: {msglen}')

# msg = (input('메시지를 입력:'))

# msgLen = len(msg)
# print(f'msgLen: {msgLen}')

# print(len(['hello python']))  #이런식이면 문자열 1개가 들어간거라 1이다 

# 리스트 전체 데이터 조회
# balls = ['야구공', '축구공','탁구공','골프공','농구공']
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')

# for 변수 in 이터러블 데이터 :
#     pass

# balls = ['야구공', '축구공','탁구공','골프공','농구공']

# idx = 0         당연히 index가 0부터 시작이라서 

# for item in balls :                       # for문이 자동으로 item에 값을 넣어주는거기 때문에 for문이 만든 변수임                 
#     print(f'item: {item}, index: {idx}')  # ['야구공', '축구공','탁구공','골프공','농구공']  여기서 하나씩 꺼낸다는 의미
#     idx += 1

# idx = 0     
# for item in balls :                # item = '야구공'
#     print(f'item: {item}, index: {idx}')
#     idx += 1  
             
# balls = ['야구공', '축구공','탁구공','골프공','농구공']

# for idx, item in enumerate(balls):             #  for (index, value) in enumerate(balls)     
#     print(f'item: {item}, index: {idx}')

# for idx, item in enumerate(balls):
#     print(f'item: {item}, index: {idx}')

# balls = ['야구공', '축구공','탁구공','골프공','농구공']

# i = 0
# while i < len(balls):    원래 인덱스는 0부터 시작이기 때문에 통상적으로 i < num + 1 이런식으로 하는게 맞지만 len(balls)-1 +1 = len(balls) 
#     print(f'{balls[i]}, index: {i}')
#     i += 1

# str = 'python'

'''🔥 str = "python" 이 메모리에 저장되는 방식

문자열은 하나의 객체(object) 로 저장돼.

즉 "python" 전체가 통째로 문자열 객체로 저장되고,
그 안에서 인덱스로 접근할 수 있게 되어 있는 구조야.'''

# quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오.
 
# sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']

# lenvar = len(sports) - 1 
# print(f'lenvar: {lenvar}')


# lenVar = len(sports) - 1              # 5 - 1 => 4
# print(sports[lenVar])                 # 'soccer'
#                4

# quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램을 만드시오. 

# languages = ['c/c++', 'c#', 'python', 'java']

# pythonIdx = languages.index('python')          index값을 구해서 pop()을 이용해서 타격해서 지울 수 있다

# print(f'pythonIdx: {pythonIdx}')

# languages = ['c/c++', 'c#', 'python', 'java']

# targetIdx = languages.index('python')
# print(f'targetIdx: {targetIdx}')


# for idx, str in enumerate(languages):             #  idx, value 이 순서 기억하기 
#     if str == 'python':
#         print(f'python idx: {idx}')              # 출력할 때는 enumerate (idx, value) 반대로  value , idx 

# languages = ['c/c++', 'c#', 'python', 'java']        

# for idx, str in enumerate(languages):             #  idx, value 이 순서 기억하기 
#     if str == 'python':
#         print(f'python idx: {idx}')   #if절에 종속된 출력값을 원한다면 들여쓰기를 해야한다            
 
# targetIdx = languages.index("python")           # 간단하게 쓸 수 있는 함수   = .index("")
# print(f'targetIdx: {targetIdx}')

#  아이템 기존 리스트에 삽입
#  리스트 마지막에 삽입

# sports = ['football', 'baseball', 'volleyball']    # 3
# print(f'sports: {sports}')                    #['football','baseball', 'volleyball']

# sports.append('basketball')
# print(f'sports: {sports}')                    #['football','baseball', 'volleyball','basketball']
# print(f'sports lenght: {len(sports)}')                    

# quiz) 취미 추가하기 

'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가 되는 프로그램을 만들어보자!
그리고 취미의 개수를 출력하자!
'''

# hobbies = []

# while True:
#     hobby = str(input('취미:'))
#     hobbies.append(hobby)
#     selectedNum = int(input('1. 추가  2. 종료'))
#     if selectedNum == 2:
#         break
# print(f'hobbies = {hobbies}, 개수: {len(hobbies)}')    

# ✅ print 위치는 지금처럼 while 밖이 맞음  while문이 최종적으로 완료된 이후의 출력값을 원하는거기 때문
# ⭐ 더 편하게 하려면 메뉴 입력을 먼저 받는 방식도 좋음 (이렇게 할 경우 취미를 입력x 선택지도 존재)

# hobbies = []

# while True:
#     selectedNum = int(input('1. 추가  2. 종료: '))

#     if selectedNum == 2:
#         break

#     hobby = input('취미: ')
#     hobbies.append(hobby)

# print(f'hobbies = {hobbies}, 개수: {len(hobbies)}')

# 이렇게 하면 종료하고 싶을 때 바로 2 누르면 끝나.

# hobbies = []

# hobby = str(input('취미 입력:'))
# hobbies.append(hobby)
# print(f'hobbies : {hobbies}')


# hobbies = []

# hobby = input('취미 입력:')
# hobbies.append(hobby)
# print(f'hobbies: {hobbies}')

'''
취미 입력:축구
hobbies: ['축구']
'''

# hobbies = []

# while True:
#     hobby = input('취미 입력:')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     selectedNumber = int(input('1. 취미 추가   2. 종료'))
#     if selectedNumber == 2:
#         print(f' 총 개수: {len(hobbies)}')
#         break


# # hobbies = []

# flag = True

# while flag:

#     hobby = input('취미 입력:')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     selcectedMenuNumber = int(input('1. 취미 추가   2. 종료'))   
#     if selcectedMenuNumber == 2:
#         print(f'총 개수: {len(hobbies)}')
#         flag = False    #   or True....  break 


#  특정 위치에 아이템 삽입
#  리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용합니다. 

# countries = ['korea', 'china', 'japan']      # ['korea', 'usa', 'china', 'japan']
# countries.insert(1, 'usa')
# print(f'countries: {countries}')        # countries: ['korea', 'usa', 'china', 'japan']


# quiz) 누락된 숫자 추가하기 

# numbers = [1,2,3,4,5,7,8 ,9]          6,10
# numbers 리스트를 보고 1~10까지 숫자 중 누락된 숫자를 추가해보자.

# numbers = [1,2,3,4,5,7,8,9]         # 6, 10 이 누락된 상황

# numbers.insert(5,6)
# numbers.insert(9,10)               # =>  numbers.append(10)  이거랑 같음


# numbers = [1,2,3,4,5,7,8,9]
# numbers.insert(5, 6)
# print(f'numbers: {numbers}')
# numbers.insert(9, 10)            # numbers.append(10)
# print(f'numbers: {numbers}')

# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend()함수를 사용합니다. 

# list1 = [1,2,3]
# print(f'list1 : {list1}')          # [1, 2, 3]

# list2 = [10, 20, 30]
# print(f'list2: {list2}')           

# list1.extend(list2)                # [1, 2, 3, 10, 20, 30]
# print(f'list1: {list1}')
# print(f'list2: {list2}')

# #---------------------------------------------------------------------

# list3 = list1 + list2                      # [1, 2, 3, 10, 20, 30]
# print(f'list1: {list1}')
# print(f'list2: {list2}')
# print(f'list3: {list3}') 
                  
# print(f'list3: {list3}')

# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제

# sports = ['football', 'baseball', 'volleyball', 'basketball']

# sports.pop()
# print(f'sports: {sports}') 


# sports = ['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports : {sports}')          #['football', 'baseball', 'volleyball', 'basketball']
# sports.pop()                         #['football', 'baseball', 'volleyball']
# sports.pop(1) 
# print(f'sports : {sports}')            #['football', 'volleyball']

# pop(n)   n 자리에 원하는 인덱스 기입하면 그 자리 삭제

# removedItem = sports.pop()                     # []'football']
# print(f'removedItem: {removedItem}')           # volleyball

# # pop() 대신 del 키워드를 이용해서 아이템을 삭제할 수 있다. 
# sports = ['football', 'baseball', 'volleyball', 'basketball']          list.pop()  vs del list()
# del sports[2]
# print(f'sports: {sports}')

# # quiz) sports 리스트에서 'volleyball'을 삭제하는 프로그램을 만들자. 

# sports = ['football', 'baseball', 'volleyball', 'basketball']

# volleyballIdx = sports.index('volleyball') 

# sports.pop(volleyballIdx)   del sports[2]

# print(f'sports: {sports}')

# sports = ['football', 'baseball', 'volleyball', 'basketball']
# volleyballIdx = sports.index('volleyball')
# sports.pop(volleyballIdx)
# print(f'sports: {sports}')

'''다음 리스트에서 마지막 요소를 출력하는 코드를 작성하시오.
numbers = [10, 20, 30, 40]'''

# 너 답:

# lastValue = numbers.pop(3)
# print(lastValue)

# ✅ 정답 (리스트 길이가 4라서 인덱스 3이 마지막 맞음)

# 더 일반적인 방식은:

# numbers[-1]  == numbers[len(numbers) - 1]  

# -1은 "없는 인덱스"가 아니라
# ✅ 파이썬이 지원하는 뒤에서부터 접근하는 인덱스 방식이야.

