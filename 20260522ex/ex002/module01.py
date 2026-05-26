def fun():
    print('module01의 함수가 실행됩니다.')

# fun() 

# print(f'module01의__name__: {__name__}')              # 파이썬이 만들어준 전역변수

if __name__=='__main__':         # 여기서 실행하면 여기가 main이니까 실행됨 
    fun()                        # main과 모듈의 분기점은 전역변수 __main__ or __모듈명__ 여부임
                                 # java는 명확히 지정해줌 파이썬만의 특징

