from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/lotto")
def lotto():
    
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    #url 요청은 request pip install requests 설치
    res = requests.get(url).text #요청할게. 가져올게 url를 .text는 안에있는 정보만 본다
    lotto_dict =json.loads(res)
    print(lotto_dict["drwNoDate"]) #lotto_dict 안에 정보가 많으니 그 안에 괄호안꺼 가져올꺼야 그러면 2018-12-15 뜬다 나머지 6개를 가져올 수 있다
    num1 = lotto_dict["drwtNo1"]
    
    #이번주 당첨번호 for문으로 하는 방법 (아래)
    
    week_num = [] #이걸 선언
    week_format_num =[]
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number) # for문에서 나오는 넘버를 붙여 넣는거
    print(week_num)
    
    for i in range(1,7): #1부터6 사용
       num = lotto_dict['drwtNo{}'.format(i)]   #drwtNo 는 반복 그 뒤 숫자는 어떻게 넣지? 그 방법은 string formating/ week_format_num 선언
       week_format_num.append(num)
    
    # print(type(res))
    # print(type(json.loads(res))) #json 검색해서 이해하기~!
    
    #pick = 우리가 생성한 번호
    #week_num = 이번주 당첨번호
    # 위의 두 값을 비교해서 로또 당첨 등수 출력!
    #1등 : 6개 숫자 다 맞출 떄
    #2등 : 5개
    num_list = range(1,46)
    pick = random.sample(num_list,6) #총 몇개, 몇개를 뽑을지
    count = 0
    
    n = 1 
    
    for i in range (6):
        for j in range(6):
            if pick[j] == week_num[i]:
               count = count+1
            
    if count == 6:
      print("1등입니다.")
    elif count == 5:
        print("2등입니다.")
    elif count == 4:
        print("3등입니다.")
    elif count == 3:
        print("4등입니다.")
    else :
        print("꽝입니다.")
        
        
@app. route('/lottery')        
def lottery():
    #로또 정보를 가져옴.
    
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text 
    lotto_dict =json.loads(res)
    
    
    #1등 당첨 버호를 week 리스트에 넣는다.
    week =[]
    for i in range(1,7): #1부터6 사용
       num = lotto_dict['drwtNo{}'.format(i)]   #drwtNo 는 반복 그 뒤 숫자는 어떻게 넣지? 그 방법은 string formating/ week_format_num 선언
       week.append(num)
    
    #보너스 번호를 bonus 변수 넣기
    bonus = lotto_dict["bnusNo"]
    
    #임의의 로또 번호를 생성.
    pick = random.sample(range(1,46),6)
    
    #비교해서 몇등인지 저장.
    
    # match =len(set(pict)&set(week))
    # if match==6:
    #     text = "1등"
    # elif match==5:
    #     if bonus in pick:
    #         text ="2등"
    #     else:
    #             text = "3등"
    # elif match==4:
    #     text = "4등"
    # else:
    #     text='꽝'
    
    #사용자에게 데이터를 넘겨줌.
      
    # return render_template("lottery.html",pick=pick, week=week,text=text)
    
    
    #return render_template("lotto.html", lotto=pick, week_num=week_num, week_format_num=week_format_num) #로또 html에서는 
    

@app.route('/ping')
def ping():
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()
    return render_template("pong.html", html_name=input_name,fake_job=fake_job)