from db import member_db               #  더미변수 만들 때 쉼표 이런거 잘 찍자
from db import diary_db


ids = ['gildong', 'chanho']
pws = ['1234', '0000']
mails = ['gildong@gmail.com', 'chanho@naver.com']             
phones = ['010-1234-5678', '010-9012-3456']
times = ['2026.5.22.11.41.59','2026.5.23.12.11.00' ]
                                   
def dumyInit():                # len()을 쓴 이유 -> ids 이게 리스트를 지칭하는거라 계정 수를 찾는것
    for n in range(len(ids)):   
        member_db.memberDB[ids[n]] = {   # member_db.memberDB 이게 input으로 수집한 데이터 
            'uId': ids[n],
            'uPw': pws[n],
            'uMail': mails[n],
            'uPhone': phones[n],
            'uRegDate' :times[n]
        }

        diary_db.diaryDB[ids[n]] = [] 

        # 빈 리스트를 미리 할당해두어 append를 활용해서 추가할 수 있도록 함
        # 낙하산으로 들어온 더미변수들은 회원가입 1번을 거치지 않았기 때문에
        # diary_db.diaryDB[uId] = [] 이 루트를 생략하고 넘어감. 그리서 더미 함수에 따로 추가로
        # 넣어준 것임


def dumyInit(): 
    # zip()으로 같은 위치의 데이터들을 한 번에 묶어서 꺼내옵니다.
    for u_id, pw, mail, phone, time in zip(ids, pws, mails, phones, times):   
        member_db.memberDB[u_id] = {   
            'uId': u_id,
            'uPw': pw,
            'uMail': mail,
            'uPhone': phone,
            'uRegDate' : time
        }    

# zip()
# names = ['철수', '영희', '민수']
# ages = [20, 25, 30]

# # 두 리스트를 지퍼로 잠그듯 묶어줍니다.
# for name, age in zip(names, ages):
#     print(f"이름: {name}, 나이: {age}") 
# 
# keys = ['이름', '나이', '직업']

# values = ['홍길동', 30, '개발자']

# my_dict = dict(zip(keys, values))     

# 1. 처음부터 JSON이나 실제 DB 형태와 비슷하게 한 사람 단위로 묶어둡니다.

# 짝지은 데이터를 눈으로 보기 위해 껍데기를 씌워줘야 합니다.list() or dict(), tuple()

# list()나 dict() 같은 껍데기를 씌우지 않은 zip() 객체는 "포장 방법만 적어놓고 대기 타는 상태"라고 볼 수 있습니다.

# 프로그래밍 전문 용어로는 이런 방식을 지연 평가(Lazy Evaluation)라고 부르고, 그렇게 대기하고 있는 상태의 객체를 이터레이터(Iterator)라고 부릅니다.

# DUMMY_USERS = [
#     {'uId': 'gildong', 'uPw': '1234', 'uMail': 'gildong@gmail.com', 'uPhone': '010-1234-5678', 'uRegDate': '2026.5.22.11.41.59'},
#     {'uId': 'chanho', 'uPw': '0000', 'uMail': 'chanho@naver.com', 'uPhone': '010-9012-3456', 'uRegDate': '2026.5.23.12.11.00'}
# ]

# # 2. 초기화 함수가 훨씬 단순해집니다.
# def dumyInit():
#     for user in DUMMY_USERS:
#         member_db.memberDB[user['uId']] = user