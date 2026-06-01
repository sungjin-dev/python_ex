from util import util_time
from member import config as member_config
import config as root_config
import os
import json
import session

class MemberService:
    def __init__(self):
        self.members = {}   # 틀만 제공
        self.init_database()

    # 회원 가입 기능
    def sign_up(self):

        mId = input('Input new member ID:')

        # ID 중복체크를 할 때 self.members를 사용한다.
        if mId in self.members:
            print('이미 사용중인 ID입니다.')
            return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')

        newMember = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mRegDate': util_time.getCurrentDateTime(),  # 여기서 코드를 가져오는거보다는 외부로 빼는게 좋음
            'mModDate': util_time.getCurrentDateTime()   # 가장 최근에 변경된 시점 
        }

        self.members[mId] = newMember   
        
        # DB(members.json)에 새회원정보 저장
        self.save_members(self.members)

        print('MEMBER SIGN-UP SUCCESS!!')
        # session.signinedMemberId = mId

        session.setSigninedMemberId(mId)

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 로그인 기능
    def sign_in(self):

        mId = input('Input new member ID: ')
        mPw = input('Input new member PW: ')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('MEMBER SIGN-IN SUCCESS!!')
            session.signinedMemberId = mId
            if root_config.DEV_MOD:
                print(f'session.signinedMemberId: {session.signinedMemberId}')
            return
        
        print('MEMBER SIGN-IN FAIL!!') 

    # 회원 로그아웃 기능
    def sign_out(self):
        session.setSigninedMemberId()
        print('SIGN-OUT SUCCESS!!')

    # 회원 정보수정 기능
    def modify(self):

        mPw = input('Input member PW: ')
        mMail = input('Input member MAIL: ')
        mPhone = input('Input member PHONE: ')

        self.members = self.load_members()

        memberFormodify = self.members[session.getSigninedMemberId()]

        memberFormodify['mPw'] = mPw
        memberFormodify['mMail'] = mMail
        memberFormodify['mPhone'] = mPhone
        memberFormodify['mModDate'] = util_time.getCurrentDateTime()

        self.save_members(self.members)

        print(f'MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 탈퇴 기능
    def delete(self):
        
        confirm = input('정말 탈퇴하시겠습니까? [Y] or [N]')

        if confirm == 'Y':
            self.members = self.load_members()
            del self.members[session.getSigninedMemberId()]
            self.save_members(self.members)
            session.setSigninedMemberId()
            print('DELETE SUCCESS')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    def run(self):

        flag = True

        while flag:

            # if session.signinedMemberId == '':
            if session.getSigninedMemberId() == '':

                menuNum = int(input('1. SIGN-UP  2.SIGN-IN   99.SERVICE-OUT ')) 
            else:
                menuNum = int(input('3.SIGN-OUT  4.MODIFY  5. DELETE  99.SERVICE-OUT ')) 
            
            if menuNum == member_config.SIGN_UP:
                self.sign_up()

            elif menuNum == member_config.SIGN_IN:
                self.sign_in()
                
            elif menuNum == member_config.SIGN_OUT:
                self.sign_out()

            elif menuNum == member_config.MODIFY:
                self.modify()
             
            elif menuNum == member_config.DELETE:
                self.delete()

            elif menuNum == member_config.SERVER_OUT:
                flag = False    
                
    def init_database(self):  # 파일을 만들면서 빈 딕셔너리 만들어줘

        # 현재 파일 위치       절대값 경로
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        #db/memebers.json                    폴더명   파일명
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_members(self.members)
        else:
            self.members = self.load_members()

    def save_members(self, members):   # {}
        with open(self.dbFile, 'w', encoding= 'utf-8') as f:
            json.dump(members, f, ensure_ascii = False, indent = 4)   

    def load_members(self):    # 게임 load와 똑같음. 누적해서 데이터 쌓아서 불러오기
        with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
            return json.load(f)
                                         
if __name__ == "__main__":
    memberService = MemberService()
    memberService.run()

# python -m member.member_service

# cd .\myDashboardPjt\
# python -m member.member_service

