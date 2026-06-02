import os
import json
import session

class InitDatabase:
    

    def __init__(self, types):
                         
               self.types = types

               types = {}
    
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    print(f'BASE_PATH: {BASE_PATH}')

    ROOT_DIR = os.path.dirname(BASE_PATH)
    print(f'ROOT_DIR : {ROOT_DIR}')

    types = os.path.join(ROOT_DIR, 'db', 'memos.json')
    print(f'self.dbFile: {types}')

    def confirmTool(self, types):        
        if not os.path.exists(types):       
            self.save_types(types) 
        else:
            self.memos = self.load_types() 

    def save_types(self, types): 
            with open(self.types, 'w', encoding= 'utf-8') as f:
                json.dump(types, f, ensure_ascii = False, indent = 4)  
  
    def load_types(self):   
            with open(self.types, 'r' , encoding = 'utf-8') as f:
                return json.load(f)  
            
    def isMyMemos(self):
        allDatas = self.load_types()
        if session.getSigninedMemberId() in allDatas:
            return True 
             
        return False        
            
    def run(self):
        
        if session.getSigninedMemberId() == '':
            print('Please SIGN-IN!!')
            return