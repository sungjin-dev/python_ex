import session
import os
import json
from memo import config as memo_config
import config as root_config

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
    # 애플리케이션의 데이터를 JSON 파일에 저장하는 것 
    def save_memos(self, memos):     # 그냥 save_memos는 write 성격으로 간주하기 
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(memos, f, ensure_ascii = False, indent = 4)  
    # JSON파일을 읽어서 애플리케이션으로 데이터를 가져오는 것
    def load_memos(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)
            
    def isMyMemos(self):
        allMemos = self.load_memos()
        if session.getSigninedMemberId() in allMemos:
            return True 
             
        return False        
            
    def run(self):
        
        if session.getSigninedMemberId() == '':
            print('Please SIGN-IN!!')
            return
        
        flag = True
        while flag:
            if not self.isMyMemos():
                 self.memos[session.getSigninedMemberId()] = []
                 self.save_memos(self.memos)
                     
            menuNum = int(input('1.WRITE   2.READ   3.UPDATE  4.DELETE    99.SERVICE-OUT'))

            if menuNum == memo_config.WRITE:
                newMemo = input('Write new memo')
                self.memos = self.load_memos()
                myMemos = self.memos[session.getSigninedMemberId()]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos() : {self.load_memos()}')

            elif menuNum == memo_config.READ:
                self.memos = self.load_memos()   # dic
                myMemos = self.memos[session.getSigninedMemberId()]  # list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')

            elif menuNum == memo_config.UPDATE:
                self.memos = self.load_memos()   # dic
                myMemos = self.memos[session.getSigninedMemberId()]  # list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')
                selectedNumber = int(input('Please select the number to modify: '))
                memo = input('Edit memo: ')
                myMemos[selectedNumber-1] = memo   # idx+1 인위적으로 +1했으니까  

                self.save_memos(self.memos)
                print('MODIFY SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')

            elif menuNum == memo_config.DELETE:
                self.memos = self.load_memos()   # dic
                myMemos = self.memos[session.getSigninedMemberId()]  # list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')
                selectedNumber = int(input('Please select the number to delete: '))
                myMemos.pop(selectedNumber-1)
                self.save_memos(self.memos)
                print('DELETE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')

            elif menuNum == memo_config.SERVICE_OUT:
                flag = False

if __name__ == '__main__':
    bankService = MemoService()
    bankService.run()   

    # python -m memo.memo_service