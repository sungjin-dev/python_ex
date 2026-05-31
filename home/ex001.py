# 1. 여기는 전역(Globals) 공간입니다.
global_var = "나는 전역변수"

def my_function():
    # 2. 여기는 함수 안, 즉 지역(Locals) 공간입니다.
    # 🔴 [여기에 빨간 점(중단점)을 찍어보세요!]
    local_var = "나는 지역변수" 
    print(local_var)
    print(global_var) 

# 함수 호출
my_function()