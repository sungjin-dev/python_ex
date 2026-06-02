from util import util_time
import session
from member import member_service

class InputMemberData:
    def __init__ (self):

        self.Members = {}
        
    def collectUserdata(self,ID,PW,MAIL,PHONE):

        ID = input('Input new member ID:')

        if ID in self.Members:
            print('이미 사용중인 ID입니다.')
            return

        PW = input('Input new member PW: ')
        MAIL = input('Input new member MAIL: ')
        PHONE = input('Input new member PHONE: ')

        RegDate = util_time.getCurrentDateTime()
        ModDate = util_time.getCurrentDateTime()

        newMembers = {
            'mId' : ID,
            'mPw': PW,
            'mMail': MAIL,
            'mPhone': PHONE,
            'mRegDate': RegDate,  
            'mModDate': ModDate    
        }

        self.Members[ID] = newMembers  
        
        # DB(members.json)에 새회원정보 저장
        member_service.MemberService().save_members(self.Members)

        print('MEMBER SIGN-UP SUCCESS!!')
        # session.signinedMemberId = mId

        session.setSigninedMemberId(ID)