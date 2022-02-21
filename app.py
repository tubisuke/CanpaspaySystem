# eelのインポート
import eel

import nfc
import pandas as pd

import readFelica
import accessDB
import autoLogin
import sendMail

#このファイル全体で使用するキャンパスペイの情報
canpaspay = readFelica.MyCanpasPay()

#新規登録画面：1
#残高表示画面：2
@eel.expose
def getNextPageFromJavascript():
    #ここで処理を記述
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': canpaspay.onConnect})
    clf.close()

    idm = canpaspay.getIdm()
    df = accessDB.getData(idm)

    print(idm)
    # idmがテーブルに登録されていない
    if(df.empty):
        eel.signUpFromPython()

    else:
        print('すでに登録されています')
        id = df[['id'][0]]
        password = df[['password'][0]]
        canpaspay.setId(id)
        canpaspay.setPassword(password)

        print(id)
        print(password)

        # 残高の取得
        balance = autoLogin.getBalance(id,password)
        # 円という文字を消す
        balance = balance.replace('円', '')
        print(balance)

        #ランキングの取得
        ranking = autoLogin.getAllUsageHistory(id,password)

        # メールアドレスの取得
        mailAddress = autoLogin.getMailAddress(id,password)
        sendMail.sendMail(mailAddress)

        print(ranking)

        canpaspay.setBalance(balance)
        canpaspay.setRanking(ranking)

        eel.mainPageFromPython()

@eel.expose
def signUpFromJavascript(id,password):

    print('新規登録')
    print(id)
    idm = canpaspay.getIdm()

    canpaspay.setId(id)
    canpaspay.setPassword(password)

    print(id)
    print(password)

    # 残高の取得
    balance = autoLogin.getBalance(id,password)
    # 円という文字を消す
    balance = balance.replace('円', '')
    print(balance)

    #ランキングの取得
    ranking = autoLogin.getAllUsageHistory(id,password)
    print(ranking)

    canpaspay.setBalance(balance)
    canpaspay.setRanking(ranking)

    accessDB.insertTable(idm,id,password)
    eel.mainPageFromPython()

@eel.expose
# 残高の取得
def getBalanceFromJavascript():
    print('残高の取得')
    return canpaspay.getBalance()


#ランキングの取得
@eel.expose
# 残高の取得
def getRankingFromJavascript():
    print('ランキングの取得')
    ranking = canpaspay.getRanking()

    return ranking

# ウエブコンテンツを持つフォルダー
eel.init("web")

# 最初に表示するhtmlページ
eel.start("html/index.html",size = (1080,1080))
