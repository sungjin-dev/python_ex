import config as root_config
from member import member_service
from diary import diary_service

def main():

    flag = True
    while flag:   
        selectedUserNum = int(input('1. Member, 2.Diary , 99.System-Out '))

        if selectedUserNum == root_config.MEMBER:
            member_service.MemberService().run()
        elif selectedUserNum == root_config.DIARY:
            diary_service.DiaryService().run()
        elif selectedUserNum == root_config.SYSTEM_OUT:
            print('프로그램을 종료합니다')
            flag = False
            return
        else:
            print('오타입니다. 다시 입력해주세요.')

if __name__ == "__main__":
    # member_service.MemberService().run()
    diary_service.DiaryService().run()
