def fun():
    print('module03의 함수가 실행됩니다.')

fun()

print(f'module03의__name__: {__name__}') 

if __name__=='__main__':         
    fun()

