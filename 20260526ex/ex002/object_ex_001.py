# 클래스(객체를 만들기 위한 틀 설계도) 문법

# 붕어빵 클래스

# class FishBread:               # 클래스 선언 첫글자는 대문자 함수와 구분하기 위해 그럼 함수가 아닌거네
#     # 속성(attribute)
#     def __init__(self, f, b):   # init 이 변수명만들고 이름표 명찰달고 청소 역할을 해줌 
#         self.flour = f          # self  라운더리 느낌? 초기화 과정 
#         self.bean = b

#     # 기능(function, method)

#     def makeFishBread(self):       #  self 꼭 써주기 !
#         print('붕어빵 제조') 

# # 붕어빵 클래스로부터 객체를 만들어 봅시다. (객체 생성)
# myFishBread = FishBread('팥', '밀가루')   1
# friendFishBread = FishBread('호박', '쌀')
# hisFishBread = FishBread('꿀', '밀가루')

# print(f'내 붕어빵의 속 내용물: {myFishBread.flour}') #  팥
# print(f'내 붕어빵의 반죽: {myFishBread.bean}') #  밀가루

# print(f'친구 붕어빵의 속 내용물: {friendFishBread.flour}') #  호박
# print(f'친구 붕어빵의 반죽: {friendFishBread.bean}') #  쌀

# 계산기 클래스

class Calculator:

    # 속성
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        
    # 기능
    def add(self):
        print(f'{self.num1 + self.num2}')

    def sub(self):
        print(f'{self.num1 - self.num2}')

    def mul(self):
        print(f'{self.num1 * self.num2}')
       
    def div(self):
        print(f'{self.num1 / self.num2}')

myCalculator = Calculator(10, 20)        
friendCalculator = Calculator(100, 200)        

myCalculator.add()         # print  중복으로 사용하지 않도록 주의
myCalculator.sub()
myCalculator.mul()
myCalculator.div()

friendCalculator.add()        
friendCalculator.sub()
friendCalculator.mul()
friendCalculator.div()

# 인간 클래스

class Human:
    # 속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    # 기능
    def walk(self):
        print('걷자!')    
    def run(self):
        print('걷자!')    
    def printMyInfo(self):
        print(f'나의 신장: {self.height}')
        print(f'나의 체중: {self.weight}')
  

human1 = Human(188, 87)
human2 = Human(165, 49)

human1.printMyInfo()
human2.printMyInfo()

human1 = human2
human1.printMyInfo()        # 165, 49

human1.height = 200
human1.weight = 39

human2.printMyInfo()        # 200 39

# AOP OOP 절차지향

# AOP란?  관점지향

# 핵심 비지니스 로직(core concern)

# 공통/부가기능 (Cross-cutting Concern)

