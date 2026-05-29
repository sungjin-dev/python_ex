
import urllib.request     # 웹에 있는 데이터나 페이지를 요청(Request)하고 가져오는(Response) 기능을 가진 내장 모듈
import urllib.parse       # URL 인코딩(URL Encoding) 해주는 함수  공백 " " → %20  한글 같은 특수 문자 → UTF-8 기반 %XX 형태로 변환/ 는 기본적으로 인코딩되지 않음
import datetime
import json

client_id = 'id'
client_secret = 'pw'

#Naver에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)                # Request 클래스로 틀(객체)을 먼저 만든다.
    req.add_header('X-Naver-Client-Id', client_id)   # 내 로그인 정보를 넣는 과정
    req.add_header('X-Naver-Client-Secret', client_secret)
                          
    try:                                        
        response = urllib.request.urlopen(req)  # 조립이 완료된 완성형 req 객체를 urlopen에 던진다.
        if response.getcode() == 200: 
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            #  decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것. 인코딩의 반대
        raw_data = response.read()    # response.read()는 서버가 준 데이터를 딱 한 번만 읽을 수 있는 스트림(Stream) 방식 변수에 담아서 활용
        responseData = raw_data.decode('utf-8')

        return responseData
    
    except Exception as e:    # 모든 에러들의 "조상님(최상위 클래스)" # 발생한 에러 객체를 e라는 이름의 변수에 담기(출력용)
        print(f'[{datetime.datetime.now()}] Error: {e}')  # from datetime import datetime as Dt    
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

    if responseDecode is None:   # 응답이 없는 경우를 말하는거겠지?
        return None
    else:
        return json.loads(responseDecode)     # json 형태로 바꿔주는 모듈(딕셔너리 or 리스트)
       
                                              # '데이터 정제(Data Cleaning/Parsing)' 또는 '필터링
def getPostData(post, jsonResult, cnt):       # 알맹이만 추출: 기사 제목(title), 설명(description), 원래 링크(originallink), 네이버 링크(link), 발행일(pubDate)만 
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    try:      # 가전제품_매장.세탁기.빨래하기()
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')   # pubDate 네이버서버가 지정한 딕셔너리 key값임
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')     #  time 모듈 안 써도 된다. 
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




