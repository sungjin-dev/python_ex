class Delete:
    def __init__(self):
      self.memberdict = {}

    def delete(self):
       
       flag = True
       while flag:
            mId = input('삭제할 아이디를 다시 입력해주세요.')
            mPw = input('삭제할 비밀번호를 다시 입력해주세요.')

            if mId in self.memberdict and self.memberdict[mId]['mPw'] == mPw:
                    del self.memberdict[mId]
                    break             
            else: 
                ('아이디와 비번을 확인해주세요.')