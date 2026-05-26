'''예제 4: 강력한 비밀번호 생성 검사기 (문자열 분석)
사용자가 회원가입을 할 때 입력한 비밀번호가 안전한지 3가지 규칙을 통해 검사하는 함수를 만드세요.

함수 이름: check_password

보안 규칙 3가지 (모두 만족해야 통과):

비밀번호 길이는 최소 8글자 이상이어야 합니다.

비밀번호 안에 숫자가 최소 1개 이상 포함되어야 합니다.

비밀번호 안에 영문 대문자가 최소 1개 이상 포함되어야 합니다.

출력 및 반환:

3가지 규칙을 모두 통과하면 print("안전한 비밀번호입니다.")를 출력하고 True를 return 합니다.

하나라도 실패하면 어떤 규칙을 어겼는지 출력하고 (예: "숫자가 포함되어야 합니다.") False를 return 합니다.

💡 예제 4 파이썬 치트키 힌트:
문자열이 숫자인지 확인하는 메서드는 .isdigit(), 대문자인지 확인하는 메서드는 .isupper() 입니다. for문으로 문자열의 글자를 하나씩 쪼개서 검사해 보세요! (예: for char in password:)

아래의 뼈대 코드를 복사해서 시작해 보세요!'''

'''
1) (list()로 안 바꿔도 문자열은 for문이 돌아갑니다!
'''


def check_password(password):


    if len(password) < 8:
        print('8글자 이상이여야 합니다')
        return False
    
    hasNumber = False
    hasUuper = False

    for cha in password:
        if cha.isdigit():
            hasNumber = True
        # else:
        #     hasNumber = False
        #     print('숫자가 포함되어야 합니다.')
        #     return False

        if cha.isupper():  
            hasUuper = True 
        # else:
        #     hasUuper = False
        #     print('대문자가 포함되어야 합니다.')
        #     return False
        
    if hasNumber == False:
            print('숫자가 포함되어야 합니다.')
            return False    
        
    if hasUuper == False:
            print('대문자가 포함되어야 합니다.')
            return False

    print('안전한 비밀번호 입니다')

    return True

inputPassword = input('비밀번호를 입력하세요.(단, 최소 8글자, 숫자 1개이상, 대문자 최소 1개 포함)')
    
check_password(inputPassword)
    

# is_valid = check_password("Python1234")


# 1번 관문
if hasNumber == False:
    return False  # 번호표 없으면 여기서 바로 쫓겨남 (함수 끝)

# 2번 관문 (여기까지 왔다는 건 1번 관문을 통과했다는 뜻!)
if hasUuper == False:
    return False  # 대문자 없으면 여기서 쫓겨남 (함수 끝)

# 끝까지 살아남았다면 무조건 합격! (else가 필요 없음)
return True