import urllib.request
import datetime
import json

SERVICE_KEY = '6effc53164df2cd13311dd61418570efadddf2377ac130928289579038a2e041'

def getRequestURL(url):
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION SUCCESS!!')   # 통신이 된 것과 데이터를 송신하는 것은 다름
            return res.read().decode('utf-8') 

    except Exception as e:
        print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION FAIL!!')
        print(f'e: {e}')
        return None

def getTourlismStatesItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?"
    parameters += "_type=json&"    # 공백x 주의
    parameters += "NAT_CD=" + nat_cd + '&'
    parameters += "serviceKey=" + SERVICE_KEY + '&'
    parameters += "YM=" + yyyymm + '&'
    parameters += "ED_CD=" + ed_cd 

    url = serviceURL + parameters
    res = getRequestURL(url)      # None or not None
    if res == None:
        return None
    else:
        return json.loads(res) 
        # json.loads()  JSON형식의 문자열(str)을 파이썬 애플리케이션에서 쉽게 사용할 수 있도록 변환함.
        # JSON 형식의 문자열(str) ------> dic 객체 

def getTourlismStatesService(nat_cd, ed_cd, nStartYear, nEndYear):
    
    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEND = f'{str(nEndYear)}{str(12)}'      # 202012

    # 2025 ~ 2026 : 1~12 , 1~5   
    for year in range(nStartYear, nEndYear + 1):     # 년
        for month in range(1, 13):                 # 월         
            if isDataEnd == 1:                
               break                       
                                        # > : 오른쪽 정렬 , 왼쪽에 0은 채워넣을 값      
            yyyymm = f'{str(year)}{str(month):0>2}'               # 2020 ~ 2021 : 202003(o)  20203 (x)
            jsonData = getTourlismStatesItem(yyyymm, nat_cd, ed_cd)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                # 데이터 끝 확인     
                if jsonData['response']['body']['items'] == '':          # 빈값을 지정할 때 '' (ex, session.loginedmember) 
                    isDataEnd = 1  # 데이터 끝 확인용 flag 변수 
                    dataEND = f'{str(year)}{str(month-1):0>2}'
                    print('DATA END!!')
                    break     
                # json data 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')    # 중 국 - > 중국
                num = jsonData['response']['body']['items']['item']['num']  # 481681
                ed = jsonData['response']['body']['items']['item']['ed']    # 방한외래관광객

                jsonResult.append({
                    'natName':natName,
                    'nat_cd':nat_cd,
                    'yyyymm':yyyymm,
                    'visit_cnt':num
                })
# for 끝나고                
    return (jsonResult, natName, ed, dataEND)                             

def main():

    jsonResult = []
    natName = ''

    print('-----------------------------------------------------')
    print('---------- 국내 입국한 외국인 통계 데이터 -----------')
    print('-----------------------------------------------------')

    nat_cd = input('국가 코드 입력[중국(112), 일본(130), 미국(275)]:')  # client -> server  float integer all str (112, True, 3.14, 7) 
    nStartYear = int(input('데이터 수집 시작 년도: '))   # for문으로 작업해야하기 때문에 int casting이 효율적
    nEndYear = int(input('데이터 수집 끝 년도: '))       # 변수명은 client를 기준으로 맞추는게 좋다
    ed_cd = 'E' # E: 입국  D: 출국

    jsonResult, natName, ed, dataEND = getTourlismStatesService(nat_cd, ed_cd, nStartYear, nEndYear)
    
    if natName == '':
        print('데이터 수집 오류!! 서버 담당자한테 문의 하세요.!!')
    else:
        print('데이터 수집 성공!!')
        with open(f'./{natName}_{ed}_{nStartYear}_{dataEND}.json', 'w', encoding= 'utf-8') as f:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(jsonFile)

if __name__ == '__main__':
    main()
