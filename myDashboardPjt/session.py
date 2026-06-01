signinedMemberId = ''

# setter
def setSigninedMemberId(mId = ''):
    global signinedMemberId
    signinedMemberId = mId

# def setSigninedMemberId(logined, money):
#     if logined == boss:
#         salary = money

# getter
def getSigninedMemberId():
    return signinedMemberId


# 데이터 무결성

'''
데이터가 항상 올바른 형식이어야 함
임의로 변경 및 수정할 수 없어야 함
객체의 내부데이터를 직접 수정하지 못하게 하고 이를 검증하기 위함

trigger 

"사건이 발생했을 때, 연쇄적으로 특정 코드가 '자동 실행'되도록 만들어 둔 장치"

트리거가 있을 때: 미리 DB에 "누군가 삭제되면, 그 정보를 탈퇴자 DB로 넘겨라" 
1) 메인 DB에서 회원을 지우기만 하면, DB가 알아서(트리거가 발동하여) 보관용 DB로 정보를 복사

💡 파이썬 코드로는 어떻게 구현할까?

 delete(self) 함수

지우려는 회원의 데이터를 self.members에서 찾는다.

(이 부분이 트리거 역할!) 지우기 직전에, 그 데이터를 self.deleted_members라는 새로운 딕셔너리에 먼저 복사한다. 
(그리고 deleted_members.json 파일에 save 한다.)

복사가 안전하게 끝난 것을 확인한 뒤, self.members에서 최종 삭제한다.

저장소(변수/파일) 추가하기
__init__과 init_database 부분에 기존 self.members 외에도 탈퇴자를 담을 self.deleted_members = {}를 만들고, deleted_members.json 파일 경로도 하나 더 연결해 줍니다.
pop()  pop(key)은 키(Key)값을 이용해 데이터를 쏙 빼옵니다. 
'''

