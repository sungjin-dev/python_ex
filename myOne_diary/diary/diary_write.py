import cv2
from PIL import ImageFont, ImageDraw, Image
import session
import numpy as np
from pathlib import Path
from datetime import datetime

def write(diarydict):

    if session.getloginedMember() == '':
        print('로그인부터 하세요.')
        return diarydict
    
    mId = session.getloginedMember()
    
    user_folder = Path(f'./opencv_pictures/res/picturediary/{mId}')
    
    user_folder.mkdir(parents=True, exist_ok=True)

    folder_path = Path('./opencv_pictures/res/img')

    picturefiles = []

    for f in folder_path.glob('*.jpg'):

        picturefiles.append(f.name)

    for idx, picture in enumerate(picturefiles):
        print(f'[{idx+1}] {picture}')  

    selectedNum = int(input('먼저 일기 배경을 선택해주세요.'))

    selectedPictureName = picturefiles[selectedNum-1]

    myDiarytitle = input('일기 제목을 입력해주세요.')

    time = datetime.now().strftime("%Y-%m-%d %H시 %M분") 
    
    title = f'{time}_{myDiarytitle}'

    print('제목 완성!')
     
    writingDiary = input('일기를 작성해주세요.')

    uId = session.getloginedMember()

    if uId not in diarydict:
        diarydict[uId] = {
                'diary': {  
                },
            }
        
    diarydict[uId]['diary'][title] = writingDiary 

    print('작성 완료!')   

    img = cv2.imread(f'./opencv_pictures/res/img/{selectedPictureName}')
    if img is None:
        print("배경 이미지를 불러올 수 없습니다. 경로를 확인하세요.")
        return diarydict
    
    img = cv2.resize(img, (800, 600))
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)

    try:
        font = ImageFont.truetype("malgun.ttf", size=24)
    except IOError:
        print('기본 폰트를 사용합니다.')
        font = ImageFont.load_default()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")    

    draw.text((50, 100), f'제목: {myDiarytitle}\n날짜: {current_time}\n\n{writingDiary}', fill=(255, 255, 255), font=font,
    stroke_width=2, stroke_fill=(0, 0, 0))   

    result_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR) 

    # cv2.imwrite(f'{user_folder}/{myDiarytitle}.png', result_img)
    extension = '.png'  # 한글 호환 
    _, img_encoded = cv2.imencode(extension, result_img)
    img_encoded.tofile(f'{user_folder}/{title}{extension}')

    return diarydict


   

    