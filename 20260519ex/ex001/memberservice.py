'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다. 
메뉴 : 1. 회원가입      2. 로그인       3. 특정 회원 정보 출력      4.모든 회원 정보 출력   99. 종료
사용자가 '1.회원가입'을 선택하면 회원 ID, 회원 PW 회원 Email, 회원 Phone 정보를 입력받아 회원가입 진행한다.
2. 로그인을 선택하면 회원 ID, 회원 PW를 입력받아 로그인 '성공' 또는 '실패' 출력한다. -> 인증(Authentication) / 인가(Athurization)
3. '특정 회원 정보 출력'을 선택하면 회원ID와 회원 PW를 입력받아 일치하는 회원 정보를 모두 출력한다. 
4. 모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다. 
'99.종료'를 선택하면 프로그램 종료 시킨다.

5. 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자.
'''

SIGN_UP                = 1
SIGN_IN                = 2
PRINT_MY_INFO          = 3
PRINT_ALL_MEMBER_INFO  = 4
SYSTEM_SHUTDOWN       = 99

DEV_MOD = True

flag = True

members = {}             # Database

if DEV_MOD :

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234','5678','3124']
    uMails = ['gildong@gmail.com','chanho@naver.com','saeri@daum.net']
    uPhones = ['010-1234-5678','010-9999-6666','010-7777-3333']

    for n in range(len(uIds)):               # 3회 반복 (0, 1, 2)
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMails': uMails[n],
            'uPhones': uPhones[n]
        }

#functions START
def getSelectedMenuNum():
    selectedMenuNum= int(input('1. 회원가입   2. 로그인    3. 나의 정보 출력   4.모든 회원 정보 출력   99. 종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):    
    members[uId] = {                              
                    'id': uId,
                    'uPw': uPw,
                    'uMail': uMail,
                    'uPhone': uPhone
                }       
def isMember(uId):
    if uId in members:
            print(f'{uId}는(은) 이미 사용 중 입니다. 다시 확인하세요.') 
            return True
    else:
        return False
        
def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')

#functions END


while flag:
    userSelectedMenuNum = getSelectedMenuNum()

    if userSelectedMenuNum == SIGN_UP:            # 1. 회원가입
        uId = input('input member ID:') 

        if not isMember(uId):     # False: 회원이 없는경우(회원가입 진행O)   True: 회원이 있는경우(회원가입 진행X)                   
            uPw = input('input member PW:')
            uMail = input('input member EMAIL:')  
            while True:         
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지 않습니다.')
                    uMail = input('Input member EMAIL: ')
                else:
                    break
            uPhone = input('input member PHONE:')

            setNewMember(uId, uPw, uMail, uPhone)
                          
            print('SIGN-UP SUCCESS!!')

        if DEV_MOD : print(f'members: {members}')          # 나중에 생략하고 싶으면 DEV_MOD = False로 바꾸자 0

    elif userSelectedMenuNum == SIGN_IN:
        signInCount = 1
        while True:                             # 2. 로그인        
            uId = input('input member ID:')
            uPw = input('input member PW:')          
                    
            if uId in members:                      # not in 일 경우 없으면 True 있으면 False
                uInfo = members[uId] 
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!') 
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print('존재하지 않은 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINT_MY_INFO:                  # 3. 나의 정보 출력
        uId = input('input member ID:')
        uPw = input('input member PW:')          

        if uId in members:                      
            uInfo = members[uId] 
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재하지 않은 ID입니다. 다시 확인하세요.')
    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:          # 4. 모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보------')
            for key1, value1 in value.items():
                print(f'{key}: {value1}')
            print('_' * 30)
    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:                # 99. 종료
        flag = False
        print('Good bye~')

        # MVC패턴이란?

# while flag:

#     selectedMenuNumint= int(input('1. 회원가입   2. 로그인    3. 나의 정보 출력   4.모든 회원 정보 출력   99. 종료'))

#     if selectedMenuNumint == SIGN_UP:            # 1. 회원가입
#         uId = input('input member ID:') 
#         if uId in members:
#             print(f'{uId}는(은) 이미 사용 중 입니다. 다시 확인하세요.')

#         else:               
#             uPw = input('input member PW:')
#             uMail = input('input member EMAIL:')  
#             while True:         
#                 if '@' not in uMail:
#                     print('입력한 이메일 주소가 형식에 맞지 않습니다.')
#                     uMail = input('Input member EMAIL: ')
#                 else:
#                     break
#             uPhone = input('input member PHONE:')

#             members[uId] = {                               # members[키값] = 벨류 -> 이런식으로 추가한다
#                     'id': uId,
#                     'uPw': uPw,
#                     'uMail': uMail,
#                     'uPhone': uPhone
#                 }                      
#             print('SIGN-UP SUCCESS!!')

#         if DEV_MOD : print(f'members: {members}')          # 나중에 생략하고 싶으면 DEV_MOD = False로 바꾸자 0

#     elif selectedMenuNumint == SIGN_IN:
#         signInCount = 1
#         while True:                             # 2. 로그인        
#             uId = input('input member ID:')
#             uPw = input('input member PW:')          
                    
#             if uId in members:                      # not in 일 경우 없으면 True 있으면 False
#                 uInfo = members[uId] 
#                 if uInfo['uPw'] == uPw:
#                     print('SIGN-IN SUCCESS!!')
#                 else:
#                     print('SIGN-IN FAIL!!') 
#                     signInCount += 1
#                     if signInCount > 3:
#                         print('3회 이상 틀렸어요!!')
#                         break
#             else:
#                 print('존재하지 않은 ID입니다. 다시 확인하세요.')

#     elif selectedMenuNumint == PRINT_MY_INFO:                  # 3. 나의 정보 출력
#         uId = input('input member ID:')
#         uPw = input('input member PW:')          

#         if uId in members:                      
#             uInfo = members[uId] 
#             if uInfo['uPw'] == uPw:
#                 print('SIGN-IN SUCCESS!!')

#                 print('-' * 30)
#                 for key, value in uInfo.items():
#                     print(f'{key}: {value}')
#                 print('-' * 30)

#             else:
#                 print('SIGN-IN FAIL!!')
#         else:
#             print('존재하지 않은 ID입니다. 다시 확인하세요.')
#     elif selectedMenuNumint == PRINT_ALL_MEMBER_INFO:          # 4. 모든 회원 정보 출력
#         for key, value in members.items():
#             print(f'{key}님의 정보------')
#             for key1, value1 in value.items():
#                 print(f'{key}: {value1}')
#             print('_' * 30)
#     elif selectedMenuNumint == SYSTEM_SHUTDOWN:                # 99. 종료
#         flag = False
#         print('Good bye~')