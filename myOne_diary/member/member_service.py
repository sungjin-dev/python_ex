from member import config as member_config
from member import member_signup
from member import member_signIn
from member import member_signout
from member import member_modify
from member import member_delete
import session
import os
import json

class MemberService:
    def __init__(self):
        self.memberdict = {}   
        self.init_database()

    def sign_up(self):
        member_signup.Signup().signup()
    def sign_in(self):
        member_signIn.SignIn().signIn()
    def sign_out(self):
        member_signout.SignOut().signOut()
    def modify_info(self):
        member_modify.Modify().modify()
    def delete_info(self):
        member_delete.Delete().delete()

    def run(self):

        flag = True
        while flag:  

            if session.getloginedMember() == '':
                selectedUserNum = int(input('1. Sign-Up, 2.Sign-In 99.System-Out  '))
            else:
                selectedUserNum = int(input('3.Sign-out, 4.Modify 5.Delete, 99.System-Out  '))

            if selectedUserNum == member_config.SIGN_UP:
                self.sign_up()
            elif selectedUserNum == member_config.SIGN_IN:
                self.sign_in()
            elif selectedUserNum == member_config.SIGN_OUT:
                self.sign_out()
            elif selectedUserNum == member_config.MODIFY:
                self.modify_info()
            elif selectedUserNum == member_config.DELETE:
                self.delete_info()
            elif selectedUserNum == member_config.SYSTEM_OUT:
                print('프로그램을 종료합니다')
                flag = False
                return
            else:
                print('오타입니다. 다시 입력해주세요.')

    def init_database(self):  
      
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
     
        ROOT_DIR = os.path.dirname(BASE_PATH)
    
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json') 
        
        if not os.path.exists(self.dbFile):   
            self.save_members(self.memberdict)
        else:
            self.memberdict = self.load_members() 
    
    def save_members(self, members):   
        with open(self.dbFile, 'w', encoding= 'utf-8') as f:
            json.dump(members, f, ensure_ascii = False, indent = 4)   

    def load_members(self):     
        with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
            return json.load(f)

    if __name__ == "__main__":
        run()