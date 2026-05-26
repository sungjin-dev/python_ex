'''🌙 예제 5: 나이트클럽 입구 컷 (경비원 함수)
나이트클럽 입구를 지키는 엄격한 경비원 함수를 만들어 주세요. 
손님의 정보를 확인해서, 조건에 맞지 않으면 즉시 False를 외치며 쫓아내고(return),
 모든 관문을 무사히 통과한 손님에게만 True를 외치며 들여보내야 합니다.

함수 이름: check_guest

입력값 (인자): age (나이), dress_code (옷 스타일), is_drunk (만취 여부: True/False)

경비원의 입구 컷 조건 3가지:

나이 관문: 20세 미만(age < 20)이면 "미성년자는 출입 금지입니다."를 출력하고 쫓아냅니다. (False 반환)

만취 관문: 만취 상태(is_drunk == True)라면 "술 좀 깨고 오세요."를 출력하고 쫓아냅니다. (False 반환)

복장 관문: 옷 스타일(dress_code)이 "츄리닝"이거나 "슬리퍼"라면 "복장 불량으로 입장 불가입니다."를 출력하고 쫓아냅니다. (False 반환)

합격: 위의 세 가지 관문을 모두 무사히 통과했다면 마지막에 딱 한 번 "환영합니다! 즐거운 시간 보내세요."를 출력하고 True를 반환합니다.

💡 핵심 포인트: else나 elif를 단 한 번도 쓰지 말고, 오직 **if와 return의 조합(Early Return)**만으로 코드를 짜보세요!

아래 틀을 복사해서 풀어보세요!'''


# 1) boolean(True)이 아니라 글자("True" 또는 "T")랑 비교하기!
# if is_drunk == 'True' or is_drunk == 'T': 
#     print('술 좀 깨고 오세요.')
#     return False

def check_guest(age, is_drunk, dress_code):
    
    if age < 20:
        print('미성년자는 출입 금지입니다.')
        return False
    
    if is_drunk == True:
        print('술 좀 깨고 오세요.')
        return False
    
    if dress_code == '츄리닝' or dress_code == '슬리퍼':
        print('복장 불량으로 입장 불가입니다.')
        return False
    
    print('환영합니다! 즐거운 시간 보내세요.')   
    
    return True

guestAge = int(input('나이 : '))
guestdrunk = input('만취여부(T/F) : ')
guestDressCode = input('옷스타일 : ')

check_guest(guestAge, guestdrunk, guestDressCode)



# 테스트 해보기
# result = check_guest(25, "정장", False) # 합격해야 함
# result = check_guest(22, "츄리닝", False) # 3번 관문 탈락