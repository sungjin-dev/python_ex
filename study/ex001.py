import random

class randomGame:

    def __init__(self):

        self.totalanswer = 0
        self.totalcount = 1

        self.eng = [
            'travel', 'culture', 'history', 'science', 'nature', 'language', 'subject', 'message', 'concert', 'kitchen',
            'memory', 'success', 'failure', 'dream', 'purpose', 'experience', 'opinion', 'mistake', 'habit', 'character',
            'unique', 'popular', 'modern', 'special', 'perfect', 'dangerous', 'comfortable', 'famous', 'careful', 'honest',
            'create', 'design', 'discover', 'imagine', 'develop', 'improve', 'protect', 'provide', 'support', 'understand',
            'agree', 'refuse', 'accept', 'express', 'worry', 'communication', 'community', 'global', 'environment', 'technology'
        ]

        self.kor = [
            '여행', '문화', '역사', '과학', '자연', '언어', '주제', '메시지', '콘서트', '주방',
            '기억', '성공', '실패', '꿈', '목적', '경험', '의견', '실수', '습관', '성격',
            '독특한', '인기 있는', '현대적인', '특별한', '완벽한', '위험한', '편안한', '유명한', '조심스러운', '정직한',
            '창조하다', '디자인하다', '발견하다', '상상하다', '발전시키다', '향상시키다', '보호하다', '제공하다', '지원하다', '이해하다',
            '동의하다', '거절하다', '받아들이다', '표현하다', '걱정하다', '의사소통', '공동체', '세계적인', '환경', '기술'
        ]

    def problem(self):

        flag = True

        while flag:

            selectedNumber = int(input('1. 문제 풀기, 2. 정답 수 99. 종료  '))

            if selectedNumber == 1:

                randomNum = random.randint(0,49)

                print(f'문제 : {self.eng[randomNum]}')

                userAnswer = (input('정답을 입력하세요.'))

                if userAnswer in self.kor:
             
                    answerIdx = self.kor.index(userAnswer)

                    if randomNum == answerIdx:
                        print('정답입니다.')
                        self.totalanswer += 1
                    else:
                        print('정답이 아닙니다.')   
                else:
                    print('오타거나 정답이 아닙니다.')        

            elif selectedNumber == 2:
                print(f'총 정답수 : {self.totalanswer}')    

            elif selectedNumber == 99:
                print('게임을 종료합니다.')
                flag = False

            else : 
                print('오타거나 잘못 입력하셨습니다.') 

            if self.totalcount > 10:
                print('10문제 모두 풀었습니다.')
                flag = False    

            self.totalcount += 1     

randomGame().problem()


                




