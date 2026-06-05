class SignIn:
    def __init__(self):
      self.memberdict = {}

    def signIn(self):
        mId = input('ID 입력 :')
        mPw = input('PW 입력 : ')

        flag = True
        while flag:
            if mId in self.memberdict and self.memberdict[mId]['mPw'] == mPw:
                print('로그인 성공!')
                flag = False
                return
            else:
                print('로그인 실패 오타거나 없는 아이디 비번입니다')
          
        