import session
import config as root_config
from memo import memo_service

class DeleteMemo:

    def __init__(self):
        self.memos = {}

    def delete(self):
        self.memos = memo_service.MemoService().load_memos()   # dic
        myMemos = self.memos[session.getSigninedMemberId()]  # list
        for idx, memo in enumerate(myMemos):
            print(f'[{idx+1}] {memo}')
        selectedNumber = int(input('Please select the number to delete: '))
        myMemos.pop(selectedNumber-1)
        memo_service.MemoService().save_memos(self.memos)
        print('DELETE SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_memos(): {memo_service.MemoService().load_memos()}')