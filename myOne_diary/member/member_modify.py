class Modify:
    def __init__(self):
      self.memberdict = {}

    def modify(self):

        flag = True
        while flag:
            mId = input('변경하고 싶은 ID를 입력하세요.')
            mPw = input('변경하고 싶은 PW를 입력하세요.')
            mEmail = input('변경하고 싶은 EMAIL를 입력하세요.')
            mPhone = input('변경하고 싶은 PHONENUMBER를 입력하세요.')

            if mId in self.Members:
                print('이미 존재하는 ID입니다.')
            else:
                self.memberdict['mId'] = mId   
                self.memberdict[mId]['mPw'] = mPw
                self.memberdict[mId]['mEmail'] = mEmail
                self.memberdict[mId]['mPhone'] = mPhone
                break
                