import session 

def loginBlockSystem():
    if session.getloginedMember() == '':
        print('로그인부터 하세요.')
        return True
    else:
        return False
    

