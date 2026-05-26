# 조건문 (if문) 
'''
if 조건식:
    실행문  
'''
# if num > 10 : 
#     print('num은 10보다 크다')     # 실행문 앞에는 최소 1칸 이상. 0칸만 아니면 되지만 통일시켜야함) 

# num = 5
# if num > 10 :
#     print('num은 10보다 크다.')    #false라서 실행 x
#     print('num은 10보다 크다.')    #false라서 실행 x
# print('num은 10보다 크다.')        #조건문과 별개로 무조건 실행

'''
ifKeyword : 조건문을 선언하기 위한 키워드로 '만약 ~ 라면'의 뜻을 가지고 있다.
조건식: 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다. 
콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.  
실행문: 조건식의 결과가 참(True)인 경우 실행하는 명령문입니다. 
       조건식이 거짓(False)이면 실행문은 실행되지 않는다. 
'''

# 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램을 만들어 봅시다. 

# num = int(input('please input integer number'))

# if num > 10:
#     print(f'{num}은 10보다 크다.' )

# if num == 10: 
#     print(f'{num}은 10과 같다.' )
          
# if num < 10:
#     print(f'{num}은 10보다 작다.')
          
          
# quiz) 속도 위반 경고 하기
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램을 만들어봅시다. 


'''carspeed = int(input('현재 시속 : '))

limitSpeed = 50 

result = '속도 위반!!!' if carspeed > limitSpeed else '속도 준수!'

print(f'Result: {result}')'''
 
# carSpeed = int(input('자동차의 현재 속도 입력: '))
 
# if (carSpeed > 50):
#     print(f' 속도 위반!! ')

# if (carSpeed <= 50):
#     print(f' 안전 운행 중 ') 

     
# # if else 구문을 적용해도 된다 
 
# carSpeed = 40 

# if (carSpeed <= 50):
#     print(f' 안전 운행 중 ') 
#     print(f' 좋아요~~ ') 

# if (carSpeed <= 50): print(f' 안전 운행 중 ')  # 실행구문이 단 1개일 때는 개행 생략하고 바로 가능

# num = 5
# if num > 0 :
#     print('num은 0보다 크다.')

# print('num은 0보다 크다')          

# num = 5
# if num > 0 :
#     pass
# [pass]  조건문만 코딩하고 실행문은 미지수일 때 일단 에러를 스킵   -> pass 변수명 사용 x

# if ~ else 구문
# else : 그렇지 않으면~



# if myScore >= 90:

#     print('용돈 획득~')

# if myScore < 90:

#     print('빠따~')

# myScore = 70

# print(f'용돈 획득~' if 90 <= myScore else '빠따~')

# if myScore >= 90:

#     print('용돈 획득~')

# else :
#     print('빠따')


# if ~ elif 구문  - > 다중선택

'''
점수가 90점 이상이면 'A'출력
점수가 80점 이상~ 90점 미만이면 'B'출력
점수가 70점 이상~ 80점 미만이면 'C'출력
점수가 60점 이상~ 70점 미만이면 'D'출력
'''

# point = int(input('점수 입력: '))

# if point >= 90:
#     print('A')
# elif point >= 80:
#     print('B')
# elif point >= 70:
#     print('C')
# elif point >= 60:
#     print('D')
# else:
#     print('F')
 

# myScore = int(input('점수 입력'))
# if myScore >= 90:
#     print('A')

# elif myScore >= 80:
#     print('B')

# elif myScore >= 70: 
#     print('C')

# elif myScore >= 60:
#     print('D')

# else :                   # 나머지 
#     print('F')


# # if elif는 위에서부터 순차적으로 시행하기 때문에 잘못설계하면 제대로 걸러내지 못한다 

# myScore = int(input('점수 입력'))
# if myScore >= 90:
#     print('A')

# elif (myScore >= 70) and (myScore < 80):
#     print('C')

# elif (myScore >= 80) and (myScore < 90):
#     print('B')

# elif (myScore >= 60) and (myScore < 70) :
#     print('D')

# else :                 
#     print('F')

# 실수했을 때 복구하는 법

# quiz) 자동 주문 시스템 만들기 
'''
다국어를 지원하는 식당에서 사용할 자동 주문 시스템을 만들고자 합니다. 
1번을 누르면 한국어로, 2번을 누르면 영어로, 3번을 누르면 중국어로,
그 외 번호는 영어로 주문을 받는 프로그램을 만들어 봅시다. 
'''

