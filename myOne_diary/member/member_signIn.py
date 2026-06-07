import session

def signIn(memberdict):
    
    flag = True
    while flag:

        mId = input('ID 입력 :')
        mPw = input('PW 입력 : ')
        
        if mId in memberdict and memberdict[mId]['mPw'] == mPw:
            print('로그인 성공!')
            session.signinedMember(mId)
            flag = False
            return
        else:   
            print('로그인 실패 오타거나 없는 아이디 비번입니다')
        
        