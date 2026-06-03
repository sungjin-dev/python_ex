import session
import os
import json
from memo import config as memo_config
import login_break
from memo import memo_write 
from memo import memo_read
from memo import memo_delete
from memo import memo_update
from memo import memo_management 

class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database() 

    def init_database(self):
    
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):       
            self.save_memos(self.memos) 
        else:
            self.memos = self.load_memos()   
     
    def save_memos(self, memos):    
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(memos, f, ensure_ascii = False, indent = 4)  
   
    def load_memos(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)
            
    def isMyMemos(self):
        allMemos = self.load_memos()
        if session.getSigninedMemberId() in allMemos:
            return True 
             
        return False  

    def run(self):
        login_break.commition()  
        memo_management.MemoManagement().isMemos()

        menuNum = int(input('1.WRITE   2.READ   3.UPDATE  4.DELETE    99.SERVICE-OUT'))

        flag = True
        while flag:
            
            if menuNum == memo_config.WRITE:         
                memo_write.WriteMemo().write()

            elif menuNum == memo_config.READ:
                memo_read.ReadMemo().read()
            
            elif menuNum == memo_config.UPDATE:
                memo_update.UpdatingMemo().update()
          
            elif menuNum == memo_config.DELETE:
                memo_delete.DeleteMemo().delete()
            
            elif menuNum == memo_config.SERVICE_OUT:
                flag = False              

if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()   
