from menu import config as memu_config
from menu import menu_register
from menu import memu_modify
import database

class menuService:
    def __init__(self):
        self.filename = "menus.json"
        self.menudict = {}

        self.menudict = database.save_data(self.filename, self.menudict)

    def register(self):
        menu_register.menuResister(self.menudict)
        database.save_data(self.filename, self.menudict)
    def checkOrder(self):
        pass
    def menuModify(self):
        memu_modify.
        database.save_data(self.filename, self.menudict)
    def menuDelete(self):
        database.save_data(self.filename, self.menudict)

    def run (self):
        
        flag = True

        while flag:

            selectedNum = int(input('1. 메뉴 등록, 2. 메뉴 조회, 3.메뉴 수정, 4.메뉴 삭제, 99.종료' ))

            if selectedNum == memu_config.MENUREGISTER:
                self.register(self.menudict)  
            elif selectedNum == memu_config.MENECHECK:
                pass
            elif selectedNum == memu_config.MENUMODIFY:
                pass
            elif selectedNum == memu_config.MENUDELETE:
                pass
            elif selectedNum == memu_config.SYSTEM_OUT:
                flag = False
          


