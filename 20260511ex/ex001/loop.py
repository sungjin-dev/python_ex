# 반복문(for문 & while문)

# for문: ~하는 동안  ==> 횟수에 의한 반복
'''
for 변수 in 범위:
    실행구문
'''
# 1~10까지의 정수를 출력
# for 변수 in range(시작값, 끝값, 단계):
# 1 ~ n까지의 정수 range(1, (n+1), 1)    

# for num in range(1, 11, 1):           # IT에서는 끝값에 +1을 추가한다 
#     print(f'{num}: hello')
#     print(f'hello')


'''                 「  수열 규칙 
for i in range(1.11.1):                  * i 는 변수명
 (item)        L iterable (반복가능한 객체) 반복 가능한 데이터 집합
    print(i)
'''    

# 0부터 10까지의 정수를 출력

# for num in range(11):
#      print(f'num : {num}')

# for num in range(0,11,1):             # in꼭 넣어주고 . 아니라 ,이다 
#     print(f'num : {num} ')

# range() 간략화 - 단계 1인 경우 단계를 생략할 수 있다. 
# for num in range(0,11):              
#     print(f'num : {num}')

# # range() 간략화 - 단계가 생략되고 시작이 0이면 시작도 생략 가능하다. 
# for num in range(11):       # 단계가 생략된 상태에서(조건) 결과적으로 range(0,11,1) == range(11) 
#     print(f'num : {num}')


# quiz) 2-8 사이의 짝수

# for num in range(2,9,2):         # (2,10,2) -> 이렇게 해도 결과는 같다   stop = 9 (끝값, 포함 안 함)
#     print(f'num: {num}')

# for num in range(1,16):
#     if num % 2 == 0:
#         print(num)

# for num in range(1,16):
#      if num <= 8 and (num % 2 == 0):
#           print(f'num: {num}')
         

# 등비 수열  (참고)
# num = 2
# for _ in range(5):
#     print(num)
#     num *= 2

'''✅ for문 변수(num)를 값 계산용으로 쓰면 안 되고
반복용 변수랑 계산용 변수는 분리해야 한다.'''

# quiz ) 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기

# Usernum = int(input('입력하고 싶은 횟수 :'))     

# for num in range(Usernum):              # 생략된거면 0 ~5 : 0 1 2 3 4 
#     print(f'메일 발송!')

# 1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기


# for num in range(1,11):
#     if num % 3 == 0:
#         print(f'3의 배수')
#     else : 
#         print(f'num: {num}')


# for i in range(1, 11):
#     print('3의 배수!' if (i % 3 == 0) else i)    # 짧은 건 이렇게 하는게 좋다   

# 사용자가 원하는 구구단을 입력하면 해당 구구단을 출력하자!

# dan = int(input('단 :'))

# for num in range(1,10):
#     print(f'{dan} x {num} = {dan * num}')   # 계산식은 여기다 묶어야 한다 {} 여기 안에

# quiz) 1 ~ 10까지 정수의 합 출력하기


# for num in range(1,11):
#     print((num*(num + 1))/2)

# userInputInteger = int(input('정수 입력:'))

# sum  = 0
# for num in range(1, userInputInteger + 1):
#     sum += num
# print(f'1부터 {userInputInteger}까지의 합: {sum}')

# quiz) for문을 이용해서 1~100까지 정수 중에서
# 3과 7의 공배수와 최소공배수를 출력하시오. 

# minNum = 0        # 아직 최소공배수를 구하지 못했기 때문에 비워두는 것(*임시값)

# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수: {num}')
#         if minNum == 0: 
#               minNum = num   # 저장은 = 이걸로 해야함
             
# print(f'최소 공배수: {minNum}')  

'''
🔸 if minNum == 0:

"minNum이 아직 비어있다면(아직 저장한 적 없다면)"

🔸 minNum = num

"이번에 찾은 공배수(num)를 최소 공배수로 저장해라"
'''

