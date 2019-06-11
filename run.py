#Windows + R 키 누르고 cmd 입력하여 명령 프롬프트를 실행한 뒤
#pip를 통해 아래와 같이 명령줄을 입력하여 필요 모듈들을 설치합니다:
#pip install wordcloud matplotlib bs4 requests lxml

from wordcloud import WordCloud
import requests, lxml, webbrowser
from bs4 import BeautifulSoup

#네이버 접속 위해 User Agent 설정
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

#네이버 뉴스 웹 요청
r = requests.get('https://news.naver.com/', headers=headers).text

#BeautifulSoup 모듈로 Bold 처리된 문자열(헤드라인) 모두 블러오기
bs = BeautifulSoup(r, 'lxml')
bs2 = bs.find_all('strong')

#뉴스 헤드라인 데이터 담기
f = open('data.txt', 'w')
count = 0
for s in bs2:
    count += 1
    #필요없는 값 걸러내기
    if count > 2 and count < 33 and s.text!='동영상 기사': f.write(s.text + '\n')
f.close()

#출력할 html 페이지 설정
html = '''
<html>
<head>
<font face="맑은 고딕">
<title>워드클라우드 출력 결과</title>
</head>
<body>
<center>
<br><h1>네이버 뉴스 헤드라인 워드클라우드</h1><br>
<img src="output.png">
</body>
</html>
'''

#한글 폰트 불러오기
fontpath = 'C:/Windows/Fonts/malgun.ttf'

#워드클라우드 설정후 생성 & 출력
wc = WordCloud(font_path=fontpath, background_color='white', width=1280, height=720).generate(open('data.txt').read())
wc.to_file('output.png')

#마지막으로 html 페이지를 만들고 열기
f = open('page.html', 'w')
f.write(html)
f.close()

webbrowser.open('page.html')

