import session
from memo import memo_service

class MemoManagement:
    def __init__(self):
        self.memos = {}
         
    def isMemos(self):   
        if not memo_service.MemoService().isMyMemos():
            self.memos[session.getSigninedMemberId()] = []
            memo_service.MemoService().save_memos(self.memos)          
    
    
    
