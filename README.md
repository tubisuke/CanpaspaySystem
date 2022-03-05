# 静岡大学生協サイト便利システム
キャンパスペイの残高や購入品に関する情報を確認できる[生協マイページ](https://mp.seikyou.jp/mypage/Static.init.do)をより便利にしたシステムです．
ログインにFelicaカード（学生証やナイスパス）を用いることにより，パスワードやIDの入力を省略することができ，利便性が増しています．
javascriptを用いて視覚的に残高を確認できる機能や，1年間の購入品ランキングを確認できる機能が搭載されています．

<div align="center">
<img width="568" alt="システムイメージ" src="https://user-images.githubusercontent.com/74696928/156884103-8a6ee407-6c1a-4c34-90ba-ef8d4d11570c.png">
</div>

## できること
- 生協サイトアカウントに対応するfelicaカードの登録
- felicaカードでのログイン
- 残高表示
- 1年間の購入品ランキングの表示

## できないこと
- もっとみるボタンへの対応
- 読み込み画面の実装

## 実行環境
```Ubuntu 20.04.2 LTS```<br>
```python 3.9.7```<br>
```非接触ICカードリーダー／ライター PaSoRi RC-S380```
 
 ## 実行方法
 必要なライブラリ（nfcpyやeelなど）を諸々インストールしてもらって，下記のコマンドを実行するとシステムが動作します．<br>
   ※seleniumの実行に，chromeが必要になります．
 ```
 python3 app.py
 ```
 
 ## 動作イメージ
以下のようにして，カードの登録を行います．

https://user-images.githubusercontent.com/74696928/156884469-636966bc-022b-4f4f-b3d0-e429bd471b90.mp4

## 動作画面
### 1.読み取り画面
読み込みボタンを押すことで，pythonのfelicaカード読み取りプログラム(readFelica.py)が呼び出され，読み取りが行われます．

<img src="https://user-images.githubusercontent.com/74696928/156883523-ca6f8bee-1711-4de6-8cec-60888e4d9029.png" width="50%">

### 2.新規登録画面
データベースに登録されていないユーザがカードを読み込んだ場合に，新規登録画面に遷移し，idm(カード識別番号)に対応したユーザIDとパスワードを入力します．

<img src="https://user-images.githubusercontent.com/74696928/156883578-f11adac9-4924-4293-be79-9d47cce41067.png" width="50%">

### 3.モード選択画
残高表示とランキング表示の2つの機能の選択を行います．

<img src="https://user-images.githubusercontent.com/74696928/156883604-e7e26ad8-2fa6-4bf5-b80e-97cbaaa56137.png" width="50%">

### 4.残高表示画面
javascriptを用いて視覚的に残高を表示します．

<img src="https://user-images.githubusercontent.com/74696928/156883616-c1231ab2-0c1c-4872-b542-351381aa8825.png" width="50%">

### 5.購入品ランキング画面
1年間の購入品の中で，購入回数が多い上位3品を表示します．

<img src="https://user-images.githubusercontent.com/74696928/156883628-bc4a31cd-c4b3-47a4-9bd3-312ec713d186.png" width="50%">
