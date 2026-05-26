import config
from util import getDay, getTime    # 이런식으로 함수명을 하나하나 넣어주면 바로 쓸 수 있다


dFlag = True

while dFlag:
    selectedMenuNum = int(input('메뉴: 1.일기작성 2.일기조회 99.종료-->'))

    if selectedMenuNum == config.DIARY_WRITE:

        print(f' [{getDay()}] 일기를 작성하세요.')

        todayDiary = input()

        with open('C:\PSJ\diary.txt', 'a') as f:
            f.write(f'[{getDay()} {getTime()}] {todayDiary}\n')

    elif selectedMenuNum == config.DIARY_READ:
        
         with open('C:\PSJ\diary.txt', 'r') as f:
            str = f.read()
            print(str)

    elif selectedMenuNum == config.SYSTEM_SHUTDOWN:
        print('Bye~')
        dFlag = False
   