import session
from bank import bank_service
from util import util_time
import config as root_config

class WithdrawalAcc:
    def __init__(self):

        self.accounts = {}

    def withdrawal(self):

        self.accounts = bank_service.BankService().load_accounts()   
        MyAccounts = self.accounts[session.getSigninedMemberId()] 

        print('\nMy Accounts-------------------------------------------------')
        for idx, account in enumerate (MyAccounts.keys()):   
            print(f'[{idx+1}]: {account}')
        print('------------------------------------------------------------\n')

        while True:
            withdrawalAccountNumber = input('Enter withdrawal account number: ')
            if withdrawalAccountNumber not in MyAccounts: 
                print('The account was not found!!')
                print('\nMy Accounts-------------------------------------------------')
                for idx, account in enumerate (MyAccounts.keys()):   
                    print(f'[{idx+1}]: {account}')
                print('------------------------------------------------------------\n')
            else:
                break    

        withdrawalAmount = int(input('Enter withdrawal amount: '))
        withdrawalHistory = input('Enter withdrawal history: ')
        withdrawal = {
            'wAmount': withdrawalAmount,
            'whistory': withdrawalHistory,
            'wRegDate': util_time.getCurrentDateTime(),
            'wModDate': util_time.getCurrentDateTime()
        }

        if withdrawalAmount > MyAccounts[withdrawalAccountNumber]['balance']:
            print('Error! Check Balance!!')
        else: 
            MyAccounts[withdrawalAccountNumber]['balance'] -= withdrawalAmount
            MyAccounts[withdrawalAccountNumber]['histories'].insert(0, withdrawal) 
            
            bank_service.BankService().save_accounts(self.accounts)
            print('WITHDRAWAL SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_account(): {bank_service.BankService().load_accounts()}')
