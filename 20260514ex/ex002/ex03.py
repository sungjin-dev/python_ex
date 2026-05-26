# CRUD
'''
C : Create   생성 추가
R : Read     조회
U : Update   수정
D : Delete   삭제
'''

'''
딕셔너리(Dictionary) : {Key: value}                 # 딕셔너리[]  -> []안에는 key값만 가능
 '''
# C : Create   생성 추가
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'      #Java의 경우 , 있음
}

print(f'student: {student}')
print(f'student type: {type(student)}')

# R : Read     조회

sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')

#  U : Update   수정

sName = student['이름']
print(f'sName: {sName}')       # 홍길동 -> 홍길자

student['이름'] = '홍길자'
sName = student['이름']
print(f'sName: {sName}')      # 홍길자

# D : Delete   삭제

del student['연락처']
print(f'student: {student}')

# keys(), values(), items()

# keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다. 뽑은 키들은 리스트와 비슷한 데이터 타입이다. 
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')        # class 'dict_keys'

for key in keys:                #  dict_keys(['학번', '이름', '나이', '성별'])
    print(f'key: value = {key}:{student[key]}')


# values(): 딕셔너리에서 밸류값들만 몽땅 뽑는다. 뽑은 밸류들은 리스트와 비슷한 데이터 타입이다. 

values = student.values()
print(f'values: {values}')               # dict_values([123456789, '홍길자', 20, 'M'])
print(f'values type: {type(values)}')    # <class 'dict_values'>

for value in values:
    print(f'value: {value}')

items = student.items()        # key & value
print(f'items: {items}')       # dict_items([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
                               # 리스트 내 아이템들이 튜플로 묶여져 있음
for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0]}, {item[1]}')
                         #     key         value

'''
item 튜플 ('학번', 123456789)  == item[0], item[1]
'''                         

for key, value in items:              # 구조분해할당
    print(f'key: value = {key}: {value}')

'''
key, value = ('학번', 123456789)
'''

# 구조분해할당
a,b = (10,20)
print(f'a: {a}, b: {b}')

c= (10, 20)
a = c[0]
b = c[1]
print(f'a: {a}, b: {b}')

a = 10
b = 20

# swapping ==> a: 20, b:10
temp = a
a = b             # a: 20
b = temp          # b: 10

a, b = b, a

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''

a, b, *c = scores
print(f'a: {a}, b: {b}, c:{c}')         #  [정수] -> 정수  [정수,] 값 하나만 있을 때 리스트형태 살리는법 콤마

# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 파이썬을 이용해서 컨테이너 자료형으로 만드시오. 

members = {                   #박찬호+25+M+010-1234-5678+헬스+수영+0
    '2019-052001': '박찬호+25+M+010-1234-5678+헬스+수영+0'
   
}
info = members['2019-052001']
print(f'info: {info}')       # 박찬호+25+M+010-1234-5678+헬스+수영+0
infos = info.split('+')
print(f'infos: {infos}')     # ['박찬호', '25', 'M', '010-1234-5678', '헬스', '수영', '0']

members = {                   #
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스, 수영'],    # 복수데이터는 리스트로 묶어주는게 좋다. 
        '할인율': 0
    }
   
}

print(members['2019-052001'])  # ['박찬호', '25', 'M', '010-1234-5678', '헬스', '수영', '0']
print(members['2019-052001']['이름'])
print(members['2019-052001']['나이'])
print(members['2019-052001']['할인율'])
print(members['2019-052001']['이용서비스'])

'''
함수(function)
'''



# '2019-052004''2019-052003'