import session
import config as root_config
from memo import memo_service

class UpdatingMemo:    

    def __init__(self):
        self.memos = {}
        
    def update(self):       
        self.memos = memo_service.MemoService().load_memos()   # dic
        myMemos = self.memos[session.getSigninedMemberId()]  # list
        for idx, memo in enumerate(myMemos):
            print(f'[{idx+1}] {memo}')
        selectedNumber = int(input('Please select the number to modify: '))
        memo = input('Edit memo: ')
        myMemos[selectedNumber-1] = memo   # idx+1 인위적으로 +1했으니까  

        memo_service.MemoService().save_memos(self.memos)
        print('MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_memos(): {memo_service.MemoService().load_memos()}')