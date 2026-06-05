import cv2
from diary import diary_service
from PIL import ImageFont, ImageDraw, Image
import session
import numpy as np

class Opencv:
    def __init__(self):
        self.diaries = {}

    def diaryOpencv(self):

        self.diaries = diary_service.DiaryService().load_diaries()  

        readingImg = cv2.imread('C:/pjt/python/opencv_personal/res/img/reading.jpg')

        uId = session.getloginedMember()

        myDiaries = self.diaries[uId]['diary']

        if len(myDiaries) > 0:
            recent_diary = myDiaries[0]
        else:
            recent_diary = "No diary yet!"

        img_pil = Image.fromarray(readingImg)
        draw = ImageDraw.Draw(img_pil)    

        font = ImageFont.truetype("malgun.ttf", 40)

        draw.text((100, 150), recent_diary, font=font, fill=(0, 255, 255))

        readingImg = np.array(img_pil)

        cv2.imshow('Result', readingImg)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

