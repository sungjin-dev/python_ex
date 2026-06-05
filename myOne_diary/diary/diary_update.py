from diary import diary_service
import session

class UpdatingMemo:    

    def __init__(self):
        self.diaries = {}
        
    def update(self):       
        self.diaries = diary_service.DiaryService().load_diaries()   
        myDiaries = self.diaries[session.getloginedMember()]  
        for idx, diaries in enumerate(myDiaries):
            print(f'[{idx+1}] {diaries}')
        selectedNumber = int(input('변경하고 싶은 다이어리를 골라주세요.'))
        Updatingdiary = input('다이어리 수정해주세요. ')
        myDiaries[selectedNumber-1] = Updatingdiary   

        diary_service.DiaryService().save_diaries(self.diaries)
        print('변경 완료!')

        