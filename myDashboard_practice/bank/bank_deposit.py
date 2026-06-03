import session
from bank import bank_service
from util import util_time
import config as root_config

class AccDeposit:
    def __init__(self):
        self.accounts = {}

    def deposit(self):
        self.accounts = bank_service.BankService().load_accounts()    # 1단계 최신정보 불러오기
        MyAccounts = self.accounts[session.getSigninedMemberId()]  # 2단계 내꺼만 빼오기 

        print('\nMy Accounts-------------------------------------------------')
        for idx, account in enumerate (MyAccounts.keys()):   # 번호를 매기고 싶다면 enumerate를 사용하자
            print(f'[{idx+1}]: {account}')
        print('------------------------------------------------------------\n')

        while True:
            depositAccountNumber = input('Enter deposit account number: ')
            if depositAccountNumber not in MyAccounts: 
                print('The account was not found!!')
                print('\nMy Accounts-------------------------------------------------')
                for idx, account in enumerate (MyAccounts.keys()):   # 번호를 매기고 싶다면 enumerate를 사용하자
                    print(f'[{idx+1}]: {account}')
                print('------------------------------------------------------------\n')
            else:
                break    

        depositAmount = int(input('Enter deposit amount: '))
        depositHistory = input('Enter deposit history: ')
        deposit = {
            'dAmount': depositAmount,
            'dhistory': depositHistory,
            'dRegDate': util_time.getCurrentDateTime(),
            'dModDate': util_time.getCurrentDateTime()
        }

        MyAccounts[depositAccountNumber]['balance'] += depositAmount
        MyAccounts[depositAccountNumber]['histories'].insert(0, deposit) 
        # 굳이 apppend보다는 reverse()할 필요가 없는  insert가 좋음 
        
        bank_service.BankService().save_accounts(self.accounts)
        print('DEPOSIT SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_account(): {bank_service.BankService().load_accounts()}')