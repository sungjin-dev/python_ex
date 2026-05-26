# 지역변수 vs 전역변수
# 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능합니다. 
# 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능합니다. 

# num = 10

# def fun():
#     global num                  # 함수가 실행되고 나서 적용되는 것
#     num = 20                    # 지역변수 -> 전역변수를 변경시킴 num => 20
#     num = num + 1               # 데이터 수정 num(전역변수) = 10 +1     
#     print(f'num: {num}')        # 이게 2번째로 출력된다.  

# print(f'num: {num}')           #10, 함수를 실행하기 전이므로 원래 전역변수인 10이 출력 <- 이게 1번째로 출력

# fun()           # 함수는 호출되기 전에는 실행되지 않는다 주의할 것

'''
global 키워드는 함수 내에서 전역변수의 값을 수정하고자 할 때 반드시 명시하자!
'''

# quiz) 웹사이트의 누적방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다. 

# flag = True
# totalVistor = 0

# def countVisitor():
#     global totalVistor        # global은 함수에서만 사용 가능한데 for문 while문에 함수를 대입해서 사용
#     totalVistor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문  2.종료'))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVistor}')
#     else:
#         flag = False
#         print(f'Good bye~')

# 매개변수 (*******************************)
# 매개 : 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출.
# 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 합니다. 

# 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 합니다. 
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장합니다. 그리고 매개변수는 지역변수의 일종입니다. 

# def greet(name, age):
#     # name = '홍길동' or '박찬호' or '박세리'     눈에 보이진 않음
#     print(f'{name}님 안녕하세요. 나이는 {age}')
    
# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)

# 세상 모든 형식 다 가능
# 매개변수는 호출부에 전달하는 인수의 개수와 순서에 맞춰서 선언한다. 다 쓸 필요는 없음 
# 다만 선언부와 호출부 순서 개수는 맞추자  안 맞추면 TypeError argument (인수)

# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}도')
#     print(f'비올 확률: {rain}도')

# forecastWeather(32, 67, 50)


# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자!
# 우리 학급 학생 수는 총 3명이다 

# def printScoresForStudent(score1, score2, score3):
#     totalScore = score1 + score2 + score3
#     averageScore = totalScore/3

#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# def printScoresForStudent(subject, *scores):                 #  여기서 * 가변인자(variable arguments)는 맨 마지막에 위치해야함

#     print(f'scores type: {type(scores)}')           # tuple
#     print(f'scores length: {len(scores)}')           # 4

#     totalScore = 0
#     for score in scores:
#         totalScore += score
#     print(f'{subject}과목 총합: {totalScore}')
#     averageScore = totalScore / len(scores)
#     print(f'{subject}과목 평균: {averageScore}')

#     #  totalScore = score1 + score2 + score3
#     #  averageScore = totalScore/3

#     #  print(f'총합: {totalScore}')
#     #  print(f'평균: {averageScore}')

# printScoresForStudent(90, 80, 100, 90)


# 90 , 80 , 100
# printScoresForStudent('국어', 90, 80, 100)

# ★ 가변인자가 사용된 예시

1. 태그들을 계속 늘릴 때

def write_diary(content, *tags):       # 가변인자는 맨 마지막에 위치
    print(f"일기 내용: {content}")
    print(f"첨부된 태그들: {tags}")

    for tag in tags:
        print(f" -> #{tag}")   # 이건 그냥 이쁘게 출력하는 용도인듯?

# 필수 정보 외에 추가 정보는 가변인자(**kwargs)로 받는 회원가입 함수

def register_member(uId, uPw, **additional_info):
    # 기본 회원 정보 생성
    member_profile = {
        'uId': uId,
        'uPw': uPw
    }        
    member_profile.update(additional_info)   # 딕셔너리 자료형 전용 '메서드(Method)'
    
    print(f"최종 저장된 회원 정보: {member_profile}")

    register_member("gildong", "1234")

    print("-" * 30)

    register_member("chanho", "0000", uMail="chanho@naver.com", uPhone="010-1234-5678")






'''
선생님이 몇명일지 모르는 학생의 점수를 입력한다. 
이 때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자!

'''

# totalScores = 0
# averageScores = 0
# scoreLits = []

