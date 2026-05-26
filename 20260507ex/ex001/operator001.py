#나눗셈 연산자(/)
# print(10/2)             # 5.0  실수 형태로 나옴
# print(3.14/.5)          # 0을 생략해서 쓰이긴 함

# num1 = 100
# num2 = 10
# print(f'num1/num2 = {num1 / num2}')

# quiz) 신체질량지수(BMI) 구하기
# 몸무게와 신장을 입력하면 신체질량지수(BMI)를 계산해주는
# 프로그램을 만들어봅시다(BMI = 몸무게(kg)/신장의 제곱(m2))


# weight = float(input('몸무게(kg):'))
# height = float(input('신장(m):'))

# # bmi = weight / (height * height) #(= height**2)
# bmi = weight / (height **2) 


# print(f'BMI: {bmi}')


# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m) '))

# bmi = weight / (height * height)

# print(f'BMI: {bmi}')

# print(f'BMI: {bmi:.2f}')      #소수점 2번째 자리까지

#숫자 0을 어떤 수로 나누어도 결과는 항상 0이다. 
# print(0 / 123)        # 0 

# #어떤 숫자를 0으로 나눌 수 없다. 에러
# print(10 / 0)       #runtime error 

#나머지(%), 몫, 거듭제곱
# print(10 % 2)
# print(10 % 3)

#quiz) 홀짝 게임하기
# 주먹 쥔 손을 상대방에게 내밀며 손 안에 동전 개수가 홀수인지 짝수인지 맞추는 게임입니다.
# 손 안에 동전 개수를 입력하면 짝수는 0, 홀수는 1을 출력하는 프로그램을 만들어봅시다. 
# inputData = int(input('손 안에 동전 수를 입력하세요.'))
# result = inputData % 2 
# print(result)

# 몫만 구할 때는 //

# print(10 // 3)       # 3 
# print(6 // 2)        # 3   정수로 나오네? 몫만 구하는거라 어차피 몫 나머지는 날아감

# quiz) 빵을 나누어 줄 수 있는 학생 수 구하기
# 길동이는 97개의 빵을 3개씩 같은 반의 친구들에게 나누어 주려고 합니다. 
# 최대 몇 명에게 나누어 줄 수 있는지 구하고, 남는 빵의 개수도 구해봅시다. 

bread = int(input('빵의 개수: '))

breadCnt = 3

maxallocation = bread // breadCnt
rest = bread % breadCnt 

print(f'빵을 나누어 줄 수 있는 학생 수: {maxallocation}, 남는 빵: {rest}')

# bread = 97
# breadCnt = 3
# maxFriendCnt = bread // breadCnt
# print(f'빵을 나누어 줄 수 있는 학생 수: {maxFriendCnt}')

# restBreadCnt = bread % breadCnt
# print(f'남는 빵 개수: {restBreadCnt}')

# 거듭제곱(**)
# print(2**2)      #4
# print(2**3)      #8 
# print(2**10)     #1024

# quiz) 전염병 예상 감염자 수 구하기
# 보건 당국은 전염병의 감염 확산 추세를 파악한 결과, 
# 하루에 한 사람이 한 명씩 감염시키는 것으로 나타났습니다.
# 확진자 한 사람이 나올 경우 30일 이후에 몇 명의 감염자가 나오는지 계산해봅시다. 


# man = 2 
# date = 30

# total = man ** date

# print(f'{date}일 이후 예상 감염자 수: {total}')

