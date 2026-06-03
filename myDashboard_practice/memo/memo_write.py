import session
import config as root_config
from memo import memo_service

class WriteMemo:
    def __init__(self):
        self.memos = {}
        
    def write(self):       
        newMemo = input('Write new memo')
        self.memos = memo_service.MemoService().load_memos()
        myMemos = self.memos[session.getSigninedMemberId()]
        myMemos.insert(0, newMemo)

        memo_service.MemoService().save_memos(self.memos)
        print('WRITE SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_memos() : {memo_service.MemoService().load_memos()}')