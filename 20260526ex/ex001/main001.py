import module_ex001 as game

data = ['가위', '바위', '보']

rockPaperScissors = []

print( '가위바위보 게임을 실행합니다.')

rockPaperScissors.append(input('가위, 바위, 보 중 하나를 입력하세요: '))

game.userRPSdata(rockPaperScissors)   
game.setRNumber()

print(f' 결과: {game.compareNumber()}')
print(f' 사용자 : {rockPaperScissors}, 컴퓨터 : {game.getRNumber()}')