import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid

class BankService:
    def __init__(self):
        self.accounts = {}     # 단기 기억. 객체를 한번 생성하고 나면 없어질 데이터
        self.init_database()   # 장기 기억으로 관리. 따로 파일로 그 과정을 저장하고 관리하게끔 해줌.
                               # 전역 변수도 결국 '단기 기억(RAM)'입니다. (가장 중요)                      
    def init_database(self):
        # 현재 파일 위치           절대값 경로
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        # db/accounts.json                    폴더명   파일명
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\pjt\python\python_ex\my

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_accounts(self.accounts)  # 파일이 없으면 파일 만드는 함수로 가는거임
        else:
            self.accounts = self.load_accounts()

    def save_accounts(self, accounts):   # {}
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(accounts, f, ensure_ascii = False, indent = 4) 

    # 데이터 무결성 검증 클래스를 만들어서 관리하기 

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
                pass
            
            elif menuNum == bank_config.NEW_ACCOUNT:
                self.accounts = self.load_accounts()   # 과정을 누적해서 저장하고 불러옴 load 
                if session.getSigninedMemberId() not in self.accounts:
                    self.accounts[session.getSigninedMemberId()] = {}

                MyAccounts = self.accounts[session.getSigninedMemberId()]
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
                pass

            elif menuNum == bank_config.WITHDRAWAL:
                pass

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