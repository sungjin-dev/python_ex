# textFile = open('C:/psj/python/python_ex/home/0531.txt', 'w')

# textFile.close()




# textFile = open('C:/psj/python/python_ex/home/0531.txt', 'w')
# for i in range(1,9):
#     text0530 = f'지금은 {i}번째 차례입니다. \n'
#     textFile.write(text0530)
# textFile.close()
   
textFile = open('C:/psj/python/python_ex/home/0531.txt', 'r')

while True:

    line = textFile.readline()
    if not line:
        break
    print(line, end="")

textFile.close()













# f = open("C:/doit/새파일.txt", 'w')
# f.close()


# f = open("C:/psj/python/python_ex/home/0530.txt", 'w')
# for i in range(1, 11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)       # 줄바꿈없이 그대로 적기만 함 그래서 위해서 개행 한 것임
# f.close()


# f = open('C:/psj/python/python_ex/home/0530.txt', 'r')

# while True:
#     line = f.readline()  # 2. 뒤에 소괄호()를 꼭 붙여줍니다!
#     if not line:         # 더 이상 읽을 줄이 없으면(None 또는 빈 문자열)
#         break            # 반복문을 빠져나갑니다.
#     print(line, end="")  # 한 줄씩 출력합니다. (자동 줄바꿈 방지 end="")

# f.close()


textFile = open('C:/psj/python/python_ex/home/0530.txt', 'r')
line = textFile.readline()
print(line)
textFile.close()


textFile = open('C:/psj/python/python_ex/home/0530.txt', 'r')
while True:
    line = textFile.readline()
    if not line: break
    print(line)
textFile.close()

textFile = open('C:/psj/python/python_ex/home/0530.txt', 'r')
lines = textFile.readlines()        
for line in lines:
    print(line)
textFile.close()

'''
# 기능        readline() (단수형)                             readlines() (복수형)

# 읽어오는 양파일을 처음부터 딱 한 줄만 읽어옴         파일의 모든 줄을 끝까지 한 번에 다 읽어옴
# 반환 형식문자열 (String) ➡️ '1번째 줄입니다.\n      리스트 (List) ➡️ ['1번째 줄입니다.\n', '2번째 줄입니다.\n']특징
# 실행할 때마다 커서가 다음 줄로 이동함                파일 전체 내용을 통째로 메모리에 집어넣음
# 대용량 파일에 좋음. 반면 다보려면                    저용향 파일에 좋음. 리스트형태라서 가공하기 좋음.
#  while True로 일일히 다 끌어와야 함
'''

# readlines()의 편의성

f = open('0530.txt', 'r')
lines = f.readlines()

print(lines[4]) # 5번째 줄만 바로 출력!
f.close()

# 리스트 형식으로 저장되기 때문에 저격으로 데이터를 추출할 수 있다. 

f = open('0530.txt', 'r')
lines = f.readlines()

lines.reverse() # 리스트 순서를 통째로 뒤집기!
for line in lines:
    print(line, end="")
f.close()


f = open('0530.txt', 'r')
lines = f.readlines()

print(f"이 파일은 총 {len(lines)}줄로 되어 있습니다.")
f.close()

# ['1번째 줄','2번째 줄','3번째 줄', ....] 이런식이기 때문에 len()함수를 통해 알 수 있다.

f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

          # 대상     목적
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# with 문 안에서 만든 변수는 with 블록이 끝난 후에도 사용할 수 있다. 다음 예를 보자.
'''with 블록 안에서 만든 content 변수를 블록 밖에서도 사용할 수 있다.
 파이썬에서 if, for, while, with 블록은 변수의 사용 범위를 제한하지 않기 때문이다.'''

with open("test.txt", "w") as f:    
    content = "Hello, Python!"
    f.write(content)

print(content)  # "Hello, Python!" 출력

# 한글이 포함된 파일을 다룰 때는 인코딩을 명시하는 것이 좋다.

with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)