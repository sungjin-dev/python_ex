from flask import Flask, render_template, request
import urllib.request
import urllib.parse
import datetime
import json

app = Flask(__name__)

client_id = ''
client_secret = ''


# 네이버 API 요청
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] 요청 성공')

        responseData = response.read().decode('utf-8')
        return responseData

    except Exception as e:
        print(e)
        return None


# 네이버 뉴스 검색
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


# 데이터 정리
def getPostData(post, cnt):

    try:
        pDate = datetime.datetime.strptime(
            post['pubDate'],
            '%a, %d %b %Y %H:%M:%S +0900'
        )

        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    except:
        pDate = post['pubDate']

    return {
        'cnt': cnt,
        'title': post['title'],
        'description': post['description'],
        'org_link': post['originallink'],
        'link': post['link'],
        'pDate': pDate
    }


# 메인 페이지
@app.route('/', methods=['GET', 'POST'])
def index():

    jsonResult = []

    if request.method == 'POST':

        srcText = request.form['keyword']

        node = 'news'
        cnt = 0

        jsonResponse = getNaverSearch(node, srcText, 1, 10)

        while jsonResponse is not None and jsonResponse['display'] != 0:

            for post in jsonResponse['items']:

                cnt += 1

                jsonResult.append(
                    getPostData(post, cnt)
                )

            break

    return render_template(
        'index.html',
        results=jsonResult
    )


if __name__ == '__main__':
    app.run(debug=True)