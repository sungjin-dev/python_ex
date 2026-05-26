'''예제 3: 영화관 티켓 요금 계산기 (조건 중첩과 로직)
나이, 영화 종류, 시간대에 따라 티켓 가격을 계산하고 적립금까지 알려주는 함수를 만드세요.

함수 이름: book_ticket

받아야 할 입력값 (인자): age (나이: 정수), movie_type (영화 종류: "2D" 또는 "3D"), 
time_slot (상영 시간: "조조", "일반", "심야")

요금 계산 규칙:

기본 요금: "2D"는 10,000원, "3D"는 15,000원입니다.

나이 할인: 20세 미만(age < 20)이면 기본 요금에서 2,000원 할인됩니다.

시간대 할인: "조조"면 3,000원 할인, "심야"면 1,000원 할인됩니다. ("일반"은 변동 없음)

중요: 나이 할인과 시간대 할인은 중복 적용이 가능합니다. (예: 15세 학생이 2D 조조 영화를 보면 총 5,000원 할인되어 5,000원 결제)

포인트 적립: 최종 결제 금액의 5% 를 포인트로 적립해 줍니다. (포인트는 소수점이 나오지 않게 int()로 정수 처리하세요)

출력 및 반환: 함수 내부에서 요금 명세서(기본 요금, 총 할인 금액, 최종 금액, 적립 포인트)를 print()로 출력하고, 
최종 결제 금액과 적립 포인트를 튜플 형태로 return 하세요.'''


def book_ticket(age, movie_type, time_slot):

    totalPrice = 0
    totaldiscount = 0 

    if movie_type == '2D':
        basicPrice = 10000
        totalPrice += basicPrice
    
    elif movie_type == '3D':
        basicPrice = 15000
        totalPrice += basicPrice

    if age < 20:
        totalPrice -= 2000
        totaldiscount += 2000

    if time_slot == '조조':

        totalPrice -= 3000
        totaldiscount += 3000

    elif time_slot == '심야':

        totalPrice -= 1000
        totaldiscount += 1000

    elif time_slot == '일반':
        pass       

    milagePoint = int(totalPrice * 0.05) 

    print(f' 기본 요금: {basicPrice}, 총할인금액: {totaldiscount} , 최종금액: {totalPrice}, 적립포인트: {milagePoint}')

    return totalPrice, milagePoint
    
inputAge = int(input('나이를 입력하세요.'))  
inputMovieType = input('영화 종류를 입력하세요. (2D OR 3D)')  
inputRunningTime = input('상영시간대 입력하세요.(조조, 일반 , 심야)')

book_ticket(inputAge, inputMovieType, inputRunningTime)



