# 예제 1: 쇼핑몰 할인율 계산 및 영수증 발행 함수
# 사용자가 물건을 살 때, 구매 금액에 따라 할인율을 
# 다르게 적용하고 최종 결제 금액을 알려주는 함수를 만드세요.

''' 함수 이름: calculate_receipt

# 받아야 할 입력값 (인자): price (구매 금액), is_member (회원 여부: True 또는 False)

# 할인 조건 규칙:

# 구매 금액이 100,000원 이상이면 기본 10% 할인

# 구매 금액이 50,000원 이상 100,000원 미만이면 기본 5% 할인

# 50,000원 미만은 할인 없음 (0%)

# [보너스 조건] 만약 is_member가 True(회원)라면, 
# 위의 조건으로 계산된 최종 금액에서 추가로 2,000원을 더 깎아줍니다. 
# (단, 최종 금액이 0원 이하로 내려가면 안 되며 최소 결제 금액은 0원입니다.)

# 출력 형태: 함수 내부에서 print()를 사용해 할인율, 할인된 금액, 
# 최종 금액을 예쁘게 출력하고, 마지막에 최종 결제 금액을 return(반환) 하세요.'''


# totalPurchased = 0
# memberDiscount = 2000
# discountrate1 = 10
# discountrate2 = 5
# discountrate3 = 0
# ismember = True
# flag = True

# def definedIsmember(inputInt):
#     global ismember

#     if inputInt == 1:
#         ismember = True     

#     if inputInt == 2:
#         ismember = False 

# selectedIsmember = int(input('회원이시면 1번, 비회원이시면 2번을 눌러주세요.'))
# definedIsmember(selectedIsmember)


# def calculate_receipt(price): 

#     global totalPurchased

#     if price > 100000 and ismember == True:
#         price = price * (1-(discountrate1/100))
#         totalPurchased += price
#         totalPurchased -= memberDiscount
#         print(f' 할인율 : {discountrate1}, 총할인금액 : {price * (discountrate1/100)+memberDiscount} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)
    
#     elif price > 100000 and ismember == False:
#         price = price * (1-(discountrate1/100))
#         totalPurchased += price
#         print(f' 할인율 : {discountrate1}, 총할인금액 : {price * (discountrate1/100)} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)
            
#     elif 50000 <=price < 100000 and ismember == True:
#         price = price * (1-(discountrate2/100))
#         totalPurchased += price 
#         totalPurchased -= memberDiscount
#         print(f' 할인율 : {discountrate2}, 총할인금액 : {price * (discountrate2/100)+memberDiscount} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)
    
#     elif 50000 <=price < 100000 and ismember == False:
#         price = price * (1-(discountrate2/100))
#         totalPurchased += price
#         print(f' 할인율 : {discountrate2}, 총할인금액 : {price * (discountrate2/100)} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)

#     elif price < 50000 and ismember == True:
#         totalPurchased += price 
#         totalPurchased -= memberDiscount
#         print(f' 할인율 : {discountrate3}, 총할인금액 : {1-((100-discountrate3)/100)+memberDiscount} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)
    
#     elif price < 50000 and ismember == False:
#         totalPurchased += price 
#         print(f' 할인율 : {discountrate3}, 총할인금액 : {1-((100-discountrate3)/100)} 총결제금액 : {totalPurchased}')
#         return(totalPurchased)
    
#     elif price < memberDiscount and ismember == True:
#         memberDiscount = 0

# purchasedInputPrice = int(input('구매금액을 입력하시오.'))

# calculate_receipt(purchasedInputPrice)


'''
1) discount_amount(할인될 금액)라는 변수를 하나 따로 만들어서 계산해 두면 훨씬 편합니다.
2) 함수에서 따로 return하지 않고 완벽하게 구현된다면 따로 호출할 필요 x
3) 0원 방지 처리는 if-elif 덩어리에 끼워 넣지 마세요. 
모든 할인(기본 할인 + 회원 2000원 할인) 계산이 완전히 다 끝난 함수의 
맨 마지막 줄에서 if totalPurchased < 0: 일 때 0원으로 만들어버리는 것이 제일 깔끔
4) return 쓸 때  괄호 금지
5)  함수 안에서 쓸 변수들은 안에서 해결하자. (global 남용 x)
'''
'''
# 수정 후 목표
def calculate_receipt(price, is_member):
    # 재료를 두 개 받아서 여기서 지지고 볶고, return으로 결과만 쏙 던져주기
'''

# totalPurchased = 0
# memberDiscount = 2000
# discountrate = 0
# discountrate1 = 10
# discountrate2 = 5
# discountrate3 = 0
# discountedPrice = 0
# ismember = True
# flag = True

# def definedIsmember(price, inputInt):
#     global ismember
#     global discountrate
#     global totalPurchased
#     global memberDiscount

#     if price > 100000:
#         discountrate = discountrate1
#         discountedPrice = price * ((100-discountrate1)/100)
#         totalPurchased += discountedPrice 

#     elif 50000 <= price < 100000:
#         discountrate = discountrate2
#         discountedPrice = price * ((100-discountrate2)/100)
#         totalPurchased += discountedPrice

#     elif price < 50000:
#         discountrate = discountrate3
#         totalPurchased += price * ((100-discountrate3)/100)

#     if inputInt == 1:
#         ismember = True     
#         totalPurchased -= memberDiscount
        
#     if inputInt == 2:
#         ismember = False

#     if totalPurchased < 0:
#         memberDiscount = totalPurchased

# purchasedInputPrice = int(input('구매금액을 입력하시오.'))
# selectedIsmember = int(input('회원이시면 1번, 비회원이시면 2번을 눌러주세요.'))


# definedIsmember(purchasedInputPrice, selectedIsmember)

# totaldiscountPrice = purchasedInputPrice - totalPurchased

# print(f' 할인율 : {discountrate}, 총할인금액 : {totaldiscountPrice} 총결제금액 : {totalPurchased}')



# 3차 북벌

 # 바깥에 잡다한 변수들을 미리 만들지 않습니다!

def calculate_receipt(price, inputInt):
    # 함수 안에서 쓸 변수들을 여기서 새로 만듭니다. (global 필요 없음)
    total_purchased = price  # 일단 원가를 넣고 시작
    discount_rate = 0        # 최종 할인율 기록용
    
    # 1. 금액별 할인 계산 (total_purchased와 discount_rate의 값을 바꿈)
    if price >= 100000:
        discount_rate = 10
        total_purchased = price * ((100-discount_rate)/100)
    
    elif price >= 50000:
        discount_rate = 5
        total_purchased = price * ((100-discount_rate)/100)
       
    else:
       total_purchased = price * ((100-discount_rate)/100)

    # 2. 회원이라면 2,000원 추가 할인
    if inputInt == 1:
        total_purchased -= 2000

    # 3. 0원 이하 방지 (모든 할인이 끝난 후 검사)
    if total_purchased < 0:
        total_purchased = 0

    # 4. 결과값 2개(최종금액, 할인율)를 튜플 형태로 바깥으로 던져줌!
    return total_purchased, discount_rate


# --- 함수 밖 (메인 프로그램) ---
purchasedInputPrice = int(input('구매금액을 입력하시오: '))
selectedIsmember = int(input('회원이시면 1번, 비회원이시면 2번: '))

# @@@@ 함수(자판기)에 동전 2개를 넣고, 결과물 2개를 뽑아서 변수에 담습니다!@@@@@
final_price, applied_rate = calculate_receipt(purchasedInputPrice, selectedIsmember)

# 총 할인 금액은 말씀하신 아이디어대로 밖에서 구합니다.
total_discount = purchasedInputPrice - final_price

print(f'할인율: {applied_rate}%, 총할인금액: int{total_discount}원, 최종결제금액: int{final_price}원')

    


