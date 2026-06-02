from util import util_time
import session
from member import member_service

class InputMemberData:
    def __init__ (self):

        self.Members = {}
        
    def collectUserdata(self):    

        mId = input('Input new member ID:')

        if mId in self.Members:
                print('이미 사용중인 ID입니다.')
                return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')

        RegDate = util_time.getCurrentDateTime()
        ModDate = util_time.getCurrentDateTime()

        newMembers = {
            'mId' : mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mRegDate': RegDate,  
            'mModDate': ModDate    
            }

        self.Members[mId] = newMembers  
        
        # DB(members.json)에 새회원정보 저장
        member_service.MemberService().save_members(self.Members)

        print('MEMBER SIGN-UP SUCCESS!!')
        # session.signinedMemberId = mId

        session.setSigninedMemberId(mId)