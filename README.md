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
![demo6](https://user-images.githubusercontent.com/73643164/109084596-68d56480-774b-11eb-8131-9a416043157c.png)
このような画面が表示されます。ここでは、authenticationに必要なtokenを獲得できます。tokenの獲得にはemailとpasswordが必要です。  
![demo7](https://user-images.githubusercontent.com/73643164/109084918-0466d500-774c-11eb-847f-9a9050a98bcc.png)
なので、emailとpasswordを入力し、POSTを押します。  
![demo8](https://user-images.githubusercontent.com/73643164/109085087-56a7f600-774c-11eb-87fa-a6f11cb61f8d.png)
これでtokenが表示されます。  
![demo9](https://user-images.githubusercontent.com/73643164/109085128-6f181080-774c-11eb-93e6-e4844db7d472.png)
これをModHeaderでAuthorizationにToken "your token"を入力します。これでauthenticationを満たせます。次に、/api/user/me/に飛びます。  
![demo10](https://user-images.githubusercontent.com/73643164/109085381-e0f05a00-774c-11eb-967d-34a2a96ad5ab.png)
ここではユーザー情報の更新をすることができます。  





