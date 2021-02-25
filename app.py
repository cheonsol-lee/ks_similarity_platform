from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

from similarity_measure import similarity_measure

@app.route('/', methods=['GET','POST'])
def index():
    A_keyword = "코로나"
    B_keyword = "바이오"

    A_index = request.form.getlist('A_Check') # 유저가 선택한 코로나 기사들 index
    B_index = request.form.getlist('B_Check') # 유저가 선택한 바이오 기사들 index

    # 유사도 계산 모듈
    A_list, B_list, AB_list, A_avg, B_avg, AB_avg = similarity_measure(A_keyword, A_index, B_keyword, B_index)
    print(A_list)
    print(B_list)
    print(AB_list)
    A_len  = len(A_list)
    B_len  = len(B_list)
    AB_len = len(AB_list)

    return render_template('index.html',
                           enumerate=enumerate,
                           A_list=A_list,
                           B_list=B_list,
                           AB_list=AB_list,
                           A_avg=A_avg,
                           B_avg=B_avg,
                           AB_avg=AB_avg,
                           A_keyword=A_keyword,
                           B_keyword=B_keyword,
                           A_title_list=A_title_list,
                           B_title_list=B_title_list,
                           A_link_list=A_link_list,
                           B_link_list=B_link_list,
                           A_index=A_index,
                           B_index=B_index,
                           A_len=A_len,
                           B_len=B_len,
                           AB_len=AB_len)

# 코로나 기사
A_title_list=[
"정부, 내일 '2∼3월 코로나19 백신 접종계획' 발표(종합2보)",
"정부, ‘2~3월 코로나19 백신 접종계획’ 내일 발표",
"코로나19 백신 누가, 어떤 종류 맞나…\"2∼3월 약 76만명 접종\"",
"1분기 코로나19 예방접종 계획 발표…만 65세 이상은 일단 제외",
"서울시, 코로나 위기 관광업체에 총 15억 현금 지원",
"귀뚜라미보일러 아산공장서 코로나19 42명 집단 감염(종합)",
"영국 정부 \"영국발 변이 코로나19, 치명률도 더 높다\"",
"아동용 코로나 백신 나온다, 미국·영국서 임상시험 시작",
"코로나19 신규 확진자 344명…사흘째 300명대",
"20대 코로나 첫 사망"
]

A_link_list = [
"https://www.yna.co.kr/view/AKR20210214042952530?input=1195m",
"http://news.kbs.co.kr/news/view.do?ncd=5117334&ref=A",
"https://www.yna.co.kr/view/AKR20210215091400530?input=1195m",
"http://news.kbs.co.kr/news/view.do?ncd=5117988&ref=A",
"https://www.fnnews.com/news/202102131445134005",
"https://www.yna.co.kr/view/AKR20210215108751063?input=1195m",
"http://news.kmib.co.kr/article/view.asp?arcid=0015532695&code=61131111&cp=nv",
"https://www.chosun.com/economy/science/2021/02/14/3DLY2MZ7IZDHTNEU2B32K2UW6I/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news",
"http://www.hani.co.kr/arti/society/health/982950.html#csidx0e814340d0810688c38766e088b7407",
"https://www.seoul.co.kr/news/newsView.php?id=20210215003001&wlog_tag3=naver"
]

# 바이오 기사
B_title_list = [
"셀트리온, 유럽서 고농도 휴미라 바이오시밀러 판매 허가",
"셀트리온, 고농도 휴미라 바이오시밀러 유럽 허가…시장 규모 19조원↑",
"셀트리온, ‘세계1위 휴미라’ 바이오시밀러 유럽 판매 시작",
"셀트리온, 자가면역질환 치료제 바이오시밀러 유럽 판매 허가",
"식약처장, AZ 코로나 백신 제조 SK바이오사이언스 방문",
"김강립 식약처장, AZ백신 생산하는 SK바이오사이언스",
"폐섬유증 신약 1호 경쟁…브릿지바이오 '전화위복'",
"헬릭스미스, 美 바이오 CEO&투자자 컨퍼런스 참가",
"SK바이오 상장에 SK케미칼·SK디스커버리도 훈풍",
"테라젠바이오, 국내 최다 78개 세부항목 ‘DTC 유전자검사’ 실시"
]

B_link_list = [
"https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202102150132&t=NN",
"http://www.ceoscoredaily.com/news/article.html?no=78603",
"https://www.sedaily.com/NewsView/22IJHLR2CV",
"https://health.chosun.com/site/data/html_dir/2021/02/15/2021021500770.html",
"https://newsis.com/view/?id=NISX20210215_0001338762&cID=13001&pID=13000",
"https://www.news1.kr/articles/?4211781",
"https://www.hankyung.com/it/article/2021021598031",
"https://www.mk.co.kr/news/it/view/2021/02/147278",
"https://www.fnnews.com/news/202102112028443052",
"http://www.segyebiz.com/newsView/20210215509412?OutUrl=naver"
]

if __name__ == '__main__':
    app.run()
