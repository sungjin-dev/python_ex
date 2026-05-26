# 1. 모든 회원 정보를 저장할 딕셔너리
members = {}

# 2. 회원가입 함수
def register(ID, PW, Email, Phone):
    members[ID] = [PW, Email, Phone]
    print("회원가입이 완료되었습니다.")

# 딕셔너리이름[새로운 키] = 넣을 값   

# 3. 로그인 함수
def login(ID, PW):
    if ID in members:
        if members[ID][0] == PW:
            print("로그인 성공")       
    else:
        print("로그인 실패")     # 아이디 비밀번호의 경우 else로 따로따로 모든 경우의 수를 지정하지 않는다 
                                 # 보안상 정보 힌트를 줄 수 있다 

# 4. 특정 회원 정보 출력 함수
def show_member(ID, PW):
    if ID in members:
        if members[ID][0] == PW:
            print(f"ID: {ID}")
            print(f"PW: {members[ID][0]}")
            print(f"Email: {members[ID][1]}")
            print(f"Phone: {members[ID][2]}")
        else:
            print("비밀번호가 일치하지 않습니다.")
    else:
        print("존재하지 않는 아이디입니다.")

# 5. 모든 회원 정보 출력 함수
def show_all():
    if not members:
        print("가입된 회원이 없습니다.")
        return

    for ID, info in members.items():
        print(f"--- 회원 정보 ({ID}) ---")
        print(f"ID: {ID}")
        print(f"PW: {info[0]}")
        print(f"Email: {info[1]}")
        print(f"Phone: {info[2]}")

# 6. 메인 프로그램 실행 반복문
while True:
    print("\n메뉴: 1.회원가입 2.로그인 3.특정 회원 정보 출력 4.모든 회원 정보 출력 99.종료")
    choice = input("원하는 메뉴 번호를 입력하세요: ")

    if choice == '1':
        inputData = [
            input("회원ID: "),
            input("회원PW: "),
            input("회원Email: "),
            input("회원Phone: ")
        ]
        register(*inputData)

    elif choice == '2':
        inputData = [
            input("회원ID: "),
            input("회원PW: ")
        ]
        login(*inputData)

    elif choice == '3':
        inputData = [
            input("회원ID: "),
            input("회원PW: ")
        ]
        show_member(*inputData)

    elif choice == '4':
        show_all()

    elif choice == '99':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")