#  1. 대한민국 , 2. USA   3. 中國

# 1: 주문하시겠습니까?
# 2: Would you like to order?
# 3: 您要点餐吗? 

# 그외, Would you like to order? 


# CONST_KOREA_NUMBER = 1          # 파이썬은 상수를 지원하지 않는다 즉 11로 입력을 해도 에러가 나지 않는다 다른 프로그램을 사용할 시에는 상수 선언을 하고 나면 에러가 남                   
# CONST_USA_NUMBER = 2
# CONST_CHINA_NUMBER = 3 

# selectedNumber = int(input('1. 대한민국  2. USA   3. 中國 '))

# if  selectedNumber == KOREA_NUMBER :
#     print('주문하시겠습니까?')

# elif selectedNumber == USA_NUMBER :
#     print('Would you like to order?')

# elif selectedNumber == CHINA_NUMBER :
#     print('您要点餐吗？')

# else : 
#     print('Would you like to order?')

# quiz ) 국가재난지원금 수령액 조회하기
'''
다음은 가구 인원수에 따른 국가재난지원금 수령액을 안내하는 프로그램입니다.
표를 참고하여 프로그램을 만들어봅시다. 
1인 가구 : 400,000원
2인 가구 : 600,000원
3인 가구 : 800,000원
4인 이상 가구 : 1,000,000원
'''

# famailyNum = int(input('가구 인원수: '))

# single = 1
# twoPeople = 2
# threePeole = 3

# if famailyNum == single:
#     print('400,000원')
# elif famailyNum == twoPeople:
#     print('600,000원')
# elif famailyNum == threePeole:
#     print('800,000원')
# else:
#     print('1,000,000원')


# familyNumber = int(input('가구 인원수 :'))

# SINGLE = 1
# TWO_PERSON = 2
# THREE_PERSON = 3

# if familyNumber == SINGLE:       # 1= > ONE_PERSON 이런식으로 상수화 하는 작업 -> 리펙토링 refactoring 
#     print('400,000원')

# elif familyNumber == TWO_PERSON:
#     print('600,000원')

# elif familyNumber == THREE_PERSON:
#     print('800,000원')

# else :
#     print('1,000,000원')

'''
다음 요구사항을 충족하는 프로그램을 if~elif문을 이용해서 만드시오. 
 - BMI 지수를 입력한다 
 - BMI 지수가 90이하면 '저체중'을 출력한다.
 - BMI 지수가 90초과 ~ 110 이하면 '정상 체중'을 출력한다. 
 - BMI 지수가 110초과 ~ 120이하면 '과체중'을 출력한다.
 - BMI 지수가 120초과 ~ 140이하면 '비만'을 출력한다. 
 - BMI 지수가 140초과면 '고도 비만'을 출력한다. 
'''

# integer = float(input('BMI 지수:'))

# if integer <= 90:
#     print('저체중')

# elif 90 < integer <= 110  :
#     print('정상 체중')

# elif 110 < integer <= 120:
#     print('과체중')

# elif 120 < integer <= 140:
#     print('비만')

# else :
#     print('고도 비만')

# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 있는데 이를 중첩 조건문이라고 합니다 
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝인지 구분하자!

# myInteger= int(input('정수 입력:'))
# if myInteger > 0:
#     print('양수')
#     if myInteger % 2 == 0:
#         print('짝수!')

#     else : 
#         print('홀수!')

# else:
#     print('음수!')

# quiz) 짝수/홀수를 판별하는 프로그램을 만들자!

# num = int(input('사용자야~~ 양의 정수 입력해주라~'))
# if num > 0:
#     if num % 2 == 0 :
#         print('짝수!!!!')
#     else : 
#         print('홀수!!!!')                                #  alt shift 위아래 -> 복사 , alt 행 이동 
# else:
#     print('입력한 정수는 0 또는 음수입니다.')               #  ctrl + shift + k

# 출생연도 끝자리(endBirthYear)와 나이(age)를 입력하면 다음 요구사항에 맞춰
# 마스크 구매 가능한 요일을 출력하는 프로그램을 만드시오. 
#  - 공적마스크 판매 관련해서 출생연도 끝자리를 이용한 5부제를 다음과 같이 실시한다.

#  - 1, 6 => 월
#  - 2, 7 => 화
#  - 3, 8 => 수
#  - 4, 9 => 목
#  - 5, 0 => 금
# - 만 65 이상 어르신은 언제든지 구매 가능하다. 


# endBirthYear = int(input('출생연도 끝자리 : '))

# age = int(input('나이 : '))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월')
#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화')
#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수')
#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목')
#     elif endBirthYear == 5 or endBirthYear == 0:
#         print('금')
# else :
#     print('만 65 이상 어르신은 언제든지 구매 가능')

 # and 인지 or 인지 명확히 구분하자. 


# endBirthYear = int(input('출생연도 끝자리 입력:'))
# age = int(input('나이 입력:'))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월요일에 구매 가능')

#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화요일에 구매 가능')

#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수요일에 구매 가능')

#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목요일에 구매 가능')

#     elif endBirthYear == 5 or endBirthYear == 0:
#         print('금요일에 구매 가능')
# else :
#     print('언제나 구매 가능합니다.')
    

   # endBirthYear == 1 or 6 파이썬에서는 (endBirthYear == 1) or (6) 이런식으로 해석해서 True or False 이렇게 나옴

   # -> 축약한다면 endBirthYear in (1, 6)  -> 이런식으로 하는게 가장 바람직

# 날짜 관련 모듈: datetime

# import operator 

# from datetime import datetime 

# # 현재 일 구하기
# print(datetime.today().weekday())        #day weekday(함수) month

'''
오늘 날짜를 구한다. 
차량 번호 4자리를 입력한다
2부제에 따라 오늘 날짜와 차량번호를 비교해서 입차 가능여부를 출력
번호가 짝수면 짝수일자에, 번호가 홀수면 홀수일자에 가능
'''

# from datetime import datetime
# today = datetime.today().day

# carNum = int(input('차량번호 4자리 : '))

# if carNum % 2 == today % 2 :
#     print('입차 가능')

# else:
#     print('입차 불가능')


# result = '입차 가능' if carNum % 2 == today % 2 else '입차 불가능'
# print(result)    


    

# carNum = int(input('차량 번호 4자리 입력:'))

# from datetime import datetime
# today = datetime.today().day 
#   
'''datetime.today()
➡️ 오늘 날짜/시간 정보를 가진 datetime 객체를 만들어 줌
예: 2026-05-10 12:34:56
.day
➡️ 그 객체에서 "일(day)" 값만 꺼냄
예: 10'''

# if carNum % 2 = 0 :
#     print('번호가 짝수인 차량')

#     if today % 2 = 0:
#         print('귀하의 차량은 입차 가능합니다')

#     else: 
#         print('귀하의 차량은 입차 불가합니다')

# elif carNum % 2 != 0:
#     print('번호가 홀수인 차량')
#     if today % 2 != 0:
#         print('귀하의 차량은 입차 가능합니다')
#     else:
#         print('귀하의 차량은 입차 불가합니다.')
     
 



# from datetime import datetime
# today = datetime.today().day

# carNum = int(input('차량 번호 4자리 입력: '))


# print(f'오늘 날짜: {today}일')             # 오늘 날짜 

# if carNum % 2 == 0:
#     print('번호가 짝수인 차량')

#     if today % 2 == 0:
#         print('귀하의 차량은 입차 가능합니다')

#     else:
#         print('귀하의 차량은 입차 불가합니다')

# elif carNum % 2 != 0:
#     print('번호가 홀수인 차량')

#     if today % 2 != 0:
#         print('귀하의 차량은 입차 가능합니다')

#     else:
#         print('귀하의 차량은 입차 불가합니다.')
    

# if today % 2 == 0:
#     print('오늘 입차 : 번호가 짝수인 차량')
# else:
#     print('오늘 입차 : 번호가 홀수인 차량')

# if today % 2 == carNum % 2:
#     print('귀하의 차량은 입차 가능합니다')
# else:
#     print('귀하의 차량은 입차 불가능합니다')


# 다음 표는 심장 정지 환자에게 자동 심장 충격기를 사용했을 때 최초로 시행한 시간에 따른 환자의 생존율을 나타냅니다. 
# 표를 보고 장비를 사용하기까지 걸린 시간을 입력하면 생존율이 출력되는 프로그램
#  
#
# spendTime = int(input('장비를 사용하기까지 걸린 시간(초):')) 


