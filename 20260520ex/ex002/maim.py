'''
사용자가 3과목의 시험 점수를 입력하면 총점, 평점, 통과 여부를 출력하는 프로그램을 모듈을 이
용해서 만들어 봅시다. 시험 통과 여부는 평점이 60이상이고 한 과목도 40미만이 없다면 'Pass', 
그렇지 않으면 'Fail'로 판정합니다.
'''

import examCalculator

score1 = int(input('과목 점수를 입력하세요.'))
score2 = int(input('과목 점수를 입력하세요.'))
score3 = int(input('과목 점수를 입력하세요.'))

print(f'총점: {examCalculator.getTotalScore(score1, score2, score3)}')
print(f'총점: {examCalculator.getAverageScore(score1, score2, score3)}')
print(f'총점: {examCalculator.getPassorFail(score1, score2, score3)}')

