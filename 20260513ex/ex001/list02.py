# # 리스트 정렬
# '''
# sort() 함수는 리스트의 아이템을 정렬하는데 사용합니다.
# reverse 옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬합니다  
#                         ascending          descending''' 

# # numbers = [5, 1, 3, 4, 2, 6]
# # print(f'numbers: {numbers}')       # [5, 1, 3, 4, 2, 6]


# # # 오름차순(ASC)
# # numbers.sort()     #  ==  numbers.sort(reverse = False)   reverse = False 기본적으로 내재
# # print(f'numbers: {numbers}')       # [1,2,3,4,5,6]

# # numbers.sort(reverse = True)
# # print(f'numbers: {numbers}')       # [6,5,4,3,2,1]

# # korean = ['다','가','마','하','카']
# # print(f'korean: {korean}')      # ['다', '가', '마', '하', '카']

# # korean.sort()                   #  ['가', '다', '마', '카', '하']
# # print(f'korean: {korean}')

# # korean.sort(reverse = True)      #  ['하', '카', '마', '다', '가']
# # print(f'korean: {korean}')

# # scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
# # print(f'scores: {scores}')  
# # scores.sort()
# # print(f'scores: {scores}')  
# # scores.sort(reverse = True)
# # print(f'scores: {scores}')   


# # quiz) 회의 참석자 정렬하기
# # 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.

# # names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# # print(f'names: {names}')
# # names.sort() 
# # print(f'names: {names}')
# # names.sort(reverse=True) 
# # print(f'names: {names}')

# # 리스트 순서 뒤집기

# # reverse() 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있습니다. 
# # vegetables = ['당근', '오이','양파','감자', '고구마']
# # vegetables.reverse() 
# # print(f'vegetables: {vegetables}')

# # 리스트 슬라이싱 (slicing) ★★★★★★★★
# # 슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것을 말합니다. 
# animals = ['호랑이','사자','곰','여우','늑대']
# # print(f'animals: {animals}')     # ['호랑이','사자','곰','여우','늑대']

# ''' 
#           l1-----------3l
# ['호랑이','사자','곰','여우','늑대']
# '''

# # print(f'animals[1:4]: {animals[1:4]}')     # [사자','곰','여우']
# # print(f'animals: {animals}')               # ['호랑이', '사자', '곰', '여우', '늑대']

# # sliceAnimals = animals[1:4]           
# # print(f'sliceAnimals: {sliceAnimals}')      # [''사자', '곰', '여우']         따로 방파고 메모리 숫자 저장

# # # [n:m] : n 인덱스부터 (m-1) 인덱스 까지의 아이템을 슬라이싱(추출)한다. 

# # animals = ['호랑이','사자','곰','여우','늑대']
# # print(f'{animals[:3]}')  # ['호랑이','사자','곰']       0이면 앞자리 생략 가능
# # # 인덱스 0부터 2(3-1)까지의 아이템 슬라이싱

# # print(f'{animals[3:]}')   # ['여우','늑대']
# # 인덱스 3부터 끝까지 아이템 슬라이싱

# # 뒤에서 2개의 아이템을 슬라이싱
# # print(f'{animals[len(animals)-2:]}')    # ['여우','늑대']

# # print(f'{animals[:-1]}')                # ['호랑이', '사자', '곰', '여우']
# # print(f'{animals[1:-1]}')               # ['사자', '곰', '여우']

# # print(f'{animals[:]}')                  # ['호랑이','사자','곰','여우','늑대'] 
# # print(f'{animals[::2]}')                # ['호랑이','곰,'늑대']    일종의 step  n-1칸씩
# # print(f'{animals[::3]}')                # ['호랑이', '여우']
# # print(f'{animals[::4]}')                # ['호랑이', '늑대']

# # quiz) 다음 리스트를 보고 답하시오.
# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# # 1. alphabet 리스트를 역순으로 출력하시오.

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# alphabet.sort(reverse=True)

# print(f'alphabet : {alphabet}')

# alphabet.reverse()

# print(f'alphabet : {alphabet}')

# # 2. 다음 요구사항에 맞게 alphabet 리스트를 슬라이싱하시오.

# '''
#  - 인덱스 2부터 5까지의 아이템을 출력하시오.
#  - 인덱스 0부터 4까지의 아이템을 출력하시오.
#  - 인덱스 3부터 7까지의 아이템을 출력하시오.
#  - 인덱스 5부터 끝까지의 아이템을 출력하시오.
#  - 인덱스 3부터 8까지의 아이템을 출력하시오.
# '''

