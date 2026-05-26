password = "mySecretPassword123!"
has_exclamation = False

for char in password:
    if char == '!':
        has_exclamation = True
        break # 찾았으면 더 반복할 필요 없이 탈출!

if has_exclamation:
    print("비밀번호에 느낌표(!)가 포함되어 있습니다.")


1. 리스트(List)와 튜플(Tuple) : "안에 있는 값을 그대로 준다"
리스트와 튜플은 순서대로 줄을 서 있는 상자들과 같습니다. 
그래서 for문을 돌리면 상자 안에 들어있는 실제 데이터(값)를 
하나씩 순서대로 i에 던져줍니다. 둘의 작동 방식은 완벽하게 똑같습니다.

2. 2. 딕셔너리(Dictionary) : "기본적으로 '키(Key)'만 준다" 🚨(가장 많이 헷갈리는 부분)
딕셔너리는 이름표(Key)와 내용물(Value)이 짝지어져 있죠. 
딕셔너리를 그냥 for문에 던져넣으면, 파이썬은 "내용물은 빼고 이름표(Key)만" 
i에 쏙쏙 뽑아줍니다.

# 1. 딕셔너리를 그냥 넣었을 때 -> i에는 'Key'만 들어옴
for i in my_dict:
    print(i)
# 출력: 이름, 나이, 직업

# 2. 내용물(Value)만 받고 싶을 때 -> .values() 사용
for i in my_dict.values():
    print(i)
# 출력: 홍길동, 20, 학생

# 3. 이름표와 내용물 둘 다 받고 싶을 때 -> .items() 사용 (변수 2개 필요)
for k, v in my_dict.items():
    print(f"키:{k}, 값:{v}")
# 출력: 키:이름, 값:홍길동 / 키:나이, 값:20 ...

2. .keys()만의 특별한 기능 (교집합/합집합 찾기)

old_users = {'gildong': 20, 'chanho': 25}
new_users = {'chanho': 26, 'minsoo': 30}

# 두 딕셔너리에 '모두' 존재하는 공통 아이디 찾기 (& 교집합 기호 사용)
common_keys = old_users.keys() & new_users.keys()

print(common_keys)