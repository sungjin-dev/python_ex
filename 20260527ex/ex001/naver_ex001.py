# 제공해주신 코드는 이미 VS Code(Visual Studio Code)에서 바로 실행할 수 있는 훌륭한 파이썬 코드입니다! 다만, VS Code 환경이나 파이썬 버전 환경에 따라 실행 시 에러를 일으킬 수 있는 치명적인 버그 2가지와 모듈 누락이 있어서 그 부분을 명확하게 수정해 드려야 할 것 같아요.

# VS Code에서 실행하기 전 꼭 수정해야 할 부분
# 1. urllib.parse 모듈 누락 (NameError 방지)
# 코드 내부에서 urllib.parse.quote()를 사용하고 계시지만, 정작 파일 최상단에는 import urllib.parse가 빠져 있습니다. 이대로 실행하면 NameError가 발생합니다.

# 2. response.read() 중복 호출 문제 (None 반환 버그)
# getRequestUrl 함수 안에서 주석 처리된 print문 바로 아래를 보시면 다음과 같이 작성되어 있습니다.


# response.read()가 비어있게 되는 원인
# if response.getcode() == 200:
#     print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
#     return response.read().decode('utf-8')
# # 파이썬의 response.read()는 한 번 호출하여 데이터를 읽고 나면 스트림이 닫혀서 두 번째 호출할 때는 빈 값("")을 반환합니다. 주석 처리된 곳에서 비록 실행은 안 되었지만, 추후 주석을 풀거나 코드를 수정할 때 안전하도록 데이터를 변수에 한 번만 담아서 처리하는 것이 정석입니다.

# 3. 네이버 API의 페이지 제한 (while문 무한 루프 또는 에러 방지)
#네이버 검색 API는 start 인덱스 값이 1000을 넘어가면 에러(400 Bad Request)를 뱉거나 멈추게 되어 있습니다. 검색 데이터가 아무리 많아도 start 값이 1000을 넘지 않도록 안전장치를 걸어주어야 VS Code에서 프로그램이 뻗지 않습니다.

import urllib.request
import urllib.parse  # 💡 필수 모듈 추가
import datetime
import json

# 네이버 API 개발자 센터 Key (본인 Key 입력)
client_id = 'qU7Vv0lpL6Vn_xp0A_M5'
client_secret = 'BqTjXFOz8m'

# NAVER에서 원본 데이터 가져오는 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            
            # 💡 데이터를 변수에 안전하게 한 번만 읽어옵니다.
            responseData = response.read().decode('utf-8')
            return responseData
            
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None

# NAVER에서 데이터 검색 하는 함수
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)

# 데이터 가공 및 리스트 추가 함수
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    
    # 날짜 포맷팅 예외 처리 (간혹 포맷이 다를 경우 프로그램 다운 방지)
    try:
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        pDate = post['pubDate']

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():
    node = 'news'
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []

    start = 1
    display = 100
    jsonResponse = getNaverSearch(node, srcText, start, display)
    
    if jsonResponse is not None and 'items' in jsonResponse and len(jsonResponse['items']) > 0:
        print(f"👉 총 검색 결과(total): {jsonResponse['total']}건")
        print(f"👉 첫 번째 뉴스 제목: {jsonResponse['items'][0]['title']}")
    else:
        print("검색 결과가 없거나 오류가 발생했습니다.")
        return

    # 데이터 수집 반복문
    while jsonResponse is not None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        # 💡 네이버 API 한계(start 최대 1000) 및 전체 개수 도달 시 탈출 조건 추가
        next_start = jsonResponse['start'] + jsonResponse['display']
        if next_start > 1000 or next_start > jsonResponse['total']:
            break

        jsonResponse = getNaverSearch(node, srcText, next_start, display)

    # 파일로 저장 (💡 VS Code 실행 위치 기준 저장)
    filename = f'{srcText}_naver_{node}.json'
    with open(filename, 'w', encoding='utf8') as f:
        # sort_keys=False로 해야 우리가 딕셔너리에 넣은 순서(cnt, title...)대로 이쁘게 저장됩니다.
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=False, ensure_ascii=False)
        f.write(jsonFile)
        
    print(f'💾 수집 완료! [{filename}] 파일로 성공적으로 저장되었습니다. (총 {cnt}개)')

if __name__ == '__main__':
    main()