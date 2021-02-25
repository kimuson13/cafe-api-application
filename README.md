# Cafe Application API [![Build Status](https://travis-ci.org/kimuson13/cafe-api-application.svg?branch=master)](https://travis-ci.org/kimuson13/cafe-api-application)
## リンク
[Cafe App API](http://54.64.23.118:8000)
## 概要
Cafe App APIはカフェの情報を管理する機能を備えているAPIです。
## 機能一覧
・ユーザーの新規登録
・ユーザーのトークンの獲得
・ユーザー情報の更新
・カフェのタグの作成
・カフェの情報(名前、住所、開店時間、閉店時間、タグ)の追加
・カフェの情報の更新
## デモ＆使い方
上のリンクに飛ぶと、まずこのページが表示されます。
![demo1](https://user-images.githubusercontent.com/73643164/109083514-6540de00-7749-11eb-8db0-269889e2ede6.png)  
そのため、/api/user/create/とURLに入力します。  
![demo2](https://user-images.githubusercontent.com/73643164/109083695-bcdf4980-7749-11eb-9edc-2eb557bef223.png)
/api/user/create/ではこれが表示されます。まずフォームを満たします。  
![demo3](https://user-images.githubusercontent.com/73643164/109083783-e6987080-7749-11eb-9400-f36f9658a379.png)
そしてPOSTを押します。  
![demo4](https://user-images.githubusercontent.com/73643164/109083905-22cbd100-774a-11eb-9096-4fbe28428666.png)
ここでは、test@test.co,となっており、バリデーションエラーが表示されます。そのため、test@test.comに直し、再度POSTを押します。  
![demo5](https://user-images.githubusercontent.com/73643164/109084293-daf97980-774a-11eb-940c-9f850603595b.png)
そうすると、emailとnameだけが表示され、パスワードは非表示になっています。次に/api/user/token/と入力します。  



