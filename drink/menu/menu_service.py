from menu import config as menu_config
from menu import menu_register
from menu import menu_modify
from menu import menu_delete
from menu import menu_check
import database

class MenuService:
    def __init__(self):
        self.filename = "menus.json"
        self.menudict = {}

        self.menudict = database.save_data(self.filename, self.menudict)

    def register(self):
        menu_register.menuResister(self.menudict)
        database.save_data(self.filename, self.menudict)
    def checkOrder(self):
        menu_check.menuInfos(self.menudict)
    def menuModify(self):
        menu_modify.menuModify(self.menudict)
        database.save_data(self.filename, self.menudict)
    def menuDelete(self):
        menu_delete.menuDelete(self.menudict)
        database.save_data(self.filename, self.menudict)

    def run (self):
        
        flag = True
        while flag:
            selectedNum = int(input('1. 메뉴 등록, 2. 메뉴 조회, 3.메뉴 수정, 4.메뉴 삭제, 99.종료' ))

            if selectedNum == menu_config.MENU_REGISTER:
                self.register(self.menudict)  
            elif selectedNum == menu_config.CHECK_INFO:
                self.menuCheck(self.menudict)
            elif selectedNum == menu_config.MENU_MODIFY:
                self.menuModify(self.menudict)
            elif selectedNum == menu_config.MENU_DELETE:
                self.menuDelete(self.menudict)
            elif selectedNum == menu_config.SYSTEM_OUT:
                flag = False
            else:
                print('오타거나 없는 메뉴입니다. 다시 입력해주세요.')
                return

if __name__=="__main__":
    MenuService().run()
          