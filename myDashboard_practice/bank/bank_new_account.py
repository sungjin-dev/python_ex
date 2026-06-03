from bank import bank_service
import session
import uuid
import config as root_config

class NewAccount:
    def __init__(self):
        self.accounts = {}
    
    def addtionalAcc(self):

        self.accounts = bank_service.BankService().load_accounts()

        if session.getSigninedMemberId() not in self.accounts:  
            self.accounts[session.getSigninedMemberId()] = {}

        MyAccounts = self.accounts[session.getSigninedMemberId()] 
        MyAccounts[str(uuid.uuid4())] = {          
                'balance' : 0,
                'histories' : []
        } 

        bank_service.BankService().save_accounts(self.accounts)  
        print('NEW-ACCOUNT SUCCESS')

        if root_config.DEV_MOD:
            print(f'self.load_accounts: {bank_service.BankService().load_accounts()}')