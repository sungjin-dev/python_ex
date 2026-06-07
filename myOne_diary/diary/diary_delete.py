from pathlib import Path
import session

def delete(diarydict):

    if session.getloginedMember() == '':
        print('로그인부터 하세요.')
        return diarydict
    
    mId = session.getloginedMember()

    folder_path = Path(f'./opencv_pictures/res/picturediary/{mId}')

    pictureDiaryFiles = [f.name for f in folder_path.glob('*.png')]

    if not folder_path.exists() or not list(folder_path.glob('*.png')):
        print("저장된 그림 일기가 하나도 없습니다.")
        return diarydict
    
    for idx, title in enumerate(pictureDiaryFiles):
        print(f'[{idx+1}] : 그림일기 제목: {title}')

    sortedDiaries = sorted(pictureDiaryFiles, reverse=True)

    selectedNum = int(input('삭제하고 싶은 그림일기를 선택하세요.'))

    selectedDiary = sortedDiaries[selectedNum-1]

    deleteDiray = input(f'{selectedDiary} 일기를 정말 삭제하시겠습니까? (Y/N): ')
    
    if deleteDiray.upper() == 'Y':
        try:
           (folder_path/selectedDiary).unlink()
           print(f'{selectedDiary} 그림일기가 성공적으로 삭제되었습니다.')
        except Exception as e:
            print(f'파일 삭제 중 오류가 발생했습니다: {e}')
    else:
        print('삭제하기 아까우면 되돌아가기')

    return diarydict