# print(f'alphabet: {alphabet[2:6]}')    # ['c', 'd', 'e', 'f']
# print(f'alphabet: {alphabet[:5]}')     # ['a', 'b', 'c', 'd', 'e']
# print(f'alphabet: {alphabet[3:8]}')    # ['d', 'e', 'f', 'g', 'h']
# print(f'alphabet: {alphabet[5:]}')     # ['f', 'g', 'h', 'i', 'j']
# print(f'alphabet: {alphabet[3:9]}')    # ['d', 'e', 'f', 'g', 'h', 'i']

# # 뒤에서 4개 아이템을 출력하시오 
# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# print(f'alphabet: {alphabet[len(alphabet)-4:]}')  ['g', 'h', 'i', 'j']
# print(f'alphabet: {alphabet[-4:]}')    ['g', 'h', 'i', 'j']           # 역순으로 시작점을 계산
# print(f'alphabet: {alphabet[:-4]}')    ['a', 'b', 'c', 'd', 'e', 'f'] # 역순으로 끝나는 지점을 계산 

# print(f'alphabet: {alphabet[-7:-4]}')  ['d', 'e', 'f']          # [n : m-1]

# # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# # list에서는 음수가 역순을 의미한다

# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# print(f'alphabet: {alphabet}')  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# del alphabet[1:4]
# print(f'alphabet: {alphabet}') # ['a','f', 'g', 'h', 'i', 'j']


# print(animals[::-1])    # 전체 역순 출력

# 리스트[start : end : step]
# nums.sort()  반환값이 없다. 


#-------------------------------------------------------------

# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#  [3, 7, 1, 9, 5]

# nums = [3, 7, 1, 9, 5]
# nums.sort()                   
# print(f'maxNums: {nums[len(nums)-1]}')
# print(f'maxNums: {nums[-1:]}')

# print(max(nums))

# nums = [3, 7, 1, 9, 5]

# maxNum = 0
# for num in nums: 
#     if num > maxNum:
#         maxNum = num

# print(f'maxNums: {maxNum})

# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# userNum = int(input('숫자를 입력하세요: '))

# sum = 0

# for num in range(1, userNum + 1):
#     sum += num

# print(f'1부터 {userNum}까지의 합계: {sum}')
    

#  3. 리스트에 있는 숫자 중 짝수만 출력하기
#   [1,2,3,4,5,6]

# nums = [1,2,3,4,5,6]

# # print(f'짝수: {nums[1::2]}')

# for num in nums:
#     if nums % 2 ==0:

#         print(f'짝수: {nums}')


# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]

# nums = [5,1,7,3]
# nums.sort()
# print(f'nums: {nums}')

# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]

# nums = [5,1,7,3]
# nums.sort(reverse = True)
# print(f'nums: {nums}')

# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]

# nums = [10,20,30]
# for num in nums:
#     num+=num
#     average = num / len(nums)
# print(f'average: {average}')   

# nums = [10,20,30]
# total = 0
# average = 0

# for num in nums:
#     total += num

# average = total / len(nums)

# print(f'total: {total}')
# print(f'average: {average}')


# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)

# nums = [3, 7, 1, 9, 5]
# minNum = nums[0]

# for num in nums :
#     if num < minNum:
#         minNum = num     # (계속 변수 갱신할 때는 '=')
# print(f'minNum: {minNum}')       

# nums = [3, 7, 1, 9, 5]
# nums.sort()
# print(f'nums: {nums[0]}')
# print(f'nums: {nums[len(nums)-1]}')  # 최대값

# minNum = nums.pop(0)
# print(f'minNum: {minNum}')

# [str(i) for i in nums]


# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기 

# for num in range(1, 101):
#     if num % 3 == 0:
#         print(f'{num}은 3의 배수입니다.')

#     if num % 5 == 0:
#         print(f'{num}은 5의 배수입니다.')


# for num in range(1,101): 
#     if num % 3 == 0 and num % 5 == 0:
#         print(f'num: {num}')

# range (,)  따옴표 

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]


# userNum1 = []            # 변수명 

# while True:
#     userNum2 = int(input('입력:'))
#     userNum1.append(userNum2)
    
#     if userNum2 == 0:
        
#         break

# print(f'userNum: {userNum1}')       

nums = []

while True:
    userInputNumber = int(input('정수 입력:'))

    if userInputNumber == 0:
            break

    nums.append(userInputNumber)         # append   [list].append(value)  

print(f'nums: {nums}') 


