from member import config as member_config
from member import member_signup
from member import member_signIn
from member import member_signout
from member import member_modify
from member import member_delete
import dbfile_manager
import session

class MemberService:
    def __init__(self):
        self.fileName = "members.json"
        self.memberdict = {}  

        self.memberdict = dbfile_manager.load_data(self.fileName, self.memberdict)

    def sign_up(self):
        member_signup.signUp(self.memberdict)
        dbfile_manager.save_data(self.fileName, self.memberdict)
    def sign_in(self):
        member_signIn.signIn(self.memberdict)
    def sign_out(self):
        member_signout.signOut()
    def modify_info(self):
        member_modify.modify(self.memberdict)
        dbfile_manager.save_data(self.fileName, self.memberdict)
    def delete_info(self):
        member_delete.delete(self.memberdict)
        dbfile_manager.save_data(self.fileName, self.memberdict)

    def run(self):

        flag = True

        while flag:  
            if session.getloginedMember() == '':
                selectedUserNum = int(input('1. Sign-Up, 2.Sign-In  99.System-Out  '))
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

    if __name__ == "__main__":
        run()