# 그래서 처음에 찾은 21이 minNum에 저장되고 그 이후 42는 minNum != num 이기 때문에
#if minNum == 0:   # False (minNum은 21임)
#    minNum = 42   # 실행 안 됨


# minNum = 0

# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수: {num}')
#         if minNum == 0: minNum = num              # minNum = num -> 처음에 21로 지정이 되고 나면 21 != 42 이런식으로 
#                                                   # 결과적으로 첫번째 최소공배수만 출력이 된다
#                                                   #  
# print(f'3과 7의 최소공배수: {minNum}')

'''
C에서 상수
const int minNum = 0;
minNum = 21; // 오류
Java에서 상수
final int minNum = 0;
minNum = 21; // 오류

java나 C에서도 이런 식으로 변수 지정을 통해 초기화하고 코딩가능
'''

# for num in range(1,101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수 : {num}')


'''minNum = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 7 == 0:
        print(f'3과 7의 공배수: {num}')
        if minNum == 0: minNum = num

print(f'3과 7의 최소공배수: {minNum}')
'''

# range() 함수 정리 

# 홀수의 경우 그냥 range(1, 11, 2) 이런식으로 뒤에 단계에 2를 넣어서 처리한다 
                  #  시작    단계
# 단계를 생략하면 데이터를 1로 생각 
# 시작도 생략 가능하다. 시작을 '0'으로 설정

''''단계' 감소   range(10,0,-1)  10 ~ 1        
 
단계가 증가하는 경우에는 끝나는 숫자 - 1            # 반복하다가 마지막 전 숫자까지
단계가 감소하는 경우에는 끝나는 숫자 + 1
'''

# 문자열을 이용한 for문 (****)
'''
지금까지 이터러블에 range()함수를 이용한 예를 살펴봤습니다. 
그런데 이터러블에는 다음과 같이 문자열도 이용할 수 있습니다. 
'''

# for ch in 'Hello   ':
#     print(f'ch: {ch}')

# for num in range(1, 51):
#     if num % 7 == 0 :
#         print(f'num: {num}')


# while문 : ~하는 동안 ==> 조건에 의한 반복 (조건식의 결과에 따라 반복 실행)

# num = 1

# while num <5:
#     print(num)
#     num += 1     # 그니까 여기서 저장  num = num +1

# num = 1                 # => 무한루프에 빠지게 됨. 
# while num <5:
#     print(num)
#     # num += 1


# num = 1

# while num <= 10:
#     print(f'num: {num}')
#     num += 2


# quiz) 1~30 정수 홀수 짝수 구분해서 출력

# num = 1

# while num < 31:
#     if num % 2 == 0:
#         print(f'짝수: {num} ')
#     else :
#         print(f'홀수: {num}')
#     num += 1

# num = 1

# while num < 31:

#     if num % 2 == 0 :
#         print(f'{num}은 짝수!')

#     else:
#         print(f'{num}은 홀수!')
        
#     num += 1

# quiz ) 구구단 3단 출력하기 by while문

# num = 1 

# timesTables = int(input('구구단 숫자를 입력하세요.'))

# while num < 10:
#     print(f'{timesTables} x {num} = {timesTables * num}' )
#     num += 1

# num = 1

# timesTables = int(input('구구단 숫자를 입력하세요.'))

# while num < 10:
#         print(f'{timesTables} x {num} = {timesTables * num}')

#     num += 1

# quiz) 구구단 전체(2단 3단 4단 .... 9단)

# num1 = 1

# while num1 < 10:
#     line = ''
#     num2 = 2
#     while num2 < 10:
#         line += f'{num2}x{num1} = {num2 * num1}\t'
#         num2 += 1
#     print(line)
#     num1 += 1

# num1 = 1
# while num1 < 10:
#     num2 = 2
#     while num2 < 10:
#         print(f'{num2}x{num1}={num2*num1:2d}', end= '   ')   #end는 print()에서만 쓸 수 있다 
#         num2 += 1
#     print()
#     num1 += 1

# 프롬프트 배열이 깨지는 이유는 숫자 자리수가 달라 간격이 다르기 때문임. 
# \t는 탭이고 8칸 단위로 다음 위치로 점프

'''num1 = 1

while num1 < 10:
    line = ''
    num2 = 2    
    while num2 < 10:
        line += f'{num2}x{num1}={num2*num1:2d}   '  # {num2*num1:2d}
        num2 += 1
    print(line)
    num1 += 1

num1 = 1

while num1 < 10:
    num2 = 2
    while num2 < 10:
        print(f'{num2} x {num1} = {num2*num1:2d}', end='   ')
        num2 += 1
    print()
    num1 += 1   

print()는 출력할 내용은 없고, 그냥 엔터만 쳐주는 역할

'''

'''
dan = 1

for dan in range (1,10):
     
    num = 1                               
    
    while num < 10:
            print(f'{dan} x {num} = {dan * num}')

            num += 1

         
num = 1
while num < 10:
    for number in range(1, 10):
        print(f'{num} X {number} = {num * number}')
    num += 1
'''

# num1 = 2
# while num1 < 10:

#     num2 = 1
#     while num2 < 10 :
#          print(f'{num1}x{num2} = {num1*num2}')
#          num2 += 1
#     print(f'------------------')
#     num1 += 1

# num1 = 2
# while num1 < 10:

#     num2 = 1
#     while num2 < 10 :
#          print(f'{num1}x{num2} = {num1*num2}', end = '')
#          num2 += 1
#     num1 +=1

# num1 = 1                                        # 구구단 뒷자리
# while num1 < 10:
     
#      num2 = 2  
#      str = ''                                    # 구구단 앞자리      line = '' 으로 대체 가능(권장)
#      while num2 < 10:
#         str += f'{num2}x{num1} = {num2 * num1}\t'
#         num2 += 1

#      print(str)
        
#      num1 += 1

 
# num1 = 1
# while num1 < 10:

#     num2 = 2
#     str = ''
#     while num2 < 10 :
#         str += f'{num1}x{num2} = {num1 * num2}\t'
#         num2 += 1
#     print(str)

#     num1 += 1         # 위치가 중요함

#      -> 여기서 num1 += 1은 print(str)과 같은 줄 맞춤(들여쓰기 레벨)   

'''
for num1 in range(1, 10):      # 뒤에 곱해지는 수 (1~9)

    line = ''                  # 한 줄 저장할 문자열

    for num2 in range(2, 10):  # 앞단 (2~9단)
        line += f'{num2}x{num1} = {num2 * num1}\t'

    print(line)
'''     

# quiz ) 0~100 3,8의 최소공배수 




 
# num = 1                      # 반복문의 시작(초기값)       곱셈의 경우는 0~ 이더라도 1로 지정
# minNum = 0                   # 최소공배수

# while num <= 100:

 

#     if num % 3 == 0 and num % 8 == 0 :
#         print(f'3과 8의 공배수 : {num}')           # 공배수 출력

#                                                  # 24  최소공배수 도출하는 방식  
#         if minNum == 0:
#             minNum = num            -> 사실 이말을 풀어쓰면 비어있으면 값을 저장하라는거임. 

#         num +=1 
        
# print(f'3과 8의 최소공배수: {minNum}')
     

# 현재 기온은 30도이고 희망온도를 입력해서 

# for 구문

# currentP = 30.0 

# targetP = float(input('희망 온도:'))

# for num in range(1000): 
#     currentP -= 0.1
#     if targetP == currentP: break



currentT = 30.0

num = 1

targetT = float(input('희망 온도:'))

while currentT > targetT :
     currentT -= 0.1
     if currentT == targetT :
         print(f'현재온도: {currentT}')
         break
     num += 1

currentT = 30.0
num = 0

targetT = float(input('희망 온도: '))

while currentT > targetT:
    currentT = round(currentT - 0.1, 1)
    num += 1

