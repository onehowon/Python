from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
import numpy as np

# 해시태그 검색어
keyword = "검색할 단어"
count = "검색할 글의 갯수"

# 로그인 정보
username = '유저 아이디'
userpw = '비밀번호'
time.sleep(3)

# 해시태그 url 값
url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

# dataframe 만들기 (해시태그는 총 20개까지 크롤링)
insta_df = pd.DataFrame("", index=np.arange(1,count+1), columns=["account","date", "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10" , "t11", "t12", "t13", "t14", "t15", "t16", "t17", "t18", "t19", "t20"])
instagram_account =[]
instagram_tags = []
instagram_tag_dates = []

# 인스타 로그인 URL
loginUrl = 'https://www.instagram.com/accounts/login/'

# Chrome drvier 실행
driver = wd.Chrome("chromedriver.exe")
driver.get(loginUrl)
time.sleep(2)

# login
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(userpw)
time.sleep(2)
driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
time.sleep(3)

# 정보 나중에 저장하기 클릭하고 넘어가기
driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()
time.sleep(3)
# 설정 나중에하기 클릭하고 넘어가기
driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
time.sleep(3)

# 해시태그 검색 창에 "키워드" 검색
driver.get(url)
time.sleep(15)

# 맨 왼쪽 상단 첫 게시물 클릭
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
time.sleep(3)

# 데이터 기록, 다음 게시물로 클릭
for i in range(count):
    try: 
        # account 데이터 기록
        account_data = driver.find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV')
        account_text = account_data.text
        
        # 날짜 기록 (주단위)
        date = driver.find_element_by_css_selector("time.FH9sR.Nzb55").text # 날짜 선택
        
        # 날짜 데이터가 시간, 일, 분 단위이면 0주로 변환
        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1:
            date_text = '0주'
        else:
            date_text = date
        # 해쉬태그 데이터 기록
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj')
        tag_raw = data.text
        tag = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tag).replace("#"," ") # "#" 제거
        tag_data = tag.split()
    except:
        tag_data = "error"
        date_text = "error"
        
    try: # 최대 50초까지 기다렸다가, > 모양 클릭하여 다음 게시물로 넘어가기
        WebDriverWait(driver,50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._65Bje.coreSpriteRightPaginationArrow')))
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
    except:
    	print("크롤링이 비정상적으로 종료되었습니다")
        driver.quit()
    
    time.sleep(5)
    print('{}, {}번째 게시물 탐색 완료'.format(time.strftime('%c', time.localtime(time.time())), i+1))
    print(account_text)
    print(date_text)
        
    # dataframe에 계정정보, 날짜 저장
    insta_df.iloc[i, 0] = account_text
    insta_df.iloc[i, 1] = date_text
    
    # 해시태그저장, 20개가 넘으면 20개까지만 저장됨
    for j in range(17):
        try:
            insta_df.iloc[i,j+2] = tag_data[j]
        except :
            break


# 결과값 저장
insta_df.to_excel("저장경로\\"+keyword+"_results.xlsx")

# 크롬드라이버 종료
print('크롤링 종료')
driver.quit()