# if  spendTime <= 60:
#     print('생존율 : 85%')

# elif spendTime <= 120:
#     print('생존율 : 76%')

# elif spendTime <= 180:
#     print('생존율 : 66%')

# elif spendTime <= 240:
#     print('생존율 : 57%')

# elif spendTime <= 300:
#     print('생존율 : 47%')

# else :
#     print('생존율 25% 미만')

'''
200kwh이하  기본요금 910원, 단가 : 99.3원, 
400kwh이하  기본요금 1600원, 단가 : 187.9원
그 이상 기본요금 7300원, 단가 : 280.6원

전기사용량(kwh)에 따른 요금을 계산하시오 
'''

spentLight = int(input('전기 사용량(kwh) : '))

basicFee1 = 910
basicFee2 = 1600
basicFee3 = 7300

personalFee1 = 99.3
personalFee2 = 187.9
personalFee3 = 280.6

if spentLight <= 200:
    totalFee = basicFee1 + (personalFee1 * spentLight)
elif spentLight <= 400:
    totalFee = basicFee2 + (personalFee2 * spentLight)
else:
    totalFee = basicFee3 + (personalFee3 * spentLight)
   
print(f'요금: {totalFee:,}원')
    

# spendlight = int(input('전기 사용량(kwh)을 입력하세요.'))

#total = spendlight * 단가 + 기본요금 

# if spendlight <= 200:
#     print('기본요금: 910원')
# elif spendlight <= 400:
#     print('기본요금: 1600원')
# else :
#     print('기본요금: 7300원')
    
# if spendlight <= 200:
#     print('단가: 99.3원')
# elif spendlight <= 400:
#     print('단가: 187.9원')
# else :
#     print('단가: 280.6원')

# if spendlight <= 200:
#     print(f'전기요금 : {spendlight*99.3+910}')
# elif spendlight <= 400:
#     print(f'전기요금 : {spendlight*187.9+1600}')
# else :
#     print(f'전기요금: {spendlight*280.6+7300}')


# # 어린이의 신장을 입력하면 놀이기구 탑승 여부가 출력되는 프로그램
#  120<= 신장 <= 160

# height = int(input('신장 입력'))

# if 120 <= height <= 160:
#     print('탑승 가능')  
# else :
#     print('탑승 불가')

# testScore = int(input('시험점수 입력'))
# result ='success' if testScore >= 85 else 'fail' 

# # 다음은 컴퓨터와 사용자가 '난수를 이용한 가위 바위 보 게임' 을 하는 모습이다. 실행 결과를 보고 프로그램을 완성하시오. 

# import random                  # 난수 발생 모듈

# ranNum = random. randint(1, 4)          # 1~3까지의 정수 중에서 하나는 발생한다. 

# myNum = int(input('1.가위 2.바위 3.보 를 선택하세요'))

# # if (ranNum == 1 and myNum == 1) or (ranNum == 1 and myNum == 1) or (ranNum == 1 and myNum == 1):
# #     print('무승부')

# myNum = int(input('1.가위 2.바위 3.보 를 선택하세요'))

# if ranNum == myNum:
#     print('무승부')

# elif (ranNum == 1 and myNum == 2) \
#       or \
#      (ranNum == 2 and myNum == 3) \
#       or \
#      (ranNum == 3 and myNum == 1):
#      print('사용자 승')

# elif (ranNum == 1 and myNum == 3) \
#      or \
#      (ranNum == 2 and myNum == 1) \
#      or \
#      (ranNum == 3 and myNum == 2):
#      print('컴퓨터 승')
    
'''
사용자가 입력한 문자 메시지 길이에 따라서 SMS 또는 MMS의 발송을 결정하는 프로그램을 완성하시오
(단, 메시지 길이가 50이하면 SMS 발송, 그렇지 않으면 MMS를 발송한다)
'''

# str = 'hello'
# print(f'str: {str}')                          # hello
# print(f'str\'s length: {len(str)}')              # 5

# useMessage = input('메시지를 입력하세요.')
# MsgLen = len(useMessage)

# if MsgLen <= 50:
#     print('SMS 발송!')
# else:
#     print('MMS 발송!')
      