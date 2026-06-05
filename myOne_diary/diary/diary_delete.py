from diary import diary_service
import session
import login_Block

class DeleteDiary:
    def __init__(self):
        self.diaries = {}

    def delete(self):
        
        if login_Block.loginBlockSystem() == True:
            return   
        else:
            self.diaries = diary_service.DiaryService().load_diaries()
            
            mydiaries = self.diaries[session.getloginedMember()]  

            for idx, diaries in enumerate(mydiaries):
                print(f'[{idx+1}] {diaries}')
            selectedNumber = int(input('삭제할 다이어리를 선택해주세요.'))
            mydiaries.pop(selectedNumber-1)
    
  