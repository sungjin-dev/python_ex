import session
  
def signOut():

    if session.getloginedMember() == True:
        session.signinedMember('')
        print('로그아웃되었습니다.')
    else:
        print('로그인한 계정이 없습니다.')
        