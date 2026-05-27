# API는 Application Programming Interface(애플리케이션 프로그래밍 인터페이스)

# 쉽게 말해, 서로 다른 소프트웨어 프로그램들이 서로 소통하고 
# 데이터를 주고받을 수 있도록 해주는 "다리(연결고리)"

# JSON은 데이터 교환 형식
# - 쉽게 말해 프로그램끼리 데이터를 쉽게 주고 받기 위해서

# 1) 딕셔너리 구조라서 가독성이 좋다
# 2) 컴퓨터가 처리하기 쉬움.  가볍고 전송속도도 빠름
# 3) 대부분 언어 호환성이 좋음. 
# 4) 현재 웹개발 및 웹API로 가장 널리 사용

import urllib.request     # 웹에 있는 데이터나 페이지를 요청(Request)하고 가져오는(Response) 기능을 가진 내장 모듈
import urllib.parse       # URL 인코딩(URL Encoding) 해주는 함수  공백 " " → %20  한글 같은 특수 문자 → UTF-8 기반 %XX 형태로 변환/ 는 기본적으로 인코딩되지 않음
import datetime
import json

client_id = '1JpN61biLGVpu23H0EBN'
client_secret = 'XHNI8GJKHu'

#Naver에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)                # 요청서 
    req.add_header('X-Naver-Client-Id', client_id)   # 내 로그인 정보를 넣는 과정
    req.add_header('X-Naver-Client-Secret', client_secret)
                          
    try:                                        # 파이썬은 안 해도 되긴 하지만 문제 시 셧다운 될 수 있음
        response = urllib.request.urlopen(req)  # 상태코드값 http응답코드  100번대 요청 진행중 200번대 성공 300번대 리다이렉트(다른위치) - 데이터를 안 가지고 있어서 다른 곳에서 요청 400번대 클라이언트 오류 500번대 서버 오류   
        if response.getcode() == 200:       
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            #  decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것. 인코딩의 반대
        responseData = response.read().decode('utf-8')   # 디코딩
        return responseData
    
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None
    
#NAVER에서 데이터 검색하는 녀석
def getNaverSearch(node, srcText, start, display):   #  getRequestUrl(url) 이 함수가 호출되기 전에는 이 함수가 선언되어야함
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'                           # /[카테고리].json 
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    # “서버로 보내기 전에 URL에서 안전하게 사용할 수 있는 형태로 문자열을 변환한다” 
    # URL은 원래:영문, 숫자, 일부 특수문자만 안전하게 사용할 수 있습니다.( %20, %EC)
    # urllib.parse.unquote()  디코딩 하는 방법
    url = base + node + parameters     # 💡 나눠서 조립한 이유 (각각 재조립할 수 있어서 재사용하기 좋음)
    responseDecode = getRequestUrl(url)

    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)     # json 형태로 바꿔주는 모듈
    
def getPostData(post, jsonResult, cnt):       # 알맹이만 추출: 기사 제목(title), 설명(description), 원래 링크(originallink), 네이버 링크(link), 발행일(pubDate)만 
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    try:
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')   # pubDate 네이버서버가 지정한 딕셔너리 key값임
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        pDate = post['pubDate']     # 비상대책: 그냥 원본 쓰자

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():
    node = 'news'   # 크롤링 하는 대상  API의 데이터 종류(카테고리)
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')
    # 네이버가 보내준 데이터(응답)가 정상적으로 존재, 네이버가 이번에 가져다준 뉴스 개수가 0개가 아니며

    while jsonResponse != None and jsonResponse['display'] != 0 and cnt < 300:    # 범위를 제한하고 싶을 때는 cnt
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)
  
    # 파일로 저장
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)

if __name__ == '__main__':
    main()                        #  main() 부터 실행됨  

# pyenv-win   


# 단계: 우리(파이썬)가 주소를 인코딩해서 '요청'함
# 인터넷 도로는 한글을 실어 나를 수 없습니다. 
# 그래서 urllib.parse.quote('대구')를 써서 
# 한글을 %EB%8C%80%EA%B5%AC라는 인터넷 도로용 문자열로 우리가 먼저 포장(인코딩)합니다. 
# 그리고 이 주소로 네이버 서버에 노크(요청)를 합니다.

# 2단계: 서버가 우리가 보낸 주소를 '인식'함
# 네이버 서버는 우리가 보낸 %EB%8C%80%EA%B5%AC라는 주소를 받아보고, 
# 자기들의 규칙에 따라 "아, 이 사람이 '대구'라는 글자를 찾고 있구나!"하고 
# 주소를 해독(디코딩)해서 정확하게 인식합니다.

# 3단계: 서버가 데이터를 찾아서 우리에게 '전송'함
# 우리가 뭘 원하는지 알아챈 네이버 서버는, 자기네 데이터베이스에서
# '대구'와 관련된 뉴스 데이터를 열심히 찾습니다. 
# 그리고 그 결과물(자료)을 JSON 형식의 텍스트로 뭉쳐서 
# 우리(파이썬)에게 인터넷으로 쏘아 보내줍니다.

# 4단계: 우리(파이썬)가 받아서 해석함
# 마지막으로 내 파이썬 코드가 그 JSON 데이터를 받아서 화면에 출력하거나 파일로 저장하게 됩니다.

# 💡 핵심 교정: 인코딩은 '우리'가 하는 것!
# "우리가 서버에게 내 요청을 인식시키려고 인코딩해서 주소창에 담아 보내는 것!"

# query=: "내가 아까 인코딩한 이 검색어가 들어간 글만 찾아줘." (원하는 데이터 지정)

# start=: "검색 결과 중에서 몇 등(몇 번째) 뉴스부터 보여줄지 정할게." (시작 범위 설정)

# display=: "한 바퀴 돌 때 몇 개씩 묶어서 가져올지 정할게." (가져올 수량 범위 설정)

# {
#   "title": "대구 맛집 소개...",
#   "link": "https://...",
#   "pubDate": "Tue, 26 May 2026 14:30:00 +0900"
# }

