from util import util_time
from member import config as member_config
import config as root_config
import os
import json
import session
from member import member_input
from member import member_login
from member import member_modify
from member import member_delete

class MemberService:
    def __init__(self):
        self.members = {}   
        self.init_database()

    def sign_up(self):
        member_input.InputMemberData().collectUserdata()

    def sign_in(self):
        member_login.LoginSystem().login_in()    

    def sign_out(self):
        session.setSigninedMemberId()  
        print('SIGN-OUT SUCCESS!!')

    def modify(self):
        member_modify.ModifymemberData().modifying()
    
    def delete(self):
        member_delete.DeleteUser().delete()
        
    def run(self):
        flag = True
        while flag:
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
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json') # os.path.join 윈도우인지 맥인지 스스로 파악
        print(f'self.dbFile: {self.dbFile}')  # 확인용 디버깅 코드 
        # 3개의 조각을 줄 테니 완벽한 파일 주소로 만들어줘 C:\myDashboardPjt\db\members.json
        if not os.path.exists(self.dbFile):   # os.path.exists() : True or False 반환 
            self.save_members(self.members)
        else:
            self.members = self.load_members() # 있다면 기존 데이터를 내 가방으로
    #  게임의 '저장하기', '불러오기
    def save_members(self, members):   # 최신 데이터를 json파일에 덮어쓰기
        with open(self.dbFile, 'w', encoding= 'utf-8') as f:
            json.dump(members, f, ensure_ascii = False, indent = 4)   

    def load_members(self):     # 파이썬이 읽을 수 있도록 딕셔너리로 불러옴
        with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
            return json.load(f)
                                         
if __name__ == "__main__":
    memberService = MemberService()
    memberService.run()

# cd .\myDashboardPjt\


'''
json.dump(): 파이썬 딕셔너리 ➡️ 파일로 내보내기 (포장해서 창고에 넣기)

json.load(): 파일 ➡️ 파이썬 딕셔너리로 가져오기 (창고에서 꺼내오기)
'''

# mId = input('Input new member ID: ')
#         mPw = input('Input new member PW: ')
#        # 시작하자마자 창고에서 최신 데이터를 새로 불러옵니다
#         self.members = self.load_members()
#         if mId in self.members and self.members[mId]['mPw'] == mPw:
#             print('MEMBER SIGN-IN SUCCESS!!')
#             session.signinedMemberId = mId
#             if root_config.DEV_MOD:
#                 print(f'session.signinedMemberId: {session.signinedMemberId}')
#             return
        
#         print('MEMBER SIGN-IN FAIL!!') 