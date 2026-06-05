from diary import diary_service
import session

class ReadDiary:

    def __init__(self):
        self.diaries = {}

    def read(self):      
        self.diaries = diary_service.DiaryService().load_diaries()  
        myDiaries = self.diaries[session.getloginedMember()]  
        for idx, diary in enumerate(myDiaries):
            print(f'[{idx+1}] {diary}')