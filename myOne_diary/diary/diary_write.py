import session
from diary import diary_service
import login_Block

class WriteDiary:
    def __init__(self):
        self.diaries = {}

    def write(self):

        if login_Block.loginBlockSystem() == True:
            return   
        else:
            self.diaries = diary_service.DiaryService().load_diaries()

            writingDiary = input('일기를 작성해주세요.')

            uId = session.getloginedMember()

            if uId not in self.diaries:
                self.diaries[uId] = {
                        'diary': []
                    }
    
            self.diaries[uId]['diary'].insert(0, writingDiary)

            diary_service.DiaryService().save_diaries(self.diaries)
            
            print('작성완료!')