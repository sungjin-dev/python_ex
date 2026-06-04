import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# SK하이닉스 종목코드
CODE = '000660'
URL = f"https://finance.naver.com/item/main.naver?code={CODE}"

def get_current_price():
    # 봇(Bot)으로 인식되어 차단당하는 것을 방지하기 위해 일반 브라우저인 척하는 User-Agent 추가
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status() # 웹페이지를 정상적으로 불러왔는지 확인
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 네이버 금융 HTML 구조에서 현재가 부분 추출 (<p class="no_today"> 안의 <span class="blind">)
        today_p = soup.find('p', class_='no_today')
        if today_p:
            price = today_p.find('span', class_='blind').text
            return price
        return None
        
    except Exception as e:
        return f"Error: {e}"

def run():
    print("📈 SK하이닉스(000660) 실시간 주가 조회 시작")
    print("종료하려면 터미널에서 'Ctrl + C'를 누르세요.")
    print("-" * 50)
    
    try:
        while True:
            price = get_current_price()
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            if price:
                print(f"[{current_time}] SK하이닉스 현재가: {price}원")
            else:
                print(f"[{current_time}] 가격 정보를 불러올 수 없습니다.")
                
            # 💡 서버 부하 및 IP 차단 방지를 위해 5초 대기
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n프로그램을 안전하게 종료합니다.")

if __name__ == '__main__':
    run()