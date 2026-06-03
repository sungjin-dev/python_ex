import session
from bank import bank_service

class AccountList:
    def __init__(self):
        self.accounts = {}  

    def list(self):
        
        self.accounts = bank_service.BankService().load_accounts()
        
        MyAccounts = self.accounts[session.getSigninedMemberId()]

        for idx, MyAccount in enumerate(MyAccounts.keys()): 
            print('=' * 80)
            print(f'[{idx + 1}]: {MyAccount}: {MyAccounts[MyAccount]["balance"]}')
            print('-' * 80)
            print('날짜/시간 \t\t 내역 \t\t\t 입금 \t\t 출금')
            for history in MyAccounts[MyAccount]['histories']:
                if 'dAmount' in history:
                    print(f'{history["dRegDate"]} \t {history["dhistory"]} \t\t\t {history["dAmount"]}')
                else: 
                    print(f'{history["wRegDate"]} \t {history["whistory"]} \t\t\t\t\t {history["wAmount"]}')
            print()        