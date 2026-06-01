# controller 계층에서는 직접적으로 데이터를 처리하면 x
# 코드 컨벤션 -> 코드 변수명 모듈 파일명들을 일관적으로 정돈하는 것
# 폴더별로 묶어두는 행위 -> 패키징(packaging) 


import config
from member import member_service
from bank import bank_service

def main():
    flag = True

    while flag:

        menuNum = int(input('1.MEMBER  2.BANK  3.MEMO  4.TODO  99.SYSTEM-OUT'))

        if menuNum == config.MEMBER_SERVICE:
            memberService = member_service.MemberService()
            memberService.run()

        elif menuNum == config.BANK_SERVICE:
            bankService = bank_service.BankService()
            bankService.run()
        
        elif menuNum == config.MEMO_SERVICE:
            pass

        elif menuNum == config.TODO_SERVICE:
            pass

        elif menuNum == config.SYSTEM_OUT:
            flag = False



if __name__ == "__main__":
    main()