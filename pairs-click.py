## https://review-of-my-life.blogspot.com/2017/11/selenium-facebook-login.html
## https://tanuhack.com/python/selenium/
## メソッド一覧記事　https://qiita.com/mochio/items/dc9935ee607895420186#%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%82%92%E6%9B%B4%E6%96%B0%E3%81%99%E3%82%8B
import os
from selenium import webdriver
import pandas
import time

driver = webdriver.Chrome(executable_path="/Users/hikaru.s/Desktop/myvenv/bin/chromedriver")

## 自分のアカウントの情報を入れる。
email = ""
password = ""


def facebookLogin(email, password):

    #1-1 最初にPairsのFacebook認証を済ませる

    driver.get("https://www.pairs.lv/")
    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[2]/header/div/nav/ul/li[6]/a').click()
    time.sleep(6)

    # ウィンドウハンドルを取得する
    handle_array = driver.window_handles
    # ウィンドウを切り替える
    driver.switch_to.window(handle_array[-1])
    # メールとパスワードを入力する
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    time.sleep(4)
    # 送信ボタン
    driver.find_element_by_xpath('//*[@id="email_container"]/div/label').click()
    #1-3 どこでもいいので、クリック
    driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
    ## pairログイン完了
    ## 広告削除
    time.sleep(15)
    handle_array = driver.window_handles
    driver.switch_to.window(handle_array[-1])
    driver.find_element_by_xpath('//*[@id="welcome_close_button"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[49]/div[2]/div/a').click()
    time.sleep(5)
    ##いいね1回目
    driver.find_element_by_xpath('//*[@id="pairs_search_page"]/div/div[5]/ul/li[1]/div[2]/div[3]/div/span[1]/a').click()
    ##いいねモーダルクリック
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="like_modal_area"]/div/div[3]/a').click()
    ##いいね2回目
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="pairs_search_page"]/div/div[5]/ul/li[2]/div[2]/div[3]/div/span[1]/a').click()
    ##いいねモーダルクリック
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="like_modal_area"]/div/div[3]/a').click()
    ##いいね3回目

if __name__ == '__main__':
    facebookLogin(email, password)
