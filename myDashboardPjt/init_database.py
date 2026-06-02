import os
import json
import session

class InitDatabase:

    def __init__(self):
                         
        self.dictDates = {}
    
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')
        
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'datas.json')
        print(f'self.dbFile: {self.dbFile}')
        
    def confirmTool(self):        
            if not os.path.exists(self.dbFile):       
                self.save_datas(self.dictDates) 
            else:
                self.memos = self.load_datas() 

    def save_datas(self, dictDates): 
                with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                    json.dump(dictDates, f, ensure_ascii = False, indent = 4)  
    
    def load_datas(self):   
                with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                    return json.load(f)  
                
    def isMyMemos(self):
            allDatas = self.load_datas()
            if session.getSigninedMemberId() in allDatas:
                return True 
                
            return False        
                
  