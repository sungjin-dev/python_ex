import session
from pathlib import Path
import cv2
from datetime import datetime
import numpy as np
from PIL import ImageFont, ImageDraw, Image
        
def update(diarydict): 

    if session.getloginedMember() == '':
        print('로그인부터 하세요.')
        return diarydict
    
    mId = session.getloginedMember()

    if mId not in diarydict or not diarydict[mId]['diary']:
        print('수정할 일기가 없습니다.')
        return diarydict    
       
    user_path = Path(f'./opencv_pictures/res/picturediary/{mId}')

    sortedTitles = sorted(diarydict[mId]['diary'].keys(), reverse=True)

    for idx, title in enumerate(sortedTitles):
        print(f'[{idx+1}] : 그림일기 제목: {title}')

    selectedNum = int(input('바꾸고 싶은 그림일기를 선택하세요.'))

    selectedTitle = sortedTitles[selectedNum-1]

    folder_path = Path('./opencv_pictures/res/img')

    picturefiles = []

    for f in folder_path.glob('*.jpg'):

        picturefiles.append(f.name)

    for idx, picture in enumerate(picturefiles):
        print(f'[{idx+1}] {picture}')

    selectedBackGround = int(input('일기 배경을 다시 선택해주세요.'))

    selectedPictureName = picturefiles[selectedBackGround-1]
     
    rewritingDiary = input('다시 일기를 작성해주세요.')

    uId = session.getloginedMember()

    if uId not in diarydict:
        diarydict[uId] = {
                'diary': { 
                },
            }

    diarydict[uId]['diary'][selectedTitle] = rewritingDiary 

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

    draw.text((50, 100), f'제목: {selectedTitle}\n날짜: {current_time}\n\n{rewritingDiary}', fill=(255, 255, 255), font=font,
    stroke_width=2, stroke_fill=(0, 0, 0))   

    result_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR) 

    extension = '.png'  
    _, img_encoded = cv2.imencode(extension, result_img)
    img_encoded.tofile(str(user_path / f"{selectedTitle}{extension}"))

    return diarydict


        