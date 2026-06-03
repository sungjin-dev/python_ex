import session
from memo import memo_service

class ReadMemo:

    def __init__(self):
        self.memos = {}

    def read(self):      
        self.memos = memo_service.MemoService().load_memos()  
        myMemos = self.memos[session.getSigninedMemberId()]  
        for idx, memo in enumerate(myMemos):
            print(f'[{idx+1}] {memo}')