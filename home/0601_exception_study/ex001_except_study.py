# sys.path.append 사용하기

# import sys

# # 'sys.path' [리스트형태]는 파이썬 라이브러리가 설치되어 있는 디렉터리 목록을 보여 준다. 
# # 이 디렉터리 안에 저장된 파이썬 모듈은 모듈이 저장된 디렉터리로 이동할 필요 없이 
# # 바로 불러 사용할 수 있다.


# C:\doit>set PYTHONPATH=C:\doit\mymod
# C:\doit>python
# import mod2
# print(mod2.add(3, 4))
# 7


# from game.sound import echo  이런식으로도 가능


# f = open('나없는 파일', 'r')

# try:
#     ...
# except [발생오류 [as 오류변수]]:

#     ...

try:
        4 / 0
   
except ZeroDivisionError as e:
        print('오류 발생') 

try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    (... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

    try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else:  # 오류가 없을 경우에만 수행
    ...

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')