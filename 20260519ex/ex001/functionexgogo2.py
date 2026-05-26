'''예제 2: 텍스트 기반 단어 수 및 금지어 필터링 함수
사용자가 작성한 글을 분석하여 총 단어 수를 세고, 비속어나 금지어가 포함되어 있으면 
다른 문자(*)로 가려주는 보안 함수를 만드세요.

단어 수 계산: 공백(띄어쓰기)을 기준으로 이 문장에 단어가 총 몇 개 있는지 세어서 출력하세요. 
(힌트: 문자열을 쪼개는 메서드 활용)

금지어 마스킹: 문장 중에 바보, 멍청이 라는 단어가 포함되어 있다면, 
각각 , *** 처럼 글자 수에 맞게 * 기호로 변경(치환)하세요.

출력 형태: 함수 내부에서 [분석 결과] 총 단어 수: X개를 출력하고, 
금지어가 깔끔하게 가려진 최종 수정된 문자열을 return(반환) 하세요.
'''
'''
1) 중복 or 둘다 같이 나오는 경우 해결 : if elif가 아니라 if if, 그리고 for 반복문 쓰기
'''
# 예제 2 틀

def filter_text(user_text):

    userTextLsit = user_text.split()

    countWords = len(userTextLsit) 

    for idx in range(len(userTextLsit)):
        if userTextLsit[idx] == '바보':
            userTextLsit[idx] = '**'
            
        if  userTextLsit[idx] == '멍청이':
            userTextLsit[idx] = '***'

    cleaned_text = ' '.join(userTextLsit)  

    print(f' 단어수: {countWords}, 수정된 텍스트: {cleaned_text}')

    return countWords, cleaned_text

userInputText = str(input('글을 작성하세요.'))

# result2 = filter_text("오늘 파이썬 공부를 했는데 나는 바보 인가봐")

filter_text(userInputText)


# words = ['나는', '천재다']

# # ❌ 틀린 예시 (이렇게 쓰면 에러가 납니다!)
# result = words.join(" ") 
# # 에러 메시지: AttributeError: 'list' object has no attribute 'join'

# # ⭕ 맞는 예시 (본드(" ")가 먼저 오고, 괄호 안에 리스트를 넣어야 합니다)
# result = " ".join(words) 
# print(result) # 출력: "나는 천재다"

# phone = ['010', '1234', '5678']

# # 1. 짝대기로 붙이기 (전화번호 만들 때 최고!)
# print("-".join(phone))  
# # 출력: 010-1234-5678

# # 2. 이모지로 붙이기 (응용)
# words = ['파이썬', '코딩', '성공']
# print(" 🚀 ".join(words)) 
# # 출력: 파이썬 🚀 코딩 🚀 성공



💡 보너스 꿀팁: 파이썬이 제공하는 치트키 (.replace())


def filter_text(user_text):
    # 1. 단어 수 세기 (이건 split이 필요함)
    countWords = len(user_text.split()) 
    
    # 2. 금지어 바꾸기 (쪼갤 필요 없이 원본 문장에서 바로 교체!)
    cleaned_text = user_text.replace('바보', '**')
    cleaned_text = cleaned_text.replace('멍청이', '***')
    
    print(f'단어수: {countWords}, 수정된 텍스트: {cleaned_text}')
    return countWords, cleaned_text