import session

def delete(memberdict):
      
    flag = True
    while flag:
        mId = input('삭제할 아이디를 다시 입력해주세요.')
        mPw = input('삭제할 비밀번호를 다시 입력해주세요.')

        if mId in memberdict and memberdict[mId]['mPw'] == mPw:
                del memberdict[mId]
                session.signinedMember('')
                break             
        else: 
            ('아이디와 비번을 확인해주세요.')
    
    return memberdict