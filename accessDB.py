import sqlite3
import pandas as pd

#テーブルの作成
def createTable():

    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # テーブルの作成
    cur.execute(
        'CREATE TABLE users(idm STRING PRIMARY KEY, id STRING, password STRING)'
    )

    # データベースにコミット（結果の反映）
    conn.commit()
    conn.close()

#テーブルの削除
def dropTable():

    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # テーブルの作成
    cur.execute(
        'DROP TABLE users'
    )

    # データベースにコミット（結果の反映）
    conn.commit()
    conn.close()

#テーブルの中身を削除
def dropTableContents():

    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # テーブルの作成
    cur.execute(
        'DELETE FROM users WHERE 1'
    )

    # データベースにコミット（結果の反映）
    conn.commit()
    conn.close()

#テーブルへの挿入：idm,id,passwordの組を挿入
def insertTable(idm,id,password):
    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # INSERT文の実行
    executeString = 'INSERT INTO users values("{}","{}","{}")'.format(idm,id,password)

    cur.execute(executeString)
    # データベースにコミット（結果の反映）
    conn.commit()
    # DB切断
    conn.close()

# データの取得
def getData(idm):
    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SELECT文の実行
    executeString = 'SELECT id,password FROM users WHERE idm="{}"'.format(idm)
    # pandasのデータフレームで取得
    df = pd.read_sql(executeString,conn)

    # データベースにコミット（結果の反映）
    conn.commit()
    # DB切断
    conn.close()

    # データフレームを返す
    return df

# IDの更新
def updateId(idm,id):
    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # UPDATE文の実行
    executeString = 'UPDATE users SET id = "{}" WHERE idm = "{}"'.format(id,idm)

    cur.execute(executeString)
    # データベースにコミット（結果の反映）
    conn.commit()
    # DB切断
    conn.close()


# パスワードの更新
def updatePassword(idm,password):
    # ユーザIDとパスワードの登録を行うDB
    dbname = 'main.db'
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # UPDATE文の実行
    executeString = 'UPDATE users SET password = "{}" WHERE idm = "{}"'.format(password,idm)

    cur.execute(executeString)
    # データベースにコミット（結果の反映）
    conn.commit()
    # DB切断
    conn.close()
