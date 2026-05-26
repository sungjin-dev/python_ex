# data = float(input('수심을 입력하세요.' ))
# temperature = 20 - ((data // 10)* .7)
# print(f'temperature: {temperature}')

# deep = int(input('수심을 입력하세요.'))
# temperature = 20 - ((deep // 10) * 0.7)
# print(f' 수온 : {temperature}')


# speed = int(input('속도:'))
# time = int(input('주행시간:'))            

# distance = int(speed * time)    #str 문자열 상태에서는 곱 연산이 적용 안 되기 때문에 int casting

# print(f'주행거리: {distance}km')

#quiz
'''
A회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있습니다. 
그런데 단축 근무를 하게 되어 근무 시간이 줄게 되었다면
몇 대의 컴퓨터가 더 필요할까요?

근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램
'''

time = int(input('근무 시간을 입력하세요.'))

computer = 3*8 // time 
addComputer = 1 if (3*8 // time) > 0 else 0

totalcomputer = computer + addComputer
 
print(f'필요한 컴퓨터 수량: {totalcomputer}')




# time = int(input('근무시간을 입력하세요.'))   # 단축 근무 시간
# computer = 3 * 8 // time                   # 컴퓨터는 쪼갤 수 없기 때문에 몫만 구함
# addcomputer = 1 if (3*8 % time) > 0 else 0


# totalComputer = computer + addcomputer
# print(f'필요한 컴퓨터 개수 : {totalComputer}')

# maskPrice = 340 

# maskCnt = int(input('마스크 구매 개수'))
# totalprice = maskPrice * maskCnt

# cash = int(input('지불 금액:'))

# change = cash - totalprice
# print(f'거스름돈: {change}')



# 13시 30분 25초를 초로 나타내는 프로그램을 만드시오. 
# print(f'second : {25+(60*30)+(60*(60*13))}')

# 학생의 국어, 영어, 수학 점수를 입력하면 총점과 평균을 출력하는 프로그램을 만드시오. 

# kor = int(input('국어 점수:'))         #ctrl + alt 위아래 화살표
# eng = int(input('영어 점수:'))
# mat = int(input('수학 점수:'))

# totalScore = kor + eng + mat

# averageScore = totalScore / 3

# print(f'총점:{totalScore}, 평균: {averageScore} ')

# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램을 만드시오. 

# lowestTemp = float(input('밤 최저 기온:'))
# highestTemp = float(input('낮 최고 기온:'))

# diff = highest - lowest 

# print(f'일교차 : {diff}')


# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램을 만드시오(단. 1cm는 0.38inch로 한다).

# length = float(input('길이(cm)를 입력하세요.'))

# inch = length * 0.39 

# print(f'(inch: {inch})')



#* 편의점 거스름돈 계산 프로그램 만들어보기 

# money = int(input('받은 돈'))
# change = 
# 동전(500, 100, 50, 10)만 사용해서 거스름돈 계산

price = int(input("상품 가격을 입력하세요: "))
paid = int(input("받은 돈을 입력하세요: "))

change = paid - price

if change < 0:
    print("돈이 부족합니다.")
elif change == 0:
    print("거스름돈이 없습니다.")
else:
    print(f"총 거스름돈: {change}원")

    coin_500 = change // 500
    change %= 500

    coin_100 = change // 100
    change %= 100

    coin_50 = change // 50
    change %= 50

    coin_10 = change // 10
    change %= 10

    print("동전 개수 계산 결과")
    print(f"500원: {coin_500}개")
    print(f"100원: {coin_100}개")
    print(f"50원: {coin_50}개")
    print(f"10원: {coin_10}개")

    if change != 0:
        print(f"※ 10원 단위로 나누어 떨어지지 않는 금액: {change}원")

