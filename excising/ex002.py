
DEV_MOD = True

flag = True

members = {}            # Database
#-------------------------------------------------------------------------------------
if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234','5678','3124']
    uMails = ['gildong@gmail.com','chanho@naver.com','saeri@daum.net']
    uPhones = ['010-1234-5678','010-9999-6666','010-7777-3333']

    for n in range(len(uIds)):      # range가 생략되어있는걸 보면 0~3까지 실행되니 어차피 길이만큼 딱 실행된다. 
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
        }
#-------------------------------------------------------------------------------------

def getSelecetedMenuNum():    # 여기가 빈칸인 이유가 내부에서 input데이터를 자체적으로 수급
    selecetedMenuNum = int(input('1. 회원가입   2.로그인   3. 나의 정보 출력   4.모든 회원 정보 출력   99. 종료' ))
    return selecetedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):  # 외부에서 데이터가 유입되는거라 매개변수를 지정
    members[uId] = {                        # 모은 데이터를 딕셔너리로 만든다.
        'id': uId,                          # em                       
        'uPw': uPw,
        'uMail': uMail,
        'uPhone': uPhone
    } 
def ismember(uId):
    if uId in members:   
        print(f'{uId}는 이미 사용 중 입니다. 다시 ~~')
        return True                   # True or False 이런식의 형태로 return함
    else:
        return False    
def printAllMemberInfo(value):
    for key1, value1 in value.items():
        print(f'{key1}: {value1}')

# 컨트롤 누르고 defined 된 곳을 누르면 바로 감

while flag:
    userSelctedMenuNum = getSelecetedMenuNum() #  <- input 데이터를 return받아서 여기서 명찰 달아줌
    
    if userSelctedMenuNum == SIGN_UP:
        uId = input('input member ID:')

        if not ismember(uId):       # not true  -> False 가 도출 
            uPw = input('input member PW:')
            uMail = input('input member EMAIL:')
            while True:
                if '@' not in uMail:
                    