# 할당(대입) 연산자
# 할당 연산자는 변수에 값을 대입하는데 사용하는 연사자로 대입 연산자라고도 합니다. 

# #할당 연산자(=)

# num = 5 

# #복합 대입 연산자(+=, -=, /=, %=, //=, **=)

# num += 5

# num = num / 5

# num /= 5

# #num = num / 5

# num *= 5

# #num = num % 5

# num %= 5

# #num = num // 5

# num //= 5

# # num = num**5

# num **= 5


# num = 7

# num += 7

# print(num)


# quiz) 복리 계산기 만들기
# 회사원인 길동이는 예금 계획을 세우고 있습니다. 
# 은행에서 상담을 받아 보니 5년 정기 예금을 복리로 했을 때 가장 큰 목돈을 마련할 수 
# 있다고 알게 되었습니다.
# 길동이가 500만원씩 5년 만기인 정기 예금 상품에 가입했을 때
# 5년 후 받을 총 수령액을 계산해 봅시다(이자율: 연 5%)

regulMoney = int(input('정기 예금액: '))
year = int(input('연수: '))

rate = 0.05

# receivedMoney =  regulMoney * ((1 + rate) ** year)
receivedMoney =  round(regulMoney * ((1 + rate) ** year))


print(f'총 수령액: {receivedMoney:,}원' )

''' 해결방안

✅ 방법 1) round()로 반올림     <- ★★★추천★★★
receivedMoney = round(regulMoney * ((1 + rate) ** year))
print(f'총 수령액: {receivedMoney:,}원')

✅ 방법 2) int()로 소수점 버리기 (내림)
receivedMoney = int(regulMoney * ((1 + rate) ** year))
print(f'총 수령액: {receivedMoney:,}원')

✅ 방법 3) 소수점 2자리까지만 출력하기
receivedMoney = regulMoney * ((1 + rate) ** year)
print(f'총 수령액: {receivedMoney:,.2f}원')

출력이 예를 들면 6,381,407.81원 이런 식으로 됨.
'''

# myMoney = 5000000
# rate = 0.05

# #1년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# #2년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# #3년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# #4년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# #5년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# print(f'5년 후 총 수령액: {int(myMoney):,}원')

# myMoney = 5000000
# rate = 0.05
# years = 5

# result = myMoney * ((1+rate)**years)

# print(f'5년 후 총 수령액: {int(result):,}원')


# num = 3

# num = 30 

# print(f'num = {num}' )

# 비교 연산자

'''
a == b  a와 b는 같다. => True or False
a != b  a와 b는 같지 않다. => True or False 진짜 같지 않으면 T, 같으면 F
a > b   a가 b보다 크다. => True or False
a >= b  a가 b보다 크거나 같다. => True or False
a < b   a가 b보다 작다. => True or False
a <= b  a가 b보다 작거나 같다. => True or False
'''

# num1 = 10; num2 = 20

# print(num1 == num2)     # False
# print(num1 != num2)     # True
# print(num1 > num2)      # False
# print(num1 >= num2)     # False
# print(num1 < num2)      # True
# print(num1 <= num2)     # True

# # quiz) 범퍼카 탑승 가능 판별하기
'''
DW 놀이동산에서 범퍼카는 신장이 120cm 이상인 어린이만 탑승할 수 있습니다. 
사용자가 신장을 입력하면 범퍼카를 탑승할 수 있는지 여부를 출력하는 프로그램을 만들자. 
True: 탑승가능, False : 탑승 불가능
# '''
# height = int(input('어린이의 신장을 입력하세요.'))
# print(f'탑승 가능, {height >= 120}')

# 문자 vs 문자 비교 => 아스키코드 
# print('a'=='b')       #False
# print('a'<'b')        #True
# print('a'>'b')        #False
 
# 문자열을 비교할 시에는 *아스키코드를 적용하여 숫자로 치환된 후에 비교됨

# 문자열 비교
# str1 = 'hello'
# str2 = 'hello'
# print(str1 == str2)        #True
# print(str1 != str2)        #False
# ---------------------------------
# print(str1 < str2)         #False
# print(str1 > str2)         #False
# ---------------------------------

# str1 = 'hello'
# str2 = 'hello '
# print(str1 == str2)        #False
# print(str1 != str2)        #True



