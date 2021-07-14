from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import numpy as np
import pandas as pd

keyword = "검색 단어"
count = "검색 글의 개수"

insta_id = "id" 
insta_pw = "pw"
time.sleep(3)
url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

df = pd.DataFrame("", index=np.arange(1, count+1), columns=["account", "date", "t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12","t13","t14","t15","t16","t17","t18","t19","t20"])
insta_account = []
insta_tags = []
insta_tag_dates = []

loginURL = "https://www.instagram.com/accounts/login"

driver = wd.Chrome("chromedriver.exe")
driver.get(loginURL)
time.sleep(2)

driver.find_elements_by_name('username').send_keys(insta_id)
driver.find_element_by_name('password').send_keys(insta_pw)
time.sleep(2)
driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
time.sleep(3)

driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()
time.sleep(3)
driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
time.sleep(3)

driver.get(url)
time.sleep(15)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
time.sleep(3)

for i in range(count):
    try:
        account_data = driver.find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV')
        account_text = account_data.text

        date = driver.find_element_by_css_selector("time.FH9sR.Nzb55").text

        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1:
            date_text = '0주'
        else:
            date_text = date

        data = driver.find_elements_by_css_selector('.C7I1f.X7jCj')
        tag_raw = data.text
        tag = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tag).replace("#"," ")
        tag_data = tag.split()
    except:
        tag_data = "error"
        date_text = "error"
    try:
        WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a._65Bje.coreSpriteRightPaginationArrow')))
        driver.find_elements_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
    except:
        print("크롤링 비정상 종료")
        driver.quit()

    time.sleep(5)
    print('{}, {}번 째 게시물 탐색 완료'.format(time.strftime('%c', time.localtime(time,time())), i+1))
    print(account_text)
    print(date_text)

    df.iloc[i, 0] = account_text
    df.iloc[i, 1] = date_text

    for j in range(17):
        try:
            df.iloc[i, j+2] = tag_data[j]
        except:
            break
df.to_excel("/Users/seong-wonho/Documents/크롤링 데이터\\" + keyword+"_results.xlsx")

print('크롤링 종료')
driver.quit()