print(f'현재온도: {currentT}')
print(f'횟수: {num}')              # 어차피 딱 같아질 때 멈추기 때문에 굳이 TRUE break 구조를 사용할 필요가 없다


currentT = 30.0
num = 0

targetT = float(input('희망 온도: '))

while currentT > targetT:
    currentT -= 0.1
    num += 1
    while True:
        currentT == targetT 
        break
    num += 1   
print(f'num: {num}')

currentT = 30.0
num = 0

targetT = float(input('희망 온도: '))

while currentT > targetT:
    currentT -= 0.1
    num += 1

    # 만약 0.1 줄인 결과가 targetT보다 작아지면 targetT로 맞추기
    if currentT < targetT:
        currentT = targetT
        break

print(f'num: {num}')
print(f'최종 온도: {currentT}')

# while currentT - targetT > 0.000001:  보통은 이렇게 함


    
# 반복문 내 실행 제어(continue, break)
# continue:
# 반복문에 continue 키워드를 사용하면 이후 실행을 생략하고 다시 '반복문의 처음'으로 돌아갑니다. 
    
# continue를 이용해서 1부터 10까지의 정수 중 홀수만 출력하는 프로그램을 만들어 봅시다. 

# for num in range(1, 11):
#     if num % 2 == 0:
#         continue
#     print(f'num: {num}')     

# count = 1

# for num in range(10):    # 0~9 
#      print(f'num : {num}')
#      count += 1
#      if count >=5:             # 4번 실행
#           break
            

# break:
# 반복문에서 break 키워드를 만나면 ' 실행을 중단하고 반복문을 빠져' 나옵니다. 
# 1부터 10까지의 정수를 더하되, 결과가 30이상이 될 때 정수를 찾는 프로그램

num = 1
sum = 0    # sum은 일단 미지수로 설정

while num < 11:
    sum += num
    if sum >= 30:
        print(f'num: {num}') 
        break       # f ''  크게 보면 이런 구조임
    num += 1        # if 밖에 두는걸 추천
print(f'sum : {sum}') 

# break는  if를 끝내는 게 아니라 while문을 즉시 종료


# num = 1
# sum = 0

# while num < 11:
#     sum += num
#     if sum >= 30:
#         print(f'num : {num}')
#         break
#     num += 1                 ->> 이거 위치가 아주 중요함
# print(f'sum: {sum}')        # 55


❌ 만약 num += 1을 break 위로 올리면?

예를 들어 이렇게 바꾼다고 해보자:

sum += num
num += 1

if sum >= 30:
    print(num)
    break

이러면 문제 발생.

왜 문제냐? 예시로 설명

원래는

num=8일 때 sum이 36이 돼서 멈춰야 함

근데 위처럼 하면 num=8을 더한 직후에

num이 바로 9로 바뀌어버림

그래서 출력할 때는 num=9가 출력됨.

즉 실제로는 8을 더해서 30 넘겼는데
출력은 9라고 나오는 이상한 결과가 생김.

# for ~ else 키워드 

'''
for문에 else 키워드를 사용하는 경우, else 이하의 구문은 for문의 반복 업무를 모두 완료하고 난 후 실행
'''

# 1부터 5까지 정수를 출력하고 반복문이 끝나면 완료 메시지를 출력하자!

# for num in range(1, 6):
#      print(f'num: {num}')

# else: 
#      print('완료!')

# # pass 키워드 

# for num in range (1, 10):
#      pass

# quiz)
'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어 보자. 
단, 가로 길이는 1부터 2의 배수로 증가하고
세로 길이는 1부터 3의 배수로 증가하면,
삼각형의 넓이가 150보다 크면 프로그램을 종료한다. 
# '''

# count = 1

# maxArea = 150

# while True :                     
#      result = ((count * 2) * (count * 3)) / 2
#      if result > 150: break
#      print(f'삼각형의 넓이는: {result}')
#      count += 1


