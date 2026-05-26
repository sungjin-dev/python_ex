# 1. 회원가입 2.프로그램 종료

# flag = True
# members = {}

# while flag:

#     userInputNum = int(input('1. 회원가입   2.프로그램 종료'))
#     if userInputNum == 1:
#         id = input('아이디:')
#         pw = input('비밀번호')
#         members[id] = pw               # 아이디는 중복되면 안 되니까 key값으로 쓴다
#     elif userInputNum == 2:
#         flag = False

#         for key in members.keys():
#             print(f'ID: {key}, PW: {members[key]}')
# print()

# 3학점인 과목을 모두 5학점으로 변경하는 프로그램

# classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 'Java':'5학점', 'Javascript':'3학점'}

# for key in classes.keys():           # for key in classes
#     if classes[key] == '3학점':            # 이건 true or false
#         classes[key] = '5학점'             #  변수 
# print(classes)
'''
members = {
    '2019-052001':['박찬호', '25', 'M', '010-1234-5678', '헬스' '수영', 0],
    '2019-052004':['박용택', '65', 'M', '010-9012-3456', '수영', 50],
    '2019-052003':['박세리', '70', 'W', '010-7890-1234', '아쿠아로빅', 50],             
}
'''

# 전체 회원 정보 출력
# for key in members:
#     print(f'회원번호: {key}, 회원정보: {members[key]}')

# print('-'*30)

# # 전체 회원 정보를 출력을 하는데, 이 때 회원의 '이름'과 '성별'만 출력을 하자

# for key, value in members.items():
#     print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]},{value[1]}')

# members = {
#     '2019-052001': {
#         '이름': '박찬호',
#         '나이': 25,
#         '성별': 'M',
#         '연락처': '010-1234-5678',
#         '이용서비스': ['헬스', '수영'],                 # 따옴표 따로 따로 해줘야함
#         '할인율': 0
#     },                    #컴마 있어야함
#     '2019-052004': {
#         '이름': '박용택', 
#         '나이': '65', 
#         '성별': 'M', 
#         '연락처': '010-9012-3456',
#         '이용서비스': ['수영'],
#         '할인율': 50,
#     },
#     '2019-052003':{
#         '이름': '박세리', 
#         '나이': 70,
#         '성별': 'W', 
#         '연락처': '010-7890-1234',
#         '이용서비스': ['아쿠아로빅'],
#         '할인율': 50,   
#     }              
# }

# # 회원정보를 출력하는데 이름 성별 이용서비스 그리고 이용서비스개수 만 출력을 하자!

# for key, value in members.items():
#     print(f'회원번호: {key}, 회원정보(이름, 성별: {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')

# 
# vagetables = {
#     '당근': {
#         '입고량' : 11,
#         '소비량' : 1,
#         '재고량' : 0,
#     },
#     '건대추': {
#         '입고량' : 100,
#         '소비량' : 10,
#         '재고량' : 0,
#     },
#     '대파': {
#         '입고량' : 20,
#         '소비량' : 1,
#         '재고량' : 0,
#     },
#     '애호박': {
#         '입고량' : 3,
#         '소비량' : 1,
#         '재고량' : 0,
#     },
#     '부추': {
#         '입고량' : 10,
#         '소비량' : 1,
#         '재고량' : 0,
#     },
# }   

# current = 0 

# for key, value in vagetables.items():
#     current = value['입고량'] - value['소비량']
#     value['재고량'] = current
#     print(f"채소명: {key},\t : 입고: {value['입고량']},\t 소비: {value['소비량']},\t 재고량 : {current}")


# 용돈 기입장 

allowance = {
    '월': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '화': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '수': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '목': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '금': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '토': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '일': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
}   

totalIncome = 0
totalOutcome = 0
totalBudget = 0

while True:
    selectedNum = int(input('1. 기입   2. 종료'))
    if selectedNum == 2 :
     
        print('종료합니다.')
        print(allowance)
        break
    
    days = str(input('요일 입력:'))     
    income = int(input('받은 용돈:'))
    outcome = int(input('지출 금액:'))
    budget = income - outcome 
    

    if days in allowance:
            
            allowance[days]['수입'] = income
            allowance[days]['지출'] = outcome
            allowance[days]['잔액'] = budget

            totalIncome += income
            totalOutcome += outcome 
            totalBudget += income - outcome   
    else:
        print('다시 입력해 주세요')
    
    print(f" {days} :  수입: {totalIncome}, 지출 :{totalOutcome}, 남은 돈: {totalBudget}")

   
# 결론부터 말씀드리면, break는 "지금 당장 즉시 탈출!", 
# flag = False는 "이번 바퀴까지만 돌고 다음에는 들어오지 마!"라는 뜻입니다.

'''
# : 용돈 기입장 :::::
from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False '''



