from config_dir import config
from member import session
from db import member_db
from db import diary_db
from member import member_dumy
from datetime import datetime
import copy

if config.DEV_MOD:                    # 프로그램 시작 전 가장 먼저 실행 중요!         
    member_dumy.dumyInit()                    
    print(f'memberDB: {member_db.memberDB}')
    print(f'diaryDB: {diary_db.diaryDB}')

now = datetime.now()    

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # log out 상태
        menuNum = int(input('1.sign-up   2.log-in   6.write   7.read   99.end'))
    else:
        # log in 상태
        menuNum = int(input('3.modify   5.log-out   4.delete  6.write   7.read  99.end'))

    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')
        uRegDate = datetime.now()             # 가입일

        member_db.memberDB[uId] = {   # member_db 파일에 있는 memberDB라는 비어있는 딕셔너리 창고로 찾아가라
            'uId': uId,               # uId를 직접 키(KEY)로 지정함.                                  
            'uPw': uPw,                         
            'uMail': uMail,
            'uPhone': uPhone,
            'uRegDate': uRegDate
        }
        print('New member sign-up success!!')
       
        # print(now)

        # if config.DEV_MOD:
        #     print(f'memberDB: {member_db.memberDB}')      # member_db.memberDB 수집한 딕셔너리값
        diary_db.diaryDB[uId] = []         # 정상적은 루트면 이 과정을 거침, 더미변수들은 더미함수에서 추가로 지정필요
        # if config.DEV_MOD:
        #     pass

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')

        if uId in member_db.memberDB:                   # 수집된 딕셔너리에서 아이디 확인                              
            if member_db.memberDB[uId]['uPw'] == uPw:
               
                print('sign-in success!!')
                print(now)
                session.signInedMemberId = uId  # 외부 모듈을 가져와서(import) 그 안의 변수를 직접 수정하면, 프로그램 전체에서 그 변경된 값을 공유 (자바나 C이런건 static)
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        id, pw, mail, phone 이 중에서 어떤 정보들만 수정가능케 할 것인지 정해야 합니다. 
        id: x, 또한 이미 탈퇴한 회원의 ID라도 절대/변경 사용할 수 없습니다. 
        pw: 절대 수정이 불가하지는 않습니다. 하지만 쉽게 변경할 수는 없습니다. 
        mail: 비교적 단순하게 수정할 수 있습니다.
        phone : 비교적 단순하게 수정할 수 있습니다. 
        '''

        uPw = input('Please input member PW: ')
        uMail = input('Please input member MAIL: ')
        uPhone = input('Please input member PHONE: ')
        uRegDate = now
        '''
            - member_db 모듈에 있는 memberDB 딕셔너리에 회원정보를 변경한다. 
            - 지금 현재 memberDB에는 'gildong', 'chanho'회원이 있죠? 네 
            - 현재 로그인되어있는 회원 정보를 불러와서 그 정보를 수정
            - 즉, session.signInedMemberId에서 현재 로그인 되어 있는 회원 ID를 가져와서 사용하면 됩니다. 
        '''
        currentSignInedMemberID = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberID]
        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: memberInfo: {memberInfo}')

    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
        '''
        - 현재 로그인 되어 있는 회원의 ID를 session.signInedMemberId에서 가져와서
        - 해당하는 회원의 정보를 member_db.memberDB에서 삭제합니다.
        '''
        currentSignInedMemberID = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberID]

        print('Member info deleted!!')
        session.signInedMemberId = '' 
        if config.DEV_MOD:print(f'member_db.memberDB: {member_db.memberDB}')

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out')

        print('sign-out success!!')
        
        session.signInedMemberId = '' 

    elif menuNum == config.DIARY_WRITE:
        print('6.write')    

        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!!')

        else:
            while True:
                diaryTxt = input('10글자 이하의 짧은 일기를 작성하세요.')
                if len(diaryTxt) > 10:
                    print(f'10글자 초과했어요.({len(diaryTxt)})')
                else:                                                                                      
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt) # 처음부터 추가하려면 insert(0, diaryTxt)               
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break

    elif menuNum == config.DIARY_READ:
        print('7.read')   
        
        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!!')

        else:  
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            deepCopyedDiaries = copy.deepcopy(myDiaries)       
            deepCopyedDiaries.reverse()                   # 순서 바뀐다 reverse() 반환하는 아이템이 없음                              
            for idx,diaryTxt in enumerate(deepCopyedDiaries):
                print(f'({idx+1}): {diaryTxt}')           # 실제로는 0번부터가 아니라 1번부터가 더 직관적이라서

                reversed() 내장 함수 사용 (가장 추천)

# 파이썬에서 원본 데이터를 직접 수정(In-place)하는 메서드들은 의도적으로 None을 반환하도록 설계되어 있습니다.

# [::-1] 은 뒤집힌 새로운 리스트를 반환함  # [시작:끝:보폭]
for idx, diaryTxt in enumerate(deepCopyedDiaries[::-1]):
    print(f'({idx+1}): {diaryTxt}')

    폭이 음수(-1)일 때 시작을 생략하면, 파이썬은 자동으로 "리스트의 맨 끝"을 시작점으로 잡습니다.
    두 번째 빈칸 (끝): 값을 생략했습니다. 보폭이 음수일 때 끝을 생략하면, 파이썬은 자동으로 "리스트의 맨 처음"까지 가도록 설정합니다.


'''         
# ********* 중요 *****************
diary_db.diaryDB[session.signInedMemberId] 
-> 딕셔너리에 추가하는게 아니라 딕셔너리 안의 리스트에 추가하는 것임
diaryDB.append(diaryTxt)  이런 구조는 당연히 x


