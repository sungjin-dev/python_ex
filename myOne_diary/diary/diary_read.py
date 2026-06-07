import cv2
import session
from pathlib import Path
import numpy as np

def pictureDiary(): 

    if session.getloginedMember() == '':
        print('로그인부터 하세요.')
        return 
    
    mId = session.getloginedMember()

    folder_path = Path(f'./opencv_pictures/res/picturediary/{mId}')

    pictureDiaryFiles = [f.name for f in folder_path.glob('*.png')]

    # if not pictureDiaryFiles:
    #     print("저장된 그림 일기가 하나도 없습니다.")
    #     return
    if not folder_path.exists() or not list(folder_path.glob('*.png')):
        print("저장된 그림 일기가 하나도 없습니다.")
        return   # 한글 호환됨
    
    for idx, title in enumerate(pictureDiaryFiles):
        print(f'[{idx+1}] : 그림일기 제목: {title}')

    selectedNum = int(input('원하는 그림일기를 선택하세요.'))

    choosenDiary = pictureDiaryFiles[selectedNum-1]

    diaryImagePath = f'./opencv_pictures/res/picturediary/{mId}/{choosenDiary}'

    img_array = np.fromfile(diaryImagePath, np.uint8)
    diaryImage = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if diaryImage is None:
        print("이미지를 불러오지 못했습니다. 파일이 손상되었거나 경로가 잘못되었습니다.")
        return

    cv2.imshow(f'MyDiary', diaryImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    return

    

   

      