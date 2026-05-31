a = Fourcal()

a.setdata(4,2)

a.add() 

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        

# 첫 번째 매개변수 self는 특별한 의미
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용 ( 자바 self 필요 없음.)

# 클래스명.메서드' 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해야 한다.

FourCal.setdata(a, 4, 2)  # -> 클래스명.매서드 형태라서 a 꼭 전달
a.setdata(4, 2)

# 객체.메서드' 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
'''
여기서 self는 "이 명령을 실행할 실제 객체(주인공)가 누구냐?"를 가리키는 자리표시자.
기계(파이썬) 입장에서는 "대체 누구의 데이터를 4와 2로 바꾸라는 거야?"를 알아야 하니까요. 
이 주인공을 알려주는 방식이 두 가지인 것입니다.

a.setdata(4, 2) (객체.메서드 형태) : 파이썬의 VIP 대우 (자동)
a라는 실제 물건(객체)이 직접 나서서 setdata라는 기능을 씁니다.
파이썬은 a. 하고 시작하는 것을 보자마자 "아! 주인공이 a구나!" 하고 찰떡같이 알아듣습니다.
a를 첫 번째 self 자리에 몰래 쏙 넣어줍니다. 
* 주인공(self)이 누군지 이미 파악했기 때문에, 
우리는 self 자리를 생략하고 나머지 데이터인 4와 2만 던져주면 되는 것입니다.

FourCal.setdata(a, 4, 2) (클래스명.메서드 형태) : 수동 모드
'설계도(FourCal 클래스)'에게 직접 명령
설계도의 당황: 설계도는 기능이 쓰여 있는 종이일 뿐입니다. 
설계도는 이렇게 반문합니다. "내가 만든 객체가 a도 있고, b도 있고, c도 있는데... 
대체 누구한테 4와 2를 넣으라는 거야?!"
사용자가 직접 "a한테 넣어줘!"라고 첫 번째 자리(self 자리)에 a를 콕 집어서 전달해야만 합니다.

수동 모드 사용 전에 반드시 메인 파일에서 a = FourCal()을 먼저 실행해서 빈 객체(주머니)를 만들어두어야 합니다.

'''
# 설계도 

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second
    
    # main.py (메인 실행 파일)

import calculator  # 1. 설계도가 있는 파일을 불러옵니다.

# ----------------------------------------------------
# 📌 질문하신 핵심 부분: a를 어떻게 지정(형성)하는가?
# ----------------------------------------------------

# [1단계] 빈 객체를 먼저 만듭니다. (이게 a의 진짜 정체입니다!)
a = calculator.FourCal()  
# 설명: "calculator 파일에 있는 FourCal 설계도로 빈 주머니를 만들고, 이름을 a라고 할게!"
# (주의: 만약 이 줄이 없다면, 아래에서 a를 쓸 때 에러가 납니다.)


# [2단계] 생성된 a를 수동으로 전달합니다. (질문하신 사용법)
calculator.FourCal.setdata(a, 4, 2)
# 설명: "FourCal 설계도야! 내가 방금 만든 a라는 주머니 줄 테니까, 거기에 4랑 2 좀 담아줘!"


# [3단계] 잘 담겼나 계산을 해볼까요?
result = calculator.FourCal.add(a) # 역시 a를 직접 전달합니다.
print(f"결과: {result}") # 출력: 결과: 6


🥇 __init__ 세팅의 3가지 황금 기준
1. 이 객체가 태어날 때 "반드시" 필요한 데이터인가? (필수품)
객체가 정상적으로 작동하기 위해 절대 없어서는 안 될 핵심 데이터만 매개변수(소괄호 안)로 받습니다.

2. 처음 태어날 때의 "기본 상태"가 있는가? (초기값)

밖에서 굳이 입력받지 않아도, 태어날 때 기본으로 장착하고 있어야 하는 상태들은 __init__ 내부에서 자체적으로 세팅해 줍니다.

기준: "새로 태어났으니 당연히 레벨은 1이고, 상태는 '정상'이겠지."

예시: self.level = 1, self.is_alive = True

3. 너무 무거운 동작을 시키고 있지는 않은가? (가벼움 유지)


❌ 엉망으로 짠 __init__ (나쁜 예)
Python
class Monster:
    # 너무 많은 걸 한 번에 다 받으려고 함 (호출하는 사람이 피곤함)
    def __init__(self, name, hp, level, is_alive, attack_power, items):
        self.name = name
        self.hp = hp
        self.level = level


깔끔하게 정리된 __init__ (좋은 예)
Python
class Monster:
    # 1. 꼭 필요한 것(이름, 체력)만 밖에서 받습니다.
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        # 2. 굳이 안 받아도 되는 '기본 상태'는 알아서 깔끔하게 세팅합니다.
        self.level = 1               # 처음 태어나면 무조건 레벨 1
        self.is_alive = True         # 처음 태어나면 무조건 살아있음
        self.inventory = []          # 처음엔 빈 주머니


#클래스의 상속(Inheritance)

#       상속자     부모
class MoreFourCal(FourCal):
     def pow(self):
        result = self.first ** self.second      # ** 제곱이다
        return result    
     
class SafeFourCal(FourCal):
     def div(self):
         if self.second == 0:  # 나누는 값이 0인 경우 0을 반환하도록 수정
             return 0
         else:
             return self.first / self.second        
         
# 부모랑 자식이 싸우면 자식이 이김 ㅇㅇ 매서브 오버라이딩 

# 클래스 변수   self이런거 없이 

if __name__ == "__main__":

파이썬은 어떤 파이썬 파일(.py)이 실행되든, 
그 파일에게 몰래 __name__이라는 이름표(변수)를 달아줍니다.

직접 실행할 때 (내가 주인공! 👑): * 파일에서 '실행(Run)' 버튼을 직접 누르면, 
파이썬은 "오! 네가 메인 프로그램이구나!" 하면서 이름표에 "__main__"이라고 적어줍니다.

다른 파일에서 나를 import 해서 가져가면, 파이썬은 "너는 메인이 아니라 도와주러 온 부품이구나" 
하면서 파일의 원래 이름(예: "calculator")을 이름표에 적어줍니다.


# main.py (진짜 메인 파일)
import calculator
import session

class BankSystem:
    # ... 메인 시스템 코드들 ...

# 👑 여기가 이 프로그램의 진짜 "진짜 시작점"임을 표시합니다.
if __name__ == "__main__":
    account = calculator.Account(session.loginedMember)
    account.run() # 프로그램 시동!