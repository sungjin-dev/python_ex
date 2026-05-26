# 파일 다루기 3단계

# 1단계 파일 열기
# open()

# 객체로 만들어져 메모리에 생성 

# 2단계 파일 쓰기/읽기

#  write()  and  read()


# 3단계 
# 
# close()

# open() -->> write() or read() -->> close()

# file = open('C:/PSJ/python_ex/test.txt', 'w')  # 파일을 '쓰기'모드로 open 한다.

# result = file.write('Hello python!')           # 쓰기(write)
                   
# print(f'result: {result}')                     # 문자열의 길이

# file.close()                                   # 파일 닫기(close, 외부자원 해제)

# file = open('C:/PSJ/python_ex/test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult type: {type(readResult)}')    # 무조건 문자열
# file.close()

# readResult = int(readResult)      # 문자열이라  int casting
# readResult += 1

# file.close()

# file = open('C:/PSJ/python_ex/test.txt', 'w')  # 'w' 덮어써버림
# file.write('\nhello~')
# file.close()

# file = open('C:/PSJ/python_ex/test.txt', 'a')  # a 왠지   append
# file.write('\nhi~')
# file.close()

# with open('C:/PSJ/python_ex/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello~')     # file.close() 기능이 내재

# 읽기모드                   'r'   반드시 파일 존재해야함 
# create 생성모드            'x'   반드시 파일이 없어야 함 이미 존재 x
#                            '+'   읽고 쓰기 동시 가능

# 예외 처리(보험)

# 세상에 모든 프로그램은 100% 완벽할 수가 없어요.



# 예외 처리 기본 문법

'''
try ~ except
'''

# try:
#     print(10 / 0)    #  error
# except: 
#     pass
try:
    print(10 + 20)
    print(10 / 0)    #  error
    print(10 - 20)   # 실행  x 
    print(10 * 20)   # 실행  x

except Exception as e:      # Exception class
    print(f'e: {e}')

# 오류날 곳에 정확하게 사용해야한다 


#올바른 예시 

# print(10 + 20)

# try:
    
#     print(10 / 0)    #  error

# except Exception as e:      # Exception class
#     print(f'e: {e}')

# print(10 - 20)   
# print(10 * 20)   


 
# print(10 + 20)

# try:
    
#     print(10 / 0)    #  

# except Exception as e:      # Exception class
#     print(f'e: {e}')

else:
    print('에러가 발생되지 않으면 실행되는 코드')

finally:
    print('에러가 발생하든 안 하든 무조건 실행되는 코드')

# print(10 - 20)   
# print(10 * 20)

