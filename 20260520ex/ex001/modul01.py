# # quiz) 단위환산 프로그램
# '''
# mm 단위의 길이를 입력하면 cm, m, inch, ft 등으로 단위가 변환되어 
# 출력되는 함수가 포함된 프로그램을 만들어 봅시다. 
# '''

# def convertUnit(lenMm):   # lenMm : 매개변수
#     unitDic = {}

#     unitDic['cm'] = lenMm * .1      이말은 unitDic이라는 딕셔너리에서 'cm'키값에 들어가서 값을 넣는 것 혹은 변경
#     unitDic['m'] = lenMm * .001
#     unitDic['inch'] = lenMm * .03937
#     unitDic['feet'] = lenMm * .003281

#     return unitDic

# def printLength(lengths):
#     for len in lengths.keys():     
#         print(f'{len}: {lengths[len]}{len}')  #   

# inputMmData = int(input('길이(mm)를 입력하세요.'))

# resultData = convertUnit(inputMmData)
# printLength(resultData)

# quiz) 할인된 상품 가격표 출력 프로그램
'''
DW마트는 고객 감사의 일환으로 ‘오늘의 할인’ 이벤트를 진행할 계획입니다. 아래
의 상품 가격표를 참고해서 ‘오늘의 할인율’을 입력하면 할인된 가격이 출력되는 프
로그램을 만들어 봅시다.
쌀: 9,900
상추: 1,900
고추: 2,900
마늘: 8,900
통닭: 5,600
햄: 6,900
치즈: 3,900
'''

standardPrice = {
    '쌀': 9900,
    '상추': 1900,
    '고추': 2900,
    '마늘': 8900,
    '통닭': 5600,
    '햄': 6900,
    '치즈': 3900
}

def discountedPrices(rate):
    dcprice = {}
    
    for goodsnametemp in standardPrice.keys():
        dispricestemp = int(standardPrice[goodsnametemp] * (1-(rate/100)))
        dcprice[goodsnametemp] = dispricestemp       #standardPrice[goodsnametemp] = dispricestemp -> 이건 전역변수를 바꾸는 행위
        
    return dcprice       

def printdisprices(pricelist):

    for goodstemp, pricestemp in .items():
        print(f'{goodstemp}: {standardPrice[goodstemp]}, {userInputRate} % DC : {pricestemp}')       

userInputRate = int(input('할인율을 입력하세요.'))

discountedDict = discountedPrices(userInputRate)
printdisprices(discountedDict)




def getDiscountPrice(rate):
    dcPrice = {}

    for goodsName in standardPrice.keys():         # 전역데이터 standardPrice
        disPrice = int(standardPrice[goodsName] * (1-(rate/100)))       # 소수점 버리기 위해서 intcasting

        dcPrice[goodsName] = disPrice     # 지역 내 딕셔너리에 차곡 차곡 쌓아올린다   
    
    return dcPrice                        # 지역변수를 외부에 활용할 수 있도록 리턴해준다

def printPrice(priceList):
    for goodsName, goodsPrice in priceList.items():
        print(f'{goodsName}\t: {standardPrice[goodsName]}원 {inputRateData}%DC: {goodsPrice}원')

inputRateData = int(input('오늘의 할인율 입력:'))
discountPrices = getDiscountPrice(inputRateData)   # dcPrice = {} 할인된 가격묶음이 discountPrices 여기에 저장 
printPrice(discountPrices) 


#부품의 재사용 (레고 블록처럼)
#함수를 세분화해 두면, 나중에 다른 기능을 만들 때 아주 편해집니다.

#신기한 현상의 비밀은 바로 "매개변수(Parameter)는 성벽에 뚫어놓은 '문(Gate)'이자 '터널'이기 때문"
# 매개변수 ()를 선언하는 순간 외부와 연결되는 통로가 뚫립니다.

#  함수가 외부 변수에 너무 의존하면 나중에 재사용하기 어려워집니다.

# ① 🌍 진짜 변수 (현실의 데이터 창고 / 전역 변수)
# 프로그램 전체에서 살아 숨 쉬며 진짜 데이터를 들고 있는 변수들입니다.

# standardPrice: 기본 상품 가격이 담긴 데이터 원본 (코드에는 안 보이지만 밖에 선언되어 있죠?)

# inputRateData: 사용자가 키보드로 입력한 '진짜 할인율 숫자'

# discountPrice: 함수가 계산해서 돌려준 '최종 할인 가격 데이터'

# 🏷️ 매개변수 (함수 입구의 "가짜 이름표" / Parameter)
# 함수를 정의할 때 def 함수명(이름표):

# rate: getDiscountPrice 함수 안으로 들어오는 할인율을 받기 위한 이름표

# priceList: printPrice 함수 안으로 들어오는 딕셔너리 데이터를 받기 위한 이름표

# ⏳ 임시 변수 (함수 안에서만 잠깐 쓰는 부속품 / 지역 변수)
# 함수 내부나 for문 안에서 계산을 위해 잠깐 만들어졌다가, 함수가 끝나면 먼지처럼 사라지는 변수들입니다.

# dcPrice: 할인된 가격들을 임시로 모아두는 빈 딕셔너리

# goodsName, goodsPrice: for문이 한 바퀴 돌 때마다 상품명과 가격을 하나씩 잠깐 담아두는 바구니

# disPrice: 할인 가격 계산 공식의 결과값을 잠깐 저장하는 변수

# "데이터가 택배 박스에 담겨서 함수라는 공장으로 배달된다"
# 구조적으로 헷갈리지 않으려면 이름을 짓는 규칙(Naming Convention)을 스스로 정하는 것이 가장 좋음

# 💡 딱 이것만 기억하세요!
# def 줄에 있는 괄호 안의 글자들(rate, priceList)은 진짜 변수가 아니라,
# 들어오는 데이터를 맞이하는 가짜 이름표(바구니)일 뿐이다.

# 함수 안에서 대입 연산자(=)로 새로 만든 변수들은 함수가 끝나면 사라지는 임시 부속품이다.

# 함수 맨 밑 바깥에서 사용자가 직접 입력받거나 함수 호출 결과를
# 대입한 변수(inputRateData, discountPrice)들만 끝까지 살아있는 진짜 변수다.

# # quiz) 영어 사전
# englishDictionary = {
#     'apple': '사과',
#     'chair': '의자',
#     'doll' : '인형',
#     'book' : '책',
#     'piano': '피아노',
#     'clock': '시계',
# }

# def printword(engWord):
#     print(f'{engWord}: {englishDictionary[engWord]}')

# printword(input('찾고자 하는 영어 단어 입력: '))


# random
# copy


# 파이썬 재단의 인증 -> 내장함수만 

