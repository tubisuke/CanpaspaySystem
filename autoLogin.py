import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import parse
import collections


#selectモジュールのインポート
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException


#
def getMailAddress(inputId,inputPassword):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  #WEBブラウザの起動
    driver.set_window_size('1920', '1080')
    # 画面遷移
    driver.get('https://mp.seikyou.jp/mypage/Static.init.do')

    # 待機
    time.sleep(0.5)

    # ログインIDの入力
    id = driver.find_element_by_name('loginId')
    id.send_keys(inputId)

    # パスワードの入力
    password=driver.find_element_by_name('password')
    password.send_keys(inputPassword)

    # 送信
    id.submit()

    # 3点ボタン
    element = driver.find_element_by_css_selector('#main_menu')
    element.click()

    # 「登録情報の確認・変更」
    element = driver.find_element_by_css_selector('body > div.slidemenu.slidemenu-right.menu-open > div > ul > li:nth-child(10) > a')
    element.click()

    element = driver.find_element_by_css_selector('div.item:nth-child(1) > p:nth-child(2)')
    mailAddress = element.text

    driver.close()

    return mailAddress

# 残高の取得
def getBalance(inputId,inputPassword):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  #WEBブラウザの起動
    driver.set_window_size('1920', '1080')
    # 画面遷移
    driver.get('https://mp.seikyou.jp/mypage/Static.init.do')

    # 待機
    time.sleep(0.5)

    # ログインIDの入力
    id = driver.find_element_by_name('loginId')
    id.send_keys(inputId)

    # パスワードの入力
    password=driver.find_element_by_name('password')
    password.send_keys(inputPassword)

    # 送信
    id.submit()

    # 残高の取得
    selector = '#prepaid > div > dl:nth-child(1) > dd'
    element = driver.find_element_by_css_selector(selector)
    # print('要素：'+element.is_displayed())

    balance = element.text

    driver.close()

    return balance

# すべての使用履歴の取得
def getAllUsageHistory(inputId,inputPassword):
    # 購入した商品のリスト
    productLists = []
    productNum = 0

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)  #WEBブラウザの起動
    driver.set_window_size('1920', '1080')

    # 画面遷移
    driver.get('https://mp.seikyou.jp/mypage/Static.init.do')

    time.sleep(0.5)

    # ログインIDの入力
    id = driver.find_element_by_name('loginId')
    id.send_keys(inputId)

    # パスワードの入力
    password=driver.find_element_by_name('password')
    password.send_keys(inputPassword)

    # 送信
    id.submit()

    # プリペイド利用履歴画面への遷移
    selector = '#prepaid > div > div > a'
    element = driver.find_element_by_css_selector(selector)
    element.click()

    for idx in range(13):
        dropdown = driver.find_element_by_name('rirekiDate') #"rirekiDate"という名前のプルダウンを取得
        select = Select(dropdown) # セレクトオブジェクトを取得
        select.select_by_index(idx) # インデックス指定で選択
        contents = driver.find_elements_by_class_name('box_in')
        for content in contents:

            productString = content.find_element_by_css_selector("li").text

            # '/'で商品を区切る
            splitString = productString.split('/');
            for item in splitString:
                productLists.append(item)

    driver.close()

    # 上位３件
    mycounter = collections.Counter(productLists)
    return mycounter.most_common(3)

# 使用履歴の取得
def getUsageHistory(inputId,inputPassword,index):
    driver = webdriver.Chrome()  #WEBブラウザの起動

    # 画面遷移
    driver.get('https://mp.seikyou.jp/mypage/Static.init.do')

    #time.sleep(1)

    # ログインIDの入力
    id = driver.find_element_by_name('loginId')
    id.send_keys(inputId)

    # パスワードの入力
    password=driver.find_element_by_name('password')
    password.send_keys(inputPassword)

    # 送信
    id.submit()

    # プリペイド利用履歴画面への遷移
    selector = '#prepaid > div > div > a'
    element = driver.find_element_by_css_selector(selector)
    element.click()

    dropdown = driver.find_element_by_name('rirekiDate') #"rirekiDate"という名前のプルダウンを取得
    select = Select(dropdown) # セレクトオブジェクトを取得

    select.select_by_index(index) # インデックス指定で選択

    # 「もっと見る」ボタンを押し続ける
    # selector = '#details > span > a'
    # element = driver.find_elements_by_css_selector(selector)
    # element[0].click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_xpath('//*[@id="details"]/span/a/img').click()

    # 購入した商品のリスト
    productLists = []
    productNum = 0

    contents = driver.find_elements_by_class_name('box_in')
    for content in contents:
        #
        # dateString = content.find_element_by_css_selector("dl > dt").text
        # month,day,weekday = parse.parse("{:d}/{:d}({})",dateString)

        #print(date)
        productString = content.find_element_by_css_selector("li").text
        # '/'で商品を区切る

        #print(productString.split('/'))

        splitString = productString.split('/');
        for item in splitString:
            productLists.append(item)

    driver.close()

    return productLists