# def studentScores():
#     global totalScores

#     while True:
#         selectedNum = int(input('1. 점수입력, 0, 종료'))

#         if selectedNum == 1:
        
#             scores = int(input('점수를 입력하시오.'))
#             scoreLits.append(scores)
#             totalScores += scores   
        
#         elif selectedNum == 0:
#             print('종료합니다.')
#             break

#         else:
#             print('잘못 입력하였습니다. ')  

# studentScores()

# averageScores = totalScores / len(scoreLits)    # len(scoreLits)  이건 scoreLits = ['a', 'b'] 이런식이면 len = 2 이고 2개의 값이 있다는 말임

# print(f'총합은 {totalScores}, 평균은 {averageScores}')

'''
구분괄호를 비워두는 경우 (def fun():)                 괄호에 매개변수를 넣는 경우 (def fun(x):)핵심 

요약함수가 스스로(내부에서) 재료를 다 구함             함수가 작동하려면 외부에서 재료를 줘야 함
대표 예시input()으로 안에서 직접 입력받을 때           밖에서 이미 구한 데이터로 계산만 시킬 때
비유메뉴 주문부터 요리까지 다 하는 무인 식당           손님이 고기를 가져오면 구워만 주는 식당
'''

# flag = True
# studentScores = []

# def printScoresForStudent(scores):      # scores = [,,,,,,,,,]
#     if len(scores) == 0:                                #  바로 종료할 경우를 대비하는 방법
#         print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for score in scores:
#             totalScore += score
        
#         average = totalScore / len(scores)   # 0 / 0 
#         print(f'총점: {totalScore}')
#         print(f'평점: {average}')
    
# while flag:
#     selectedMenuNum = int(input('1.학생 점수 입력     2.종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score)
#     else:
#         flag = False          # while True break 구조는 else가 아니면 종료되지 않는다. 
#         #break

# printScoresForStudent(studentScores)

# quiz) SMS와 MMS 구별하기

'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''
# 1번 경우

# def userMessage(message):
 
#     messageLength = len(message)    # <- input으로 받은 데이터(messageInput)를 message로 다시 뿌려주는거기 때문에
#                                     #   함수 내에서 message(매개변수)를 쓰자!                   
#     if messageLength <= 100:
#         print('단문 메시지 입니다. 50원 부과 ')

#     if messageLength > 100:
#         print('장문 메시지 입니다. 100원 부과 ')

# messageInput = str(input('문자 입력 : '))         # 어차피 호출되기 전이라서 이게 함수보다 먼저 실행된다. 
# userMessage(messageInput) 


# 2번 경우 
# def userMessage(str):

# messageInput = str(input('문자 입력 : '))          

#     messageLength = len(str)             

#     if messageLength <= 100:
#         print('단문 메시지 입니다. 50원 부과 ')

#     if messageLength > 100:
#         print('장문 메시지 입니다. 100원 부과 ')
       
# userMessage(messageInput)     # 실행이 꼬이는 이유는 def(함수) 안에 내용들을 흩고 지나가다가 호출되면 실행이 되는 구조인데
                                # 호출할 때 'messageInput'이라는 변수가 defined되지 않기 때문에 에러가 발생함



# def sendUserMessage(str):
#     strlength = len(str)                     # 길이는 len()  사용
#     print(f'사용자가 입력한 문자 길이: {strlength}')
  
#     if strlength <= 100:
#         print(f' SMS 발송완료!')
#         print('50원 부과!')    
#     else:
#         print(f' MMS 발송완료!')
#         print('100원 부과!')

# inputData = input('문자 입력')
# sendUserMessage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우

# def printMemberInfo(name, email, major, grade):   # 동사 + 목적어 형태가 좋음
#     print(f'Name\t: {name}')
#     print(f'Email\t: {email}')
#     print(f'Major\t: {major}')
#     print(f'Grade\t: {grade}')
#     print('-----------------------------')

# printMemberInfo("Hong Gildong","gildong@gmail.com", "art", 1)    # -> 지향하는 방식
# printMemberInfo(email = "gildong@gmail.com",                     # -> 지양하는 방식
#                 name = "Hong Gildong", 
#                 major = "art", 
#                 grade = 1)      
# 순서대로 입력하지 않아도 이렇게 하면 된다. 지정하려면 전부 지정해야한다. 


