# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 


class Account:
   
    accountsDict = {}

    def __init__(self, id, account, balance):
        self.key = id 
        self.userdata1 = account
        self.userdata2 = balance
       
        Account.accountsDict[id] = account

