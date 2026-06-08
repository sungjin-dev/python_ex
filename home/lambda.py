from functools import reduce 


# lambda 입력값 : 결과물  일반 def 함수와 어떻게 매칭되는지

# sort(key=lambda ...) 조지기

# 내장 함수 삼총사 정복: 람다와 단짝 친구인 map(), filter(), reduce() 함수와 조합해서 데이터 솎아내는 법

# def plus(a, b):
#   return a+b

# lambda a,b : a+b

# fruits = ['apple', 'banana', 'kiwi', 'watermelon', 'pear']

# fruits.sort(key=lambda x: len())

# students = [
#     ['김철수', 25],
#     ['이영희', 22],
#     ['박민수', 29]
# ]

# students.sort(key= lambda x: x[1])

diary_files = ['산림욕_20260601', '비오는날_20260607', '퇴근길_20260605']
diary_files.split('_')
diary_files.sort(key = lambda x: x[1])
print(diary_files)
diary_files.sort(key=lambda x: x.split('_')[1])
print(diary_files)

#그 껍데기(구조)를 다 깨부수고 알맹이(요소) 속으로 곧바로 쳐들어간다"

'''람다 자체는 원본을 수정하지 않지만, 람다를 품고 있는 '주인님 함수'가 누구냐에 따라 원본의 운명이 바뀝니다.

이게 무슨 뜻이냐면, map과 filter는 람다를 만났을 때 새로운 데이터를 즉시 만들어서 메모리에 쌓아두지 않습니다! 그냥 "나중에 인간이 데이터 달라고 하면 그때 람다 공식 적용해서 하나씩 꺼내줄게~" 하고 영수증(대기표)만 발행해 둔 상태인 겁니다.

메모리에 새로운 리스트 공간을 쫙 만들어서 차지'''


numbers = [1,2,3,4,5,6,7]

total = reduce(lambda a,b : a + b, numbers)

reduce()와 함께 쓸 때는 무조건 매개변수를 딱 2개(a, b)만 써야 합니다.