# def printMemberInfo(info):
#     print(f'name: {info['name']}')
#     print(f'email: {info['email']}')
#     print(f'major: {info['major']}')
#     print(f'grade: {info['grade']}')

# printMemberInfo(
#     {
#         'name': 'Hong Gildong',
#         'email': 'gildong@gmail.com',
#         'major' : 'art',
#         'grade' : 1
#     }
# )

# # 이런 구조다. 
# MemberInfo = {
#         'name': 'Hong Gildong',
#         'email': 'gildong@gmail.com',
#         'major' : 'art',
#         'grade' : 1
#     }
# printMemberInfo(MemberInfo)


# 매개변수의 기본값 설정
# 직원 급여 지급 프로그램을 만들어보자!

# def setSalary(name, pay = 200):    # 기본값 설정
#     print(f'{name}의 급여는 {pay}원 지급!!')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')

# [].sort()      # reverse = False
# [].sort(reverse = True)      # reverse = False

# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다. 
# 이때 사용하는 키워드가 return
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자!

# def printResult(value):
#     print(f'result: {value}')

# def addFuntion(n1, n2):
#     sum = n1 + n2         # 30
#     # print(f'결과값: {sum}')
#     printResult(sum)
#     return sum      # 호출부로 

# addFuntion(10, 20)    # 반환해서 호출부에서 받아도 되고 안 받아도 되고   
#result = addFuntion(10, 20)        # 받을 경우 result = addFuntion(10, 20) 
#print(f'result: {result}')

DEV_MOD = True

def fun1():
    print('111111111')
    if DEV_MOD == True:
        print('222222222')          # 함수를 종결시키는 기능 호출부로 넘겨버리니까  위치가 중요  test할 때도 쓴다
        return                      # ex) 개발단계에서 디버깅 용도로만 사용한다
    print('333333333')
DEV_MOD
fun1()

# return 뒤에 아무것도 안 적으면, 파이썬은 알아서 
# "아, 내보낼 데이터는 없고(None) 그냥 함수만 끝내고 싶구나?" 
# 라고 찰떡같이 알아듣습니다. (실제로는 보이지 않게 return None이 실행됩니다.)

# 🥊 break vs return (비슷하지만 다릅니다!)
# 말씀하신 대로 기능이 break와 아주 비슷한 느낌이죠? 하지만 둘은 활동하는 무대가 다릅니다.

# break: 반복문(while, for)을 깨부수고 탈출할 때 씁니다. (함수 자체를 끝내지는 않음)

# return: 함수(def) 전체를 깨부수고 밖으로 완전히 탈출할 때 씁니다.

def check_adult(age):
    # 1. 나이가 18세 미만이면 여기서 함수 즉시 종료! (Early Return)
    if age < 18:
        print("미성년자는 출입할 수 없습니다.")
        return    # <- 보안관 느낌임 
    
    # 2. 18세 이상인 사람만 이 아래 코드가 실행됨
    print("환영합니다! VIP 라운지 입장 가능합니다.")
    print("오늘의 칵테일을 준비해 드릴까요?")

# 별탑 만들기
# def increaseStart(limitStarCount): 
#     # print('*')
#     # print('**')
#     # print('***')
#     # print('****')
#     # print('*****')
#     # print('******')
#     # print('*******')
#     for n in range(1,8):
#         print('*' * n)
#         if n == limitStarCount:
#             break
# increaseStart(5)           # 호출하는 쪽에 제어권을 주는게 더 유연해짐 (긍정적)  IOC 

# 7 ~8교시
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다. 
메뉴 : 1. 회원가입      2. 로그인       3. 특정 회원 정보 출력      4.모든 회원 정보 출력   99. 종료
사용자가 '1.회원가입'을 선택하면 회원 ID, 회원 PW 회원 Email, 회원 Phone 정보를 입력받아 회원가입 진행한다.
2. 로그인을 선택하면 회원 ID, 회원 PW를 입력받아 로그인 '성공' 또는 '실패' 출력
3. '특정 회원 정보 출력'을 선택하면 회원ID와 회원 PW를 입력받아 일치하는 회원 정보를 모두 출력한다. 
4. 모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다. 
'99.종료'를 선택하면 프로그램 종료 시킨다.

5. 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자.
'''

'''
1. 외부에서 던져줄 데이터(인수)가 필요없을 때는 ()를 일단 비워둔다. 내부에서 자체적으로 할당 받을 때
2. 함수 내부의 변수들 = 함수 끝나면 지워지는 시한부(지역 변수)
3. return = 시한부 데이터를 밖으로 던져주는 구출 로프
 폭파 직전, return이라는 헬기를 태워 데이터 알맹이만 밖으로 슝 던진 것(명찰 필요)
  "이미 존재하는 데이터 객체에 새로운 이름표를 붙이는 행위가 필요함
4. 딕셔너리로 관리할 때는 return으로 key값을 따로 빼주는게 좋다. 
5. 큰 상자(totalUserInfoDict)에 'sora'라는 Key(방 번호)가 있는지 봅니다. 없으므로 'sora'라는 새로운 전용 방을 개설
-> 리스트는 방을 하나 만들려면 반드시 append() 같은 함수를 써서 컴퓨터에게 승인을 받아야만 순서대로 방이 늘어남
-> 딕셔너리는 대괄호([]) 안에 들어오는 것이 '숫자'든 '문자열'이든 상관없이, 일단 큰 상자 뒤져보고 없으면 
    "아, 새로 입주하고 싶으시구나! 제가 알아서 땅 파서 문패 달아드릴게요!" 하고 자율적으로 공간을 창조
    중첩 딕셔너리의 핵심임.

# [1단계 변신] 함수가 실행되어 튜플 상자가 튀어나옴

userId, userInfo = userinfoData()

# [2단계 변신] 코드가 내부적으로 이렇게 바뀜
userId, userInfo = ('sora', {'PW': '123'})
여기서 파이썬의 '구조 분해 할당(Unpacking)'이라는 마법이 일어납니다.
좌변에 콤마로 변수를 두 개(userId, userInfo) 나란히 적어두면, 파이썬이 우변에 있는 튜플 상자를 열어서 순서대로 착착 대입해 줍니다!

userId 라는 변수에는 튜플의 첫 번째 알맹이인 'sora'가 쏙 들어갑니다.

userInfo 라는 변수에는 튜플의 두 번째 알맹이인 딕셔너리 {'PW': '123'}가 쏙 들어갑니다.

딕셔너리에 데이터를 추가할 때 딕셔너리[키] = 값 형태

'''

# totalUserInfoDict = {}

# def userinfoData():                              
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')
#     userInputEmail = input('Email을 입력하세요.')
#     userInputPhoneNum = input('핸드폰 번호를 입력하세요.')

#     userInfodict = {
#         'ID': userInputId,
#         'PW': userInputPw,  
#         'Email': userInputEmail,
#         'PhoneNum': userInputPhoneNum
#     }
        
#     return userInputId, userInfodict 
 

# def checkUserLogin():   
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')

#     if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#             print('로그인 성공!')
#     else:
#         print('로그인 실패 다시 입력해주세요!')

# def checkUserData():   
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')
#     if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#         print(f'ID : {userInputId} 님의 정보는 {totalUserInfoDict[userInputId]}입니다.')
    
# def changeUserInfo():   
#      userInputId = input('ID를 입력하세요.')
#      userInputPw = input('PW를 입력하세요.')

#      if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#         print('로그인 성공!')

#         userInputNum = int(input('변경하고 싶은 회원정보 1. 비밀번호, 2. 이메일, 3. 핸드폰 번호')) 

#         if userInputNum == 1: 
#             totalUserInfoDict[userInputId]['PW'] = input('변경하고 싶은 비밀번호 : ')

#         elif userInputNum == 2: 
#             totalUserInfoDict[userInputId]['Email'] = input('변경하고 싶은 이메일주소 : ')

#         elif userInputNum == 3: 
#             totalUserInfoDict[userInputId]['PhoneNum'] = input('변경하고 싶은 핸드폰번호 : ')

#         else:
#             print('번호를 다시 입력해주세요.' )
        
#      else:
#         print('로그인 실패 다시 입력해주세요!')

# flag = True
    
# while flag:
           
#     userInputNum = int(input('원하는 항목을 선택하세요. 1. 회원가입  2. 로그인, 3. 특정 회원 정보 출력  4.모든 회원 정보 출력 5. 회원정보 수정 99. 종료 '))
     
#     if userInputNum == 99:
#          flag = False
#          print('프로그램을 종료합니다.')

#     elif userInputNum == 1:
#          userInputId, userInfodict = userinfoData()         
#          totalUserInfoDict[userInputId] = userInfodict      
    
#     elif userInputNum == 2:
#         checkUserLogin()
    
#     elif userInputNum == 3:
#         checkUserData()

#     elif userInputNum == 4:
#         print(f' 모든 회원 정보: {totalUserInfoDict}')
    
#     elif userInputNum == 5:
#         changeUserInfo()
        
#     else: 
#         print('번호를 다시 입력해주세요.')


# totalUserInfoDict = {}

# def userinfoData():                              
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')
#     userInputEmail = input('Email을 입력하세요.')
#     userInputPhoneNum = input('핸드폰 번호를 입력하세요.')

#     userInfodict = {
#         'ID': userInputId,
#         'PW': userInputPw,  
#         'Email': userInputEmail,
#         'PhoneNum': userInputPhoneNum
#     }
    
#     userInfodict = {userInputId: userInfodict}   
#     return userInfodict 
 

# def checkUserLogin():   
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')

#     if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#             print('로그인 성공!')
#     else:
#         print('로그인 실패 다시 입력해주세요!')

# def checkUserData():   
#     userInputId = input('ID를 입력하세요.')
#     userInputPw = input('PW를 입력하세요.')
#     if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#         print(f'ID : {userInputId} 님의 정보는 {totalUserInfoDict[userInputId]}입니다.')
    
# def changeUserInfo():   
#      userInputId = input('ID를 입력하세요.')
#      userInputPw = input('PW를 입력하세요.')

#      if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#         print('로그인 성공!')

#         userInputNum = int(input('변경하고 싶은 회원정보 1. 비밀번호, 2. 이메일, 3. 핸드폰 번호')) 

#         if userInputNum == 1: 
#             totalUserInfoDict[userInputId]['PW'] = input('변경하고 싶은 비밀번호 : ')

#         elif userInputNum == 2: 
#             totalUserInfoDict[userInputId]['Email'] = input('변경하고 싶은 이메일주소 : ')

#         elif userInputNum == 3: 
#             totalUserInfoDict[userInputId]['PhoneNum'] = input('변경하고 싶은 핸드폰번호 : ')

#         else:
#             print('번호를 다시 입력해주세요.' )
        
#      else:
#         print('로그인 실패 다시 입력해주세요!')

# flag = True
    
# while flag:
        
#     userInputNum = int(input('원하는 항목을 선택하세요. 1. 회원가입  2. 로그인, 3. 특정 회원 정보 출력  4.모든 회원 정보 출력 5. 회원정보 수정 99. 종료 '))
     
#     if userInputNum == 99:
#          flag = False
#          print('프로그램을 종료합니다.')

#     elif userInputNum == 1:
#          userInfodict = userinfoData()         
#          for userId in userInfodict:
#             totalUserInfoDict[userId] = userInfodict[userId]      
    
#     elif userInputNum == 2:
#         checkUserLogin()
    
#     elif userInputNum == 3:
#         checkUserData()

#     elif userInputNum == 4:
#         print(f' 모든 회원 정보: {totalUserInfoDict}')
    
#     elif userInputNum == 5:
#         changeUserInfo()
        
#     else: 
#         print('번호를 다시 입력해주세요.')


# def MemberInfo(userinputId, userinputPw, userinputEmail, userinputPhoneNum):
#        print(f'ID: {userinputId}, PW: {userinputPw}, Email:{userinputEmail}, PhoneNum: {userinputPhoneNum}')

# def inputUserData(userinputId, userinputPw ):
#          userinputId = input('ID를 입력하시오.')
#          userinputPw = input('비밀번호를 입력하시오.')
#     inputUserData(userinputId, userinputPw)


# userIdData = []
# userPwData = []
# userEmailData = []
# userPhonNumData = []

# userinfodict = {
#      'ID': userIdData,
#      'PW': userPwData,
#      'Email': userEmailData,
#      'PhoneNum':userPhonNumData
# }

# flag = True
    
# while flag:
#     userInputNum = int(input('원하는 항목을 선택하세요. 1. 회원가입  2. 로그인  3. 특정 회원 정보 출력  4.모든 회원 정보 출력 5. 회원정보 수정 99. 종료 '))
#     if userInputNum == 99:
#         flag = False
#         print('프로그램을 종료합니다.')

#     elif userInputNum == 1:
#         userinputId = input('ID를 입력하시오.')
#         userinputPw = input('비밀번호를 입력하시오.')
#         userinputEmail = input('이메일을 입력하시오.')
#         userinputPhoneNum = input('핸드폰 번호를 입력하시오.')
#         userIdData.append(userinputId)
#         userPwData.append(userinputPw)
#         userEmailData.append(userinputEmail)
#         userPhonNumData.append(userinputPhoneNum)

#     elif userInputNum == 2:
#         userinputId = input('ID를 입력하시오.')
#         userinputPw = input('비밀번호를 입력하시오.')

#         if userinputId in userIdData and userinputPw in userPwData:
#             print('성공')
#         else :
#             print('실패')

#     elif userInputNum == 3:
#         userinputId = input('ID를 입력하시오.')
#         userinputPw = input('비밀번호를 입력하시오.')
#         if 'ID' in userinfodict and 'PW' in userinfodict:
#             print(f'ID: {userinputId}, PW: {userinputPw}, Email:{userinputEmail}, PhoneNum: {userinputPhoneNum}')
#         else:
#             print('아이디를 다시 입력해주세요.')
#     elif userInputNum == 4:    
#            # for i in range(len(userIdData)-1):
#                 print(userinfodict)
#     elif userInputNum == 5: 
#             userinputId = input('ID를 입력하시오.')
#             userinputPw = input('비밀번호를 입력하시오.')
#             if 'ID' in userinfodict and 'PW' in userinfodict:
#                  userinfodict['ID'] = input('바꾸고 싶은 ID입력')
#                  userinfodict['PW'] = input('바꾸고 싶은 PW입력')
#             else :
#                 print('다시 입력하시오.')
                


# 1. 오직 '로그인 인증'만 담당하는 함수를 따로 만듭니다.



# def authenticateUser():
#     userInputId = input('ID를 입력하세요: ')
#     userInputPw = input('PW를 입력하세요: ')
    
#     # 인증에 성공하면 ID를 리턴하고, 실패하면 None을 리턴합니다.
#     if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
#         return userInputId
#     return None


# def checkUserLogin():   
#     # 이제 인증 함수를 호출하기만 하면 됩니다!
#     userId = authenticateUser()
#     if userId:
#         print('로그인 성공!')
#     else:
#         print('로그인 실패 다시 입력해주세요!')


# def checkUserData():   
#     userId = authenticateUser()
#     if userId:
#         print(f'ID : {userId} 님의 정보는 {totalUserInfoDict[userId]}입니다.')
#     else:
#         print('로그인 실패 다시 입력해주세요!')


# def changeUserInfo():   
#     userId = authenticateUser()
#     if userId:
#         print('로그인 성공!')
#         userInputNum = int(input('변경하고 싶은 회원정보 1. 비밀번호, 2. 이메일, 3. 핸드폰 번호: ')) 

#         # 이제 앞에서 배운 대로 깔끔하게 알맹이만 콕 집어 수정!
#         if userInputNum == 1: 
#             totalUserInfoDict[userId]['PW'] = input('변경하고 싶은 비밀번호: ')
#         elif userInputNum == 2: 
#             totalUserInfoDict[userId]['Email'] = input('변경하고 싶은 이메일: ')
#         elif userInputNum == 3: 
#             totalUserInfoDict[userId]['PhoneNum'] = input('변경하고 싶은 핸드폰 번호: ')
#         else:
#             print('번호를 다시 입력해주세요.')
#         print('✨ 정보가 성공적으로 변경되었습니다!')
#     else:
#         print('로그인 실패 다시 입력해주세요!')