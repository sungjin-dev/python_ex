import session
import config as root_config
from member import member_service

class LoginSystem:
    def __init__ (self):
         self.members = {}

    def login_in(self): 

        mId = input('Input new member ID: ')
        mPw = input('Input new member PW: ')

       # 시작하자마자 창고에서 최신 데이터를 새로 불러옵니다
        self.members = member_service.MemberService().load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('MEMBER SIGN-IN SUCCESS!!')
            session.signinedMemberId = mId
            if root_config.DEV_MOD:
                print(f'session.signinedMemberId: {session.signinedMemberId}')
            return
        
        print('MEMBER SIGN-IN FAIL!!') 