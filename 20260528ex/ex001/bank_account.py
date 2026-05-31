# - bank account
#     - 회원 1인당 1개의 계좌만 관리 
#     - 회원 1인당 N개의 계좌만 관리
#     - 입/출금 내역 

# 계좌별로 들어가서 입출금 내역을 확인하는게 좋겠다

import session
import time

class Account:
   
    def __init__(self, id):

        self.userid = id

        self.userAccountDict = {
            id:{}
        }

    def registUserAccount(self): 

        Flag = True

        while Flag:

            accountNum = int(input('개설할 계좌번호를 입력하세요.'))

            if accountNum in self.userAccountDict[self.userid]: 
                  
                print('이미 누군가 사용하고 있는 계좌번호입니다.')

                continue

            else: 
                Flag = True    

            Flag = True

            while Flag:
            
                selectedNum = int(input('계좌가 신설되었습니다. 입금하시겠습니까? 1.입금, 99.종료 : '))
                print(70*'-')

                if selectedNum == 99:

                    userBalance = 0
                    depositFlow = []     
                    print('종료합니다.')
                    print(70*'-')
                    Flag = False
                    
                elif selectedNum == 1:

                    userBalance = int(input('입금액: '))

                    depositTime = time.strftime('%Y-%m-%d %H:%M')
                    depositFlow = [{userBalance : depositTime}]
                        
                    print('새로운 계좌가 탄생했네요! 축하드립니다.')
                    print(70*'-')
                    Flag = False
        
                else:
                    print("오타입니다. 다시 적어주세요!")
                    print(70*'-')

        self.userAccountDict[self.userid][accountNum] = {                                                                      
                'balance': userBalance,
                'depositFlow': depositFlow,
                'withdrawalFlow': []
        }
               
    def viewAccount(self):  

        currentUserAccounts = self.userAccountDict[self.userid]

        for acc, accinfo in currentUserAccounts.items():

            balance = accinfo['balance']
            deposit =  accinfo['depositFlow']
            withdrawal = accinfo['withdrawalFlow']

            print(70*'-')    
            print(f'계좌번호: {acc}, 잔액: {balance}원, \n 예금 현황: {deposit}, \n 출금 현황: {withdrawal}')
            
    def depositMoney(self):

        if len(self.userAccountDict[self.userid]) == 0:
            print("보유 중인 계좌가 없습니다. 먼저 계좌를 개설해주세요.")
            print(70 * "-")
            self.registUserAccount()           
            return

        depositaccountNum = int(input('입금할 계좌번호를 입력하세요: '))
        print(70*'-')   

        if  depositaccountNum in self.userAccountDict[self.userid]:

            userAddDeposit = int(input('입금액을 입력하세요(단, 천만원 이하): '))
            print(70*'-')

            if userAddDeposit > 10000000:
                print('입금 한도를 초과했습니다.')
                return
                
            elif userAddDeposit < 0 :
                return
                    
            else:
                passedDeposit = userAddDeposit 
                     
                self.userAccountDict[self.userid][depositaccountNum]['balance'] += passedDeposit 

                depositTime = time.strftime('%Y-%m-%d %H:%M')

                self.userAccountDict[self.userid][depositaccountNum]['depositFlow'].append({passedDeposit:depositTime})
        else: 
            print('계좌번호가 맞지 않습니다. 다시 입력해주세요.')
            print(70*'-')
            return
            
    def withdrawal(self): 

        withdrawalAccountNum = int(input('출금할 계좌번호를 입력하세요: '))
        print(70*'-')

        if len(self.userAccountDict[self.userid]) == 0:
            print("보유 중인 계좌가 없습니다. 먼저 계좌를 개설해주세요.")
            print(70 * "-")
            self.registUserAccount()           
            return

        if  withdrawalAccountNum in self.userAccountDict[self.userid]:

            print(f'현재 잔액 : {self.userAccountDict[self.userid][withdrawalAccountNum]['balance']}')

            userAddWithdrawal = int(input('출금액을 입력하세요(단 100만원 이하):'))
            print(70*'-')
                
            if userAddWithdrawal > 1000000:
                print('출금 한도를 초과했습니다.')
                print(70*'-')
                return
                
            elif userAddWithdrawal <= 0 :
                print('0보다 작거나 같은 돈을 출금할 수는 없습니다.')
                print(70*'-')
                return
                
            passedWithdrawal = userAddWithdrawal

            if passedWithdrawal > self.userAccountDict[self.userid][withdrawalAccountNum]['balance']:
                print('잔액이 부족하여 출금이 거부되었습니다.')
                print(70*'-')
                return
            
            else: 
                self.userAccountDict[self.userid][withdrawalAccountNum]['balance'] -= passedWithdrawal

                withdrawalTime = time.strftime('%Y-%m-%d %H:%M')

                self.userAccountDict[self.userid][withdrawalAccountNum]['withdrawalFlow'].append({passedWithdrawal:withdrawalTime})

        else: 
            print('계좌번호를 다시 입력해주세요.')
            print(70*'-') 
             
    def deleteAccount(self):                

        print('계좌정보를 확인한 후 제거하고 싶은 계좌번호를 선택하세요')
        print(70*'-')

        self.viewAccount()

        wantedDelAccounted = int(input('계좌번호를 입력하세요.'))
        print(70*'-')
       
        while True:       
                
            if wantedDelAccounted in self.userAccountDict[self.userid]:

                del self.userAccountDict[self.userid][wantedDelAccounted]

                print(f'{wantedDelAccounted}가 삭제되었습니다.')
                print(70*'-')

                break

            else: 
                print('없는 계좌입니다. 다시 입력해주세요.') 
                print(70*'-')

    def shutdownAccount(self):

        print('프로그램을 종료하겠습니다. 이용해 주셔서 감사합니다.')

        print(70*'-')

    def run():

        if session.loginedMember == '':

            print('회원 가입이 필요한 기능입니다.')
            return

        userAccount = Account(session.loginedMember)

        flag = True

        while flag:

            selectedUserNum = int(input('1.계좌신설, 2. 계좌추가, 3.계좌삭제, 4. 입금, 5. 출금, 99. 종료 '))
        
            if selectedUserNum == 1:

                userAccount.registUserAccount()

            elif selectedUserNum == 2:

                userAccount.registUserAccount()

            elif selectedUserNum == 3:

                userAccount.deleteAccount()

            elif selectedUserNum == 4:

                userAccount.depositMoney()

            elif selectedUserNum == 5:

                userAccount.withdrawal()

            elif selectedUserNum == 99:

                userAccount.shutdownAccount()

                flag = False
                
            else : 
                print('오타입니다. 다시 입력해주세요.')     


# user1info = Account('tjdwlsl888')
# user1info = run()

if __name__ == '__main__':
    account = Account('gildohg')
    account.run()
 

#지피티의 피드백 ! 

# 지피티의 리펙토링 제안 

def __init__(self, id):
    self.userid = id
    self.accounts = {}  # ID로 또 감싸지 말고, 그냥 계좌들을 담을 빈 방만 만듭니다!

이렇게 __init__을 설계하면, 입금이나 출금 함수에서 데이터를 다룰 때 코드가 훨씬 직관적이고 깔끔해집니다.

변경 전: self.userAccountDict[self.userid][accountNum]['balance'] += passedDeposit

변경 후: self.accounts[accountNum]['balance'] += passedDeposit

💡 ID를 뺄 수 있는 이유: "객체(Instance) 자체가 이미 독립된 방입니다"
작성하신 코드의 run() 함수를 보면 로그인한 유저에 따라 객체를 이렇게 생성하고 있습니다.

홍길동 주머니 내부: self.userid = 'gildong', self.accounts = {111: {...}, 222: {...}}

철수 주머니 내부: self.userid = 'chulsoo', self.accounts = {333: {...}}

🏦 해결책: '개인 주머니'와 '은행 중앙 전산망' 분리하기
파이썬 클래스 안에는 변수를 두 가지 종류로 나누어 만들 수 있습니다.

인스턴스 변수 (self.xxx): 각자 따로따로 가지는 개인 주머니 (유저 ID, 개인 잔액 등)

클래스 변수 (Account.xxx): 모든 객체가 다 함께 쳐다보고 공유하는 중앙 전산망 게시판

계좌번호 중복을 막으려면, 누군가 계좌를 만들 때마다 개인 주머니에만 넣는 게 아니라 "공용 중앙 전산망"에도 그 번호를 등록해 두면 됩니다.

class Account:
    
    # 📌 클래스 변수: __init__ 바깥쪽에 만듭니다. (은행 중앙 전산망 역할)
    # 이 클래스로 만들어진 모든 유저(객체)가 이 리스트를 공유합니다.
    all_created_accounts = [] 

    def __init__(self, id):
        self.userid = id
        self.accounts = {} # 개인 주머니 (내 계좌 정보만 담음)        

def function(self,a) 어떤 경우에는 def function() 이런식으로 할 때가 있는데
init부분이 필요한가 아닌가로 구분지어도 될까?

결론부터 명확하게 말씀드리면, __init__의 필요 여부로 구분하는 것은 아닙니다! 클래스 안에서 함수(메서드)를 만들 때 self를 넣느냐 마느냐를 결정하는 아주 명쾌하고 유일한 기준은 딱 하나입니다.

"이 함수가 객체의 '개인 주머니(데이터)'를 뒤져볼 필요가 있는가?"

2. def function(): "개인 정보는 필요 없어!" (예외적인 경우)
그렇다면 self를 아예 안 적는 경우는 언제일까요? "누가 이 함수를 부르든 상관없이, 개인 데이터는 1도 알 필요가 없을 때"입니다.

내가 이 질문을 한 이유가 처음에

init부분에 self.a = a self.b= b 이런식으로 매개변수를 선언하잖아? 니말은 이런거 말고도 내부 함수들이 만들고 지정하고 가꾼 데이터들도 self로 해서 변경하라는거지?

와! 질문의 진짜 의도를 듣고 나니 정말 소름이 돋았습니다. 객체 지향 프로그래밍에서 가장 헷갈리기 쉬운 "데이터의 생존 주기(Life Cycle)"를 정확히 짚어내셨네요!

말씀하신 내용이 1000% 맞습니다. __init__에서 처음에 self.a = a로 선언한 것들뿐만 아니라, 나중에 다른 내부 함수들에서 새롭게 만들거나 변경해야 하는 중요한 데이터들도 무조건 self.어쩌구 형태로 다루어야 합니다. 그 이유를 아주 명확하게 보여드릴게요.

🎒 self를 붙이는 것과 안 붙이는 것의 치명적인 차이
함수 안에서 데이터를 만들 때 self를 붙이느냐 마느냐는 "이 데이터를 내 주머니(객체)에 평생 간직할 것인가, 아니면 지금 쓰고 버릴 것인가?"를 결정합니다.

❌ self를 안 붙인 변수 (지역 변수 = 임시 메모지)
함수 안에서 self 없이 그냥 x = 10이라고 변수를 만들면, 파이썬은 이것을 '임시 메모지'로 취급합니다. 함수 실행이 끝나는 순간 그 메모지를 쫙쫙 찢어서 쓰레기통에 버려버립니다. (다른 함수에서 절대 다시 꺼내볼 수 없습니다.)

⭕ self를 붙인 변수 (인스턴스 변수 = 내 가방 속 노트)
반면 self.x = 10이라고 선언하면, 파이썬은 "아! 이건 이 객체의 가방(주머니) 안에 잘 적어둬야겠구나!" 하고 영구적으로 보관합니다. 함수가 끝나도 데이터가 살아있어서, 나중에 다른 함수가 언제든지 가방을 열어 꺼내볼 수 있습니다.

💡 요약하자면
__init__은 "태어날 때 무조건 가방에 넣고 시작해야 하는 필수품"을 챙기는 곳입니다.

다른 내부 함수들은 작동하면서 "가방 속의 물건(self.xxx)을 꺼내서 바꾸기도 하고, 새로운 물건을 가방에 추가하기도 하는 과정"입니다.

따라서, 다른 함수가 나중에도 알아야 하는 데이터라면 언제 어디서 만들든 무조건 앞에 self.를 붙여서 내 가방에 넣으시면 됩니다!


__init__ 생성자 . 클래스로 인스턴트(객체)를 생성할 때 가장 처음에 실행되는거임 


