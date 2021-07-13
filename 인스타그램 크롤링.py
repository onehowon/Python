from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import json
import pandas as pd

insta_id = "01065778166", insta_pw = "fpdltm20010221!"
login_option = "instagram" # instagram
driver_path = "~/chromedriver"
instagram_id_name = "one_ho_won"
instagram_login_btn = ""

print(f"login start - option {login_option}")

login_url = "https://www.instagram.com/accounts/login/"
driver.get(login_url)
time.sleep(10)

if login_option == "instagram":
    try:
        instagram_id_form = driver.find_element_by_name(instagram_id_name)
        instagram_id_form.send_keys(user_id)
        time.sleep(5)

        instagram_pw_form = driver.find_element_by_name(instagram_pw_name)
        instagram_pw_form.send_keys(user_passwd)
        time.sleep(7)

        login_ok_button = driver.find_element_by_css_selector(instagram_login_btn)
        login_ok_button.click()
        is_login_success = True
    except:
        print("instagram login failed")
        is_login_success = False
