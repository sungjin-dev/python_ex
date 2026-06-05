import session
from util import util_time 
from member import member_service

class Signup:
    def __init__(self):
        self.memberdict = {}
    
    def signup(self):

        mId = input('ID 입력 :')

        if mId in self.memberdict:
            print('이미 사용중인 ID입니다.')
            return
        
        mPw = input('PW 입력 : ')
        mEmail = input('Email 입력 : ')
        mPhone = input('Phone 입력 : ')
        mRdate = util_time.getCurrentTime()
       
        self.members = {
            'mId' : mId,
            'mPw' : mPw,
            'mEmail' : mEmail,
            'mPhone' : mPhone,
            'mRdate' : mRdate
        }

        self.memberdict[mId] = self.members

        member_service.MemberService().save_members(self.memberdict) 

        session.signinedMember(mId)

        




