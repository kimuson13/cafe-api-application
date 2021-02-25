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
![demo11](https://user-images.githubusercontent.com/73643164/109103796-c202bf80-776e-11eb-9b05-0ccebcbbdf15.png)
authenticationを満たしていないとこのようなページが表示されます。  
![demo12](https://user-images.githubusercontent.com/73643164/109104327-20c83900-776f-11eb-9786-a8d00f266b73.png)
今回はユーザーのpasswordとnameを変更し、PUTを押します。  
![demo13](https://user-images.githubusercontent.com/73643164/109104409-41908e80-776f-11eb-8ffb-6fa0bfd02ead.png)
するとユーザー情報を更新することができました。ここでもpasswordは非表示になっています。ここからはCafeのAPIのページを見ていきます。そのため、/api/cafe/にアクセスします。  
![demo14](https://user-images.githubusercontent.com/73643164/109104574-90d6bf00-776f-11eb-836c-a0503b99906f.png)
このようなページが表示されます。ここからは、cafeのAPIには"tags"と"cafes"というページがあることが分かります。次は/api/cafe/tags/にアクセスします。  
![demo15](https://user-images.githubusercontent.com/73643164/109104671-bcf24000-776f-11eb-825f-1e9143a43cdc.png)
タグを作成するページに飛びます。タグはタグの名前を入力することができます。  
![demo16](https://user-images.githubusercontent.com/73643164/109105066-89fc7c00-7770-11eb-8afe-6703ba3d3062.png)
ここでは"tag1"と入力し、POSTを押します。  
![demo17](https://user-images.githubusercontent.com/73643164/109105163-b0221c00-7770-11eb-8c82-3fd3dbf29447.png)
すると、tag_id,nameの値が表示されます。タグページの基本的な内容は以上です。次に/api/cafe/cafes/にアクセスします。  
![demo18](https://user-images.githubusercontent.com/73643164/109105321-098a4b00-7771-11eb-88cb-f087f1739732.png)
このページではカフェの情報を入力する必要があります。タグは指定しなくてもPOSTすることができます。他の情報は必須項目です。  
![demo19](https://user-images.githubusercontent.com/73643164/109105625-a816ac00-7771-11eb-8dd3-a0c1baa2fa85.png)
今回は"test cafe2"という名前の架空のカフェの情報を入力しました。入力し終えたらPOSTを押します。  
![demo20](https://user-images.githubusercontent.com/73643164/109105716-d5fbf080-7771-11eb-9bcd-355b8b20d37e.png)
入力した情報に問題がなければこのように表示されます。次にカフェの情報の編集、確認をするために/api/cafe/cafes/{id}にアクセスします。今回のidは2です。
![demo21](https://user-images.githubusercontent.com/73643164/109105918-25dab780-7772-11eb-8ac9-5a2eb4f514d5.png)
このようなページが表示されます。ここでは、編集のほかに削除をすることもできます。まずは編集から行っていきます。  
![demo22](https://user-images.githubusercontent.com/73643164/109106023-56225600-7772-11eb-8d0d-43bf4c92564f.png)
ここでは、タグの情報だけ変更てみます。タグは複数つけることも可能です。そのため複数つけてみました。入力が終わったのでPUTを押します。  
![demo23](https://user-images.githubusercontent.com/73643164/109106115-8669f480-7772-11eb-9c0e-06fec07063f4.png)
すると、tagの表示が変わりました。tagを複数登録すると、tagのidだけが表示され、nameは省略されます。次に削除をしてみます。削除はDELETEという赤いボタンを押すことでできます。  
![demo24](https://user-images.githubusercontent.com/73643164/109106412-10b25880-7773-11eb-8837-2d3c9d514aa7.png)
試しに押してみると、このような警告がでます。特に問題なければもう一度DELETEを押します。  
![demo25](https://user-images.githubusercontent.com/73643164/109106501-38092580-7773-11eb-839c-14c5f51ff946.png)
これによりHTTP response
