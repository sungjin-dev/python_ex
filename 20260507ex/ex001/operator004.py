# 모듈
'''
모듈이란 특정 기능을 모아놓은 파일로 모듈을 이용하면 우리가 직접 코딩해야 하는 수고를 덜 수 있습니다. 
예를 들어 random 모듈은 난수를 발생시키는 기능을 가지고 있는데, 만약 random 모듈
을 사용하지 않고 직접 난수를 발생시키려면 직접 프로그램을 작성해야 하는 수고가 따릅니다. 

모듈을 사용하려면 우선 import를 이용해서 모듈을 가지고 와야 합니다. 
다음은 random 모듈을 이용해서 주사위 게임에 필요한 난수를 발생시키는 코드입니다. 
'''

# import random 
# randomNum = random.randrange(1, 46)
# print(f'randomNum: {randomNum}')

from random import randrange
randomNum = randrange(1, 46)

'''from -> random 모듈에서 randrange만 쓰겠다  따라서 다양한 랜덤 변수들을 활용거라면
실전처럼 그냥 import random을 사용한 이후에 .randrange 이런식으로 각각 지정해야 혼동이 없음

# + - * /   ........ >  모듈 > operator 모듈
'''
import operator 

print(10 + 20)
print(operator.add(10,20))

print(10 - 20)
print(operator.sub(10,20))

print(10 / 20)
print(operator.truediv(10,20))

print(10 % 20)
print(operator.mod(10,20))

print(10 // 20)
print(operator.floordiv(10,20))

print(10 ** 20)
print(operator.pow(10,20))

print(10 == 20)
print(operator.eq(10,20))

print(10 != 20)
print(operator.ne(10,20))

print(10 > 20)
print(operator.gt(10,20))

print(10 >= 20)
print(operator.ge(10,20))

print(10 < 20)
print(operator.lt(10,20))

print(10 <= 20)
print(operator.le(10,20))

print(True and False)
print(operator.and_(10,20))

print(True or False)
print(operator.or_(10,20))

print(not True)
print(operator.not_(10,20))
'''
'''
로그인 검사

아이디 id, 비밀번호 pw를 입력받아

id가 "admin"이고 pw가 "1234"이면 "로그인 성공"
id만 맞고 pw가 틀리면 "비밀번호 오류"
id가 틀리면 "아이디 없음"
'''

# id = str(input('아이디:'))
# pw = input('비밀번호:')

# if id == "admin" and pw == "1234":
#     print('로그인 성공')
# elif id == "admin" and pw != "1234":
#     print('비밀번호 오류')
# else :
#     print('아이디 없음')

    

# id = str(input('아이디:'))
# pw = input('비밀번호: ')   # 비밀번호는 int로 casting하기보다는 범용성 측면에서 그냥 input

# if id == 'admin' and pw == '1234':
#     print('로그인 성공')
# elif id == 'admin' and pw != '1234':
#     print('비밀번호 오류')
# elif id != 'admin' :
#     print('아이디 없음')

#근데 일반적으로 비밀번호는 문자로 받는 게 더 자연스러워서 input()만 쓰는 게 좋아.
# -> 이건 추론하기에는 비밀번호는 다양한 문자 배열의 합이라서 그런 것 같음

'''
택시 요금 계산

거리 km를 입력받아 요금을 계산해 출력하라.

기본요금: 3000원 (2km까지)
이후 1km당 1000원 추가

예)

1.5km → 3000원
3km → 4000원
5km → 6000원
''' 

# distance = float(input('주행 거리: '))

# basefee = 3000

# extraDistance = distance - 2

# if distance <= 2:
#     print(f'기본 요금 : {basefee}') 
# else:
#     if extraDistance == extraDistance // 1 :
#         print(f'택시요금 : {basefee + int(extraDistance)*1000:,}원')
#     else:
#         print(f'택시요금 : {basefee + (int(extraDistance)+1)*1000:,}원')

# int()  캐스팅하는걸 input에만 활용하지 말고 실행문 조건문에서도 활용해보기




# extraDistance = 1 - (distance // 1)

# if distance <= 2:
#     print(f'택시요금: {basefee}')

# else:
#     if extraDistance < 1:
#         print(f'택시요금 : {basefee + (1000*(((distance-2)//1)+1))}')
#     else:
#         print(basefee + (1000*(((distance-2)//1))))


# 1km당 1000원이라서 계산을 다시 해야함. 


# ✅ 연속적인 값(거리, 무게, 시간) → 그대로 계산 가능
# ✅ 개수(물건 수량, 인원, 장비 수) → 보통 올림 처리

'''extraDistance // 1 == 0 

이건 extraDistance의 정수부분이 0인지 확인하는 거야.

예를 들어:

extraDistance = 0.3
→ 0.3 // 1 = 0.0
→ True
extraDistance = 0.9
→ 0.9 // 1 = 0.0
→ True
extraDistance = 1.2
→ 1.2 // 1 = 1.0
→ False

즉 이건 0 이상 1 미만인지 확인하는 조건이야.'''

'''문제 2. 놀이공원 입장료 계산

나이 age와 키 height(cm)를 입력받아 입장료를 출력하라.

규칙:

나이 3세 미만: 무료
키 140cm 이상: 12000원
키 100cm 이상 140cm 미만: 8000원
키 100cm 미만: 5000원

단, 65세 이상은 무조건 무료.'''

age = int(input('나이: '))
height = int(input('키(cm): '))

if age < 3:
    print('무료')
elif age >= 65:
    print('65세 이상은 무조건 무료')
else:
    if height >= 140 :
        print('12000원')
    elif height >= 100 :
        print('8000원')
    else :
        print('5000원')
     

# age = int(input('나이:'))

# height = int(input('키(cm):'))

# if age < 3:
#     print('무료')
# elif age >= 3 and age < 65:       # age < 65 만 적어도 된다. 
#     if height >=140:
#         print('12000원')
#     elif height >=100 and height < 140:
#         print('8000원')
#     else:
#         print('5000원')
# else:
#     print('65세 이상은 무조건 무료')


#편의점 거스름돈 계산

# price = int(input('가격:'))

# paid = int(input('받은 돈:'))

# change = paid - price



# if change < 0 :
#     print('돈이 모자릅니다.')

# elif change == 0:
#     print('거스름돈 없음')

# else:
#     bill10000 = change // 10000
#     change = change % 10000

#     bill5000 = change // 5000
#     change = change % 5000

#     bill1000 = change // 1000                      # // 이건 몫이고 , % 나머지 
#     change = change % 1000

#     coin500 = change // 500                        # 파이썬에는 divmod()라는 함수가 있어서 몫과 나머지를 동시에 구할 수도 있어.
#     change = change % 500  

#     coin100 = change // 100
#     change = change % 100

#     coin50 = change // 50
#     change = change % 50

#     coin10 = change // 10
#     change = change % 10

#     print(f'10000원 : {bill10000}장')
#     print(f'5000원 : {bill5000}장')
#     print(f'1000원 : {bill1000}장')
#     print(f'500원 : {coin500}개') 
#     print(f'100원 : {coin100}개') 
#     print(f'50원: {coin50}개')
#     print(f'10원 {coin10}개')