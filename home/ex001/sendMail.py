# print('회원정보를 입력하세요.')

# userName = input('이름:')
# userMail = input('메일:')
# userId = input('아이디')
# userPw = input('비밀번호:')

# print('-----------------------------')
# print('To. ' + userMail)           #userMail -> 변수명
# print('▶아이디 및 비밀번호 확인')
# print(userName + '고객님 안녕하세요')                
# print(userName + '고객님의 아이디와 비밀번호는 아래와 같습니다')                            
# print('아이디: ' + userId)               
# print('비밀번호 : ' + userPw)               
# print('감사합니다')               
# print('Naver 담당자.')               
# print('-----------------------------')     
# 
userName = input('이름 :')
userMail = input('메일:')
userId = input('아이디:')
userPw = input('비밀번호:') 

print('To.' + userMail)
print('★아이디 및 비밀번호 확인')
print(userName + '고객님 안녕하세요')
print(userName + '고객님의 아이디와 비밀번호는 아래와 같습니다')
print('아이디 :' + userId)
print('비밀번호 :' + userPw)
print('감사합니다')
print('Naver 담당자.')

# userMail = 'gildong@gmail.com'
# print('To. gildong@gmail.com')
# print('To. ' + userMail)
# print('To. ' , userMail)         #기본적으로 콤마는 한칸 뛰운다 

# print("이름:", "홍길동", "나이", 20)  #이름: 홍길동 나이: 20 (*****)

# print("2026", "05", "06", sep="-")  #2026-05-06 (**)

# print("Hello", end="")         # 자동개행을 막는 방법 (end="")
# print("Hello", end=" ")         #  (end=" ") -> 칸을 띄우는 방법
# print("World")

# f-string (가장 많이 사용) (*********************)

# name = "철수"
# age = 25

#이름은 철수, 나이는 25입니다. 

# print('이름은 ', + name + ', 나이는' + age + '입니다.')
# print('이름은 ' + name + ', 나이는')

# print(f'이름은 {name}, 나이는 {age}')  #el표기법

# print(f"이름은 {name}이고 나이는 {age}입니다.")

# #format() (두 번째로 많이 사용) (*********************)

# print("이름은 {}, 나이는 {}입니다.".format(name, age))

# print("이름은 {1}, 나이는 {0}입니다.{1}{0}{1}{0}".format(age, name))   #순서 지정하는 방법

name = "철수"
age = 25

print(f'이름은 {name}, 나이는 {age}입니다') 


# korScore = input('국어 점수')
# engScore = input('영어 점수')
# mathScore = input('수학 점수')

# print(f'국어 점수:{korScore}')
# print(f'국어 점수:{engScore}')
# print(f'국어 점수:{mathcScore}')


# firstNum = input('첫 번째 정수 입력 :')
# secondNum = input('두 번째 정수 입력:')

# firstNum = int(firstNum)
# secondNum = int(secondNum)

# sum = (firstNum + secondNum)
# average = (firstNum + secondNum)/2
       
# print(f'합:{sum}')
# print(f'평균:{average}')



#var1, var2 변수에서 정수 10과 20이 각각 저장되어 있다. 
#var1과 var2의 데이터를 서로 바꾸는 프로그램을 만들고 화면에 var1과 var2의 데이터를 출력하시오. 

# var1 = 10
# var2 = 20

# print(f'var1: {var1}, var2: {var2}')

# temp = var1
# var1 = var2
# var2 = temp
# print(f'var1: {var1}, var2: {var2}')








