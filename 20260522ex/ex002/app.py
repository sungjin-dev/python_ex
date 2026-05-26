import module01
import module02
import module03

print('이 곳은 실행 파일입니다.')

print(f'실행파일의__name__: {__name__}')       # main이라는 값을 가짐. 문자열? 모듈에서 쓰면 그 모듈 이름

                                               # 여기서 실행하면 if __name__!='__main__':  이 상황이 되기 때문에 모듈부분은 실행x


# 호출될 때마다 해당 모듈이 실행되어버림 