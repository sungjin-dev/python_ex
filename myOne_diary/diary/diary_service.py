import session
import os
import json
from diary import config as diary_config
from diary import diary_write
from diary import diary_read
from diary import diary_delete
from diary import diary_update
from diary import diary_opencv

class DiaryService:
    def __init__(self):
        self.diaries = {}
        self.init_database() 

    def init_database(self):
    
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))

        ROOT_DIR = os.path.dirname(BASE_PATH)

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'diaries.json')

        if not os.path.exists(self.dbFile):       
            self.save_diaries(self.diaries) 
        else:
            self.diaries = self.load_diaries()   
     
    def save_diaries(self, diaries):    
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(diaries, f, ensure_ascii = False, indent = 4)  
   
    def load_diaries(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)
            
    def isMyMemos(self):
        allMemos = self.load_diaries()
        if session.loginedMember() in allMemos:
            return True             
        return False  

    def run(self):
        
        flag = True
        while flag:
            selectedNum = int(input('1. Write  2. Read 3. Delete , 4. Update, 5. Show, 99. System-out'))

            if selectedNum == diary_config.WRITE:
                diary_write.WriteDiary().write()
            elif selectedNum == diary_config.READ:
                diary_read.ReadDiary().read()
            elif selectedNum == diary_config.DELETE:
                diary_delete.DeleteDiary().delete()
            elif selectedNum == diary_config.UPDATE:
                diary_update.UpdatingMemo().update()
            elif selectedNum == diary_config.SHOW:
                diary_opencv.Opencv().diaryOpencv()
            elif selectedNum == diary_config.SYSTEM_OUT:
                print('종료합니다.')
                flag = False
            else:
                print('오타입니다. 다시 입력해주세요.')