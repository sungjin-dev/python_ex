import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid
from util import util_time

class BankService:
    def __init__(self):
        self.accounts = {}     # 단기 기억. 객체를 한번 생성하고 나면 없어질 데이터
        self.init_database()   # 장기 기억으로 관리. 따로 파일로 그 과정을 저장하고 관리하게끔 해줌.
                               # 전역 변수도 결국 '단기 기억(RAM)' 클래스 상단에 전역변수를 선언해도 소용없음                   
    def init_database(self):
        # 현재 파일 위치              절대값 경로
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        # db/accounts.json                  폴더명      파일명
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\pjt\python\python_ex\myDashboardPjt\db\accounts.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):       
            self.save_accounts(self.accounts)  # 파일이 없으면 파일 만드는 함수로 가는거임
        else:
            self.accounts = self.load_accounts()  # 장기 데이터에 세이브  

    def save_accounts(self, accounts):   # {}
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(accounts, f, ensure_ascii = False, indent = 4) 

    # 데이터 무결성 검증 클래스를 만들어서 관리하기 
    # JSON파일을 읽어서 애플리케이션으로 데이터를 가져오는 것   
    def load_accounts(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)
            
    def isMyAccount(self):
        allAccount = self.load_accounts()
        if session.getSigninedMemberId() in allAccount:
            return True 
             
        return False

    def run(self):

        if session.getSigninedMemberId() == '':
            print('Please SIGN-IN!!')
            return    

        flag = True
        while flag:

            if self.isMyAccount():      # if True: 이렇게만 돼도 조건문 통과됨. 
                menuNum = int(input('1.ACCOUNT-LIST   2.NEW-ACCOUNT   3.DEPOSIT   4.WITHDRAWAL    99.SYSTEM-OUT '))

            else:
                print('No account yet!!')    
                menuNum = int(input(' 2.NEW-ACCOUNT     99.SYSTEM-OUT '))

            if menuNum == bank_config.ACCOUNT_LIST:
                self.accounts = self.load_accounts()
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

            elif menuNum == bank_config.NEW_ACCOUNT:

                self.accounts = self.load_accounts()   # 최신데이터를 불러옴  

                if session.getSigninedMemberId() not in self.accounts:  # if not in 구조 : 없으면 빈 방부터
                    self.accounts[session.getSigninedMemberId()] = {}

                MyAccounts = self.accounts[session.getSigninedMemberId()]  # 브릿지. 새로운 중첩딕셔너리를 변수로 담아냄
                
                MyAccounts[str(uuid.uuid4())] = {           # UUID, str castiong 
                        'balance' : 0,
                        # 'password': '',
                        'histories' : []
                } 

                self.save_accounts(self.accounts)  
                print('NEW-ACCOUNT SUCCESS')

                if root_config.DEV_MOD:
                    print(f'self.load_accounts: {self.load_accounts()}')

            elif menuNum == bank_config.DEPOSIT:
                self.accounts = self.load_accounts()    # 1단계 최신정보 불러오기
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
                
                self.save_accounts(self.accounts)
                print('DEPOSIT SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_account(): {self.load_accounts()}')

            elif menuNum == bank_config.WITHDRAWAL:
                self.accounts = self.load_accounts()    # 1단계 최신정보 불러오기
                MyAccounts = self.accounts[session.getSigninedMemberId()]  # 2단계 내꺼만 빼오기 

                print('\nMy Accounts-------------------------------------------------')
                for idx, account in enumerate (MyAccounts.keys()):   # 번호를 매기고 싶다면 enumerate를 사용하자
                    print(f'[{idx+1}]: {account}')
                print('------------------------------------------------------------\n')

                while True:
                    withdrawalAccountNumber = input('Enter withdrawal account number: ')
                    if withdrawalAccountNumber not in MyAccounts: 
                        print('The account was not found!!')
                        print('\nMy Accounts-------------------------------------------------')
                        for idx, account in enumerate (MyAccounts.keys()):   # 번호를 매기고 싶다면 enumerate를 사용하자
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
                    # 굳이 apppend보다는 reverse()할 필요가 없는  insert가 좋음 
                    
                    self.save_accounts(self.accounts)
                    print('WITHDRAWAL SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_account(): {self.load_accounts()}')

            elif menuNum == bank_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    bankService = BankService()
    bankService.run()

# python -m bank.bank_service 

# UUID(Universally Unique Identifier, 범용 고유 식별자)는 
# 컴퓨터 시스템에서 데이터를 식별하기 위해 사용하는 '전 세계에서 유일무이한, 
# 절대 겹치지 않는 고유 번호'를 만드는 표준 약속
# UUID는 보통 아래와 같이 32개의 16진수와 4개의 하이픈(-)으로 이루어진 36자리의 문자열

# 클래스 안에서는 철저하게 "내 것(나의 데이터)과 내 능력(나의 기능)"을 쓴다

# self.accounts["gildong"]["UUID-1234"] = { 'balance': 0, ... }

# "키값을 단계별로 설정해서 중첩을 만든다"

# 로거(logger) :  정보 경보 오류 등을 기록하는 객체   
# java.util.logging.Logger 