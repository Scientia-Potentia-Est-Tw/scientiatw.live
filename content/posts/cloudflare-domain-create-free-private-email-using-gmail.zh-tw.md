---
title: "利用Cloudflare Domain搭配Gmail建立私人電子信箱"
date: 2025-12-26T15:59:00+08:00
lastmod: 2026-01-03T11:22:00+08:00
author: "黃宏勝"
categories:
  - 科技
tags:
  - 客製化電子信箱
  - Cloudflare
  - Gmail
  - 個人網域
  - Email Routing
keywords: 
  - 科技
  - 客製化電子信箱
  - Cloudflare
  - Gmail
  - 個人網域
  - Email Routing
summary: "個人化電子郵件信箱讓你看起來更專業，本文向各位介紹如何利用Cloudflare購買的網域搭配免費的Gmail來建立私人信箱"
featureimage: "https://secologies.com/wp-content/uploads/2025/12/cloudflare-domain-create-free-private-email-using-gmail.webp"
thumbnail: "https://secologies.com/wp-content/uploads/2025/12/cloudflare-domain-create-free-private-email-using-gmail.webp"
slug: "cloudflare-domain-create-free-private-email-using-gmail"
---
你是否擁有了自己的網域後，也想要一個網域的信箱？

擁有客製化的電子郵件信箱，會讓你看起來更專業，要完成這點，其實不需要額外購買存放SMTP伺服器的網路空間，只需要有免費版的Google Gmail的信箱帳號就能達成，本文將會帶各位一步一步的完成設定

由於我的網域是在Cloudflare購買的，也比較推薦讀者在該平台租用，原因可以參考Alex Hsu的《如何為網站選一個好域名》[1]以及JN的《想架部落格，需要註冊自己的網域嗎？》[2]等文章，整個流程需要設定兩個主要的部分，首先是Cloudflare端的設定

## Cloudflare Email Routing
在擁有自己的網域後，讀者可以點進去該網域內，我們可以在左側欄位找到所有功能，其中看到Email功能後下拉，會出現Email Routing可以點選

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-Email-Routing-Page.webp" alt="Cloudflare-Email-Routing-Page" width="800">
  <figcaption>Cloudflare Email Routing頁面</figcaption>
</figure>

進到頁面後，就可以做初始設定，按下Get started

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-email-routing-getstart-scaled.webp" alt="Cloudflare-Email-Routing-Get-started" width="800">
  <figcaption>Cloudflare Email Routing初始設定</figcaption>
</figure>

初始設定如果是在Cloudflare購買網域的話，除了custom address可以設定自己想要的信箱名字，@example.com地方可以下拉選擇自己的網域，而我們目前需要的操作是轉寄信件，所以預設的Send to不用動，欲轉寄的位址填寫想要用來收信的Gmail地址，確認之後按下Create and continue

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-email-routing-custom-setting.webp" alt="Cloudflare-email-routing-custom-setting.webp" width="800">
  <figcaption>Cloudflare Email Routing設定電子郵件位址</figcaption>
</figure>

Cloudflare就會寄送一封確認信到你想要轉寄的信箱裡，直接點選驗證即可

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-routing-verify-mail.webp" alt="Cloudflare-Email-Routing-Verify" width="600">
  <figcaption>Cloudflare Email Routing信箱驗證</figcaption>
</figure>

回到Cloudflare Email Routing頁面裡，就可以在Overview看到已新增的個人紀錄，以及在Routing rules可以看到之前的設定

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-email-routing-overview-scaled.webp" alt="Cloudflare-Email-Routing-Overview" width="800">
  <figcaption>Cloudflare Email Routing總覽</figcaption>
</figure>

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Cloudflare-email-routing-rule-scaled.webp" alt="Cloudflare-Email-Routing-rules" width="800">
  <figcaption>Cloudflare Email Routing規則</figcaption>
</figure>

另外設定完信箱之後，還需要新增DNS紀錄指定給這個網域，會出現在Overview頁面的底下，指示需要啟動下列的紀錄，基本上按下Add records and enable的就行了，不用一個一個自己新增

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/cloudflare-email-routing-required-records.webp" alt="Cloudflare-Email-Routing-required-records" width="800">
  <figcaption>Cloudflare Email Routing所需的DNS Records</figcaption>
</figure>

到這裡Cloudflare Email Routing部分就設定完了，但因為Cloudflare只能夠用來轉寄信件，而如果我們收到電子信件後想要用同樣的地址回覆，中間必須有一個SMTP Server進行轉譯客製化信箱地址，如果讀者使用的是Gmail作為收信地址，則可以利用Google建立SMTP Server，以下說明一下設定流程

## Gmail SMTP Server
> 首先第一點請先確認你的Gmail帳號有啟動2FA功能，這是必要的

再來我們得建立一組Gooel APP Password專門給Gmail SMTP伺服器使用，主要用來給設定新增其他電子郵件時，根據自己想要收信的帳號，請用建立一組APP密碼進入：[https://security.google.com/settings/security/apppasswords](https://security.google.com/settings/security/apppasswords)

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/Create-App-Password.webp" alt="create-app-password" width="600">
  <figcaption>建立App Password</figcaption>
</figure>

按下建立之後，就會給一組密碼，請記錄下來，並且把密碼之間的**空格**刪掉，之後在新增信箱時會需要用到，回到Gmail介面當中，按下右上角的齒輪，找到所有設定，並且到"帳號及匯入"的功能裡，按下新增其他電子郵件信箱

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/gmail-see-all-settings.webp" alt="gmail-see-all-settings" width="400">
  <figcaption>Gmail設定</figcaption>
</figure>

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/add-another-email-address-3-scaled.webp" alt="add-another-email-address-scaled" width="800">
  <figcaption>Gmail帳號及匯入功能</figcaption>
</figure>

此時跳出一個新增信箱的視窗，電子郵件信箱就填寫在Cloudflare Email Routing上的位址，把視為別名的選項**取消**掉，我們需要保留原本的電子郵件地址，再回覆信件時才能夠選擇要用哪個地址來回覆，下方可以指定用來回覆的電子信箱，此時該帳號一樣填客製化的信箱，確認完之後點選下一步

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/adding-another-address.webp" alt="adding-another-address" width="800">
  <figcaption>設定客製化信箱</figcaption>
</figure>

下一步設定SMTP Server的內容，SMTP位址我們選擇gmail作為中繼，port選擇標準的587，使用者名稱則是你目前收信的信箱，因為我們是用這個gmail作為送件者，密碼則為方才我們在App Password建立的那一組，請記得密碼之間不用空格，連線選擇標準的TLS即可，所以總共需要填
- SMTP Server: smtp.gmail.com
- port: 587
- Username: 你的gmail信箱地址 (e.g. ...@gmail.com)
- Password: 方才建立的密碼
- 勾選TLS

都確認後就可以按下新增帳號

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/send-mail-through-smtp-server-2.webp" alt="send-mail-through-smtp-server" width="800">
  <figcaption>設定Gmail SMTP Server</figcaption>
</figure>

顯示成功新增後，會寄一封確認信到你的Gmail信箱裡，在按下驗證連結就設定完成了

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/adding-email-done.webp" alt="adding-email-done" width="800">
  <figcaption>完成Gmail SMTP Server設定</figcaption>
</figure>

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/confirm-gmail-smtp-settings.webp" alt="confirm-gmail-smtp-settings" width="700">
  <figcaption>驗證Gmail SMTP Server設定</figcaption>
</figure>

我們還需要回Cloudflare設定DNS指向Gmail，到你的Domain找到DNS Records新增一條TXT紀錄，為了讓Cloudflare可以驗證Gmail SMTP Server
- Type: TXT
- Name: 你的網域
- Content: v=spf1 include:_spf.mx.cloudflare.net include:_spf.google.com ~all

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/cloudflare-gmail-dns.webp" alt="cloudflare-gmail-dns" width="800">
  <figcaption>Cloudflare驗證Gmail SMTP Server的DNS紀錄</figcaption>
</figure>

最後回Gmail帳號的設定，在回覆時可以調整成寄件者指定的信箱作為回信，也可以調整預設回覆的信箱

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/replying-setting-2-scaled.webp" alt="replying-setting-scaled" width="800">
  <figcaption>Gmail SMTP設定回信的信箱位址</figcaption>
</figure>

## 測試
最後我們來測試一下有沒有設定成功，利用其他的信箱寄件給Cloudflare Domain的位址一封電子郵件

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/sending-test.webp" alt="ending-test.webp" width="600">
  <figcaption>從protonmail寄送到我的客製化信箱</figcaption>
</figure>

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/receive-test.webp" alt="receive-test" width="600">
  <figcaption>Gmail確實有收到信件，郵件位址也正確</figcaption>
</figure>

<figure>
  <img src="https://secologies.com/wp-content/uploads/2025/12/reply-test.webp" alt="reply-test.webp" width="600">
  <figcaption>用Gmail回信，protonmail確實收到來自hshuang@hshuang.blog的信件</figcaption>
</figure>

如果上述都有成功，代表讀者的設定都正確，此文以Gmail的SMTP Server作為中繼，如果讀者使用的是Outlook或者其他商業型電子郵件服務，需要確認是否可以免費設定SMTP server，像是protonmail就需要訂閱後才能新增domain name，這點需要特別注意，祝各位可以成功建立自己的網域信箱

## Reference
[1] Alex Hsu 徐小翔, "如何為網站選一個好域名," 2025年12月18日, [https://alexhsu.com/domain-names](https://alexhsu.com/domain-names).

[2] 資工小廢物 - JN, "想架部落格，需要註冊自己的網域嗎？," 2025-12-19, [https://blog.giveanornot.com/get-a-domain-or-not/](https://blog.giveanornot.com/get-a-domain-or-not/).
