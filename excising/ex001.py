from config_dir import config
from member import session
from db import member_db
from member import member_dumy

if config.DEV.MOD: 
    member_dumy.memberDumyInit()
print('memberDB: {member_db.memberDB}')

def memberDumyInit():       
    for n in range(len(ids)):  
        member_db.memberDB[ids[n]] = {
        'uId': ids[n],
        'uPw': pws[n],
        'uMail': mails[n],
        'uPhone': phones[n],

flag = True

while flag:
    menuNum = ''
    if session.signInedMemberId == '':
        menuNum = int(input('1.sign-up 2.sign-in 99.end'))
    else:
        menuNum = int(input('3.modify 5.sign-out  99.end'))
    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('Please input new member ID:')
        uPw = input('Please input new member PW:')
        uMaill = input('Please input new member MAIL:')
        uPhone = input('Please input new member PHONE:')
    
        member_db.memberDB[uId] = {       # 딕셔너리의 인풋 데이터를 수집하는 단계
            'uId':uId,                    # uId를 직접 키(KEY)로 지정함.
            'uPw':uPw,
            'uMaill':uMaill,
            'uPhone':uPhone
        }

        print('new member sign-up success!!')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')   # member_db.memberDB 수집한 딕셔너리값
        elif menuNum == config.SIGN_IN: 
            print('2.sign-in')                 
            uId = input('Please input member ID: ')    
            uPw = input('Please input member PW: ') 

            if uId in member_db.memberDB:      # 수집된 딕셔너리에서 아이디 확인
                if member_db.memberDB[uId]['uPw'] == uPw: 
                    #  dict[key][value] == value 이런 구조면 True or False 
                    #  dict[key][value] = value  밸류값 변경
                    print('sign-in success')
                else: 
                    print('sign-in fail!! -- PW error')
            else:
                print('sign-in fail!! -- ID error')

        elif menuNum == config.MEMBER_MODIFY: 
            print('3.modify')
        elif menuNum == config.MEMBER_DELETE: 
            print('4.delete')
        elif menuNum == config.SYSTEM_OUT: 
            print('99.end')
            flag = False
        elif menuNum == config.SIGN_OUT: 
            print('5.sign_out')



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


    