🏢 비유로 이해하는 현재 상황 (낙하산 인사)
정상적인 진짜 유저 (회원가입 기능):

회사의 '정문 안내데스크(회원가입 함수)'를 거쳐서 들어옵니다.

안내데스크 직원은 유저의 신상정보를 사원 명부(memberDB)에 적고, 
활동을 시작할 수 있게 빈 업무 수첩(diaryDB = [])을 기본 지급합니다.

더미 유저 (dumyInit 함수):

개발자의 편의를 위해 정문을 거치지 않고 '뒷문(더미 초기화)'으로 
바로 사무실에 꽂아 넣은 낙하산 직원들입니다.

안내데스크를 안 거쳤기 때문에 업무 수첩(diaryDB = [])을 받지 못했습니다.

이대로 놔두면 나중에 일하라고 할 때(일기 쓰기) 에러가 나니까, 
뒷문 관리자(dumyInit)가 부랴부랴 "아, 얘네도 수첩은 줘야지!" 하면서 
빈 수첩을 챙겨주고 있는 상황입니다.
'''  
















 # 딕셔너리에도 함수 들어갈 수 있다. 

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y


# 2. 계산기 리모컨(딕셔너리)에 기호별로 함수를 등록합니다.
calculator = {
    "+": plus,
    "-": minus,
    "*": multiply
}

num1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산 기호를 입력하세요 (+, -, *): ")
num2 = int(input("두 번째 숫자를 입력하세요: "))

if operator in calculator:
    # calculator[operator] 로 함수를 꺼내고, 뒤에 (num1, num2)를 붙여서 바로 실행!
    result = calculator[operator](num1, num2)

    print(f" 계산 결과: {num1} {operator} {num2} = {result}")
else:
    print("지원하지 않는 연산 기호입니다.")

# oneDiary
#  - member service
#    - sign-up, sign-in, modify, delete
#  - diary service
#    - write, read

'''
test   파일을 새로 만들지 않는 경우면 commit -am "" 이걸로 한번에 가능
git add .; git commit -m "create temp.py" -> 새로운 파일 만들었으면 이렇게 가능
git add .; git commit -m "modify temp.py"; git push origin main  
https://hoazzinews.tistory.com/210
'''





