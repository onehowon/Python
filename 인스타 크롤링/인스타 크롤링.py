import requests
from bs4 import BeautifulSoup
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as time
import getpass
import urllib.request
import random
 
 
from time import sleep
 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

driver = webdriver.Chrome(executable_path="/Users/seong-wonho/Documents/크롤링 데이터/chromedriver")
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

username = getpass.getpass("Input ID : ")
password = getpass.getpass("Input PWD : ")
hashTag = input("Input HashTag # : ")

element_id = driver.find_element_by_name("username")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password)

sleep(1.5)

driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()
sleep(3.5)

##나중에버튼 클릭
driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF').click()

##알림 설정 클릭
driver.find_element_by_css_selector('.aOOlW.HoLwm').click()

sleep(4)

##데이터를 저장할 Dictionary
insta_dict = {'id':[],
              'date': [],
              'like': [],
              'text': [],
              'hashtag':[]}
 
baseUrl = 'https://www.instagram.com/explore/tags/'
url = baseUrl + urllib.parse.quote_plus(hashTag)
driver.get(url)

## 첫 번째 게시물 클릭 
first_post = driver.find_element_by_class_name('_9AhH0')
first_post.click()


seq = 0
start = time.time()
 
while True:
    try:
        if driver.find_element_by_css_selector('div._9AhH0'):
            if seq % 20 == 0:
                print('{}번째 수집 중'.format(seq), time.time() - start, sep = '\t')
 
 
 
            ## id 정보 수집
            try:
                info_id = driver.find_element_by_css_selector('h2._6lAjh').text
                insta_dict['id'].append(info_id)
            except:
                info_id = driver.find_element_by_css_selector('div.C4VMK').text.split()[0]
                insta_dict['id'].append(info_id)
 
 
            ## 시간정보 수집 
            time_raw = driver.find_element_by_css_selector('time.FH9sR.Nzb55')
            time_info = pd.to_datetime(time_raw.get_attribute('datetime')).normalize()
            insta_dict['date'].append(time_info)
 
            ## like 정보 수집
            try:
                driver.find_element_by_css_selector('button.sqdOP.yWX7d._8A5w5')
                like = driver.find_element_by_css_selector('button.sqdOP.yWX7d._8A5w5').text
                insta_dict['like'].append(like)
 
            except:
                insta_dict['like'].append('영상')
 
 
 
            ##text 정보수집
            raw_info = driver.find_element_by_css_selector('div.C4VMK').text.split()
            text = []
            for i in range(len(raw_info)):
                ## 첫번째 text는 아이디니까 제외 
                if i == 0:
                    pass
                ## 두번째부터 시작 
                else:
                    if '#' in raw_info[i]:
                        pass
                    else:
                        text.append(raw_info[i])
            clean_text = ' '.join(text)
            insta_dict['text'].append(clean_text)
 
            ##hashtag 수집
            raw_tags = driver.find_elements_by_css_selector('a.xil3i')
            hash_tag = []
            for i in range(len(raw_tags)):
                if raw_tags[i].text == '':
                    pass
                else:
                    hash_tag.append(raw_tags[i].text)
 
            insta_dict['hashtag'].append(hash_tag)
 
            seq += 1
 
            if seq == 100:
                break
 
            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
            time.sleep(1.5)
            
 
        else:
            break
            
    except:
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        time.sleep(2)

        test = pd.DataFrame.from_dict(insta_dict)