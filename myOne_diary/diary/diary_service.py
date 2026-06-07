from diary import config as diary_config
from diary import diary_write
from diary import diary_read
from diary import diary_delete
from diary import diary_update

import dbfile_manager

class DiaryService:
    def __init__(self):
        self.fileName = "diary.json"
        self.diarydict = {}  

        self.diarydict = dbfile_manager.load_data(self.fileName, self.diarydict)

    def run(self):
        
        flag = True
        while flag:
            selectedNum = int(input('1. Write  2. Read,  3. Delete,  4. Update,  99. System-out  ' ))

            if selectedNum == diary_config.WRITE:
                diary_write.write(self.diarydict)
                dbfile_manager.save_data(self.fileName, self.diarydict)
            elif selectedNum == diary_config.READ:
                diary_read.pictureDiary()
            elif selectedNum == diary_config.DELETE:
                diary_delete.delete(self.diarydict)
                dbfile_manager.save_data(self.fileName, self.diarydict)
            elif selectedNum == diary_config.UPDATE:
                diary_update.update(self.diarydict)
                dbfile_manager.save_data(self.fileName, self.diarydict)   
            elif selectedNum == diary_config.SYSTEM_OUT:
                print('종료합니다.')
                flag = False
            else:
                print('오타입니다. 다시 입력해주세요.')