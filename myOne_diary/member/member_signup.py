import session
from util import util_time 

def signUp(memberdict):

    mId = input('ID 입력 :')

    if mId in memberdict:
        print('이미 사용중인 ID입니다.')
        return
    
    mPw = input('PW 입력 : ')
    mEmail = input('Email 입력 : ')
    mPhone = input('Phone 입력 : ')
    mRdate = util_time.getCurrentTime()
    
    members = {
        'mId' : mId,
        'mPw' : mPw,
        'mEmail' : mEmail,
        'mPhone' : mPhone,
        'mRdate' : mRdate
    }

    memberdict[mId] = members

    session.signinedMember(mId)

    return memberdict
    
        




