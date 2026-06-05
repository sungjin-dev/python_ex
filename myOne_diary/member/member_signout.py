import session

class SignOut():
    def __init__(self):
      self.memberdict = {}

    def signOut(self):

        if session.getloginedMember() == True:
            session.signinedMember() == ''
        else:
            print('로그인한 계정이 없습니다.')
            return