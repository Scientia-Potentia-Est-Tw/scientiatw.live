---
title: "部落格問題挑戰"
date: "2025-10-18T14:19:00+08:00"
lastmod: "2025-11-04T10:10:00+08:00"
author: "黃宏勝"
categories:
  - 生活
tags:
  - bear blog question challenge
  - Blog Questions Challenge
  - 挑戰
  - 部落格
  - 故事
keywords:
  - 生活
  - bear blog question challenge
  - Blog Questions Challenge
  - 挑戰
  - 部落格
  - 故事
description: "在廢文小天地看到的Blog Questions Challenge"
image: "https://scientia-potentia-est.com/wp-content/uploads/2025/10/blog-questions-challenges-cover-scaled.webp"
slug: "blog-questions-challenge"
---
在廢文小天地RSS看到部落格挑戰[1]，源自Kev Quirk的Blog Questions Challenge[2]，看到題目蠻有興趣的，所以決定也寫一篇來回應各項問題

主要的問題有8題，總共是：
1. 你當初為什麼開始寫部落格？
2. 你使用什麼平台來管理你的部落格？為什麼選擇它？
3. 你之前有在其他平台上寫過部落格文章嗎？
4. 你如何撰寫文章？例如，使用本地編輯工具，還是在部落格的後台／控制面板中編寫？
5. 你什麼時候最有寫作靈感？
6. 你會在寫完後立即發布，還是會先存成草稿醞釀一下？
7. 你部落格上最喜歡的文章是哪一篇？
8. 你對部落格有什麼未來計畫嗎？例如重新設計、搬到另一個平台，或是加入新功能？

## 你當初為什麼開始寫部落格？
大學時期為了紀錄課程筆記，以及需要一個展示空間給轉學考的委員可以看我的作品，所以架了一個Github Page網站po一些學習上的心得，後來去實習後覺得可以經營自己的品牌，所以開始寫一些工作上的學習筆記

一開始的打算是把電腦科學裡學到的，跟平時生活心得與閱讀心得等等都在同一個網站中呈現，但隨著文章越來越多，整個網站內含所有主題越看越混淆，所以決定讓VPS主要展示技術型的文章，而這個部落格則是主要分享生活型的文章

## 你使用什麼平台來管理你的部落格？為什麼選擇它？
- [Github Pages](https://docs.github.com/en/pages)
- Wordpress
- [Cloudflare Pages](https://pages.cloudflare.com/)

大學時期沒有收入時只能選擇免費的Github Pages當作網頁空間，開始實習後有些工讀的薪水，在網路上看來看去要經營自媒體應該要架設自己的網站與網域，所以開始買了VPS安裝Wordpress

由於我之後有打算啟動訂閱服務以及線上課程的規劃，並且讀者的個人資料我想要自己全權掌控減少風險，就一定需要有資料庫管理讀者的資訊，Wordpress自然就成為我的第一選項，而且wordpress除了免費的模板功能就夠用之外，支援LaTex、多語言切換以及SEO等套件都有免費版的可以安裝

另一個考量的點是Github Repository建議只儲存5GB以下的內容在上面，光把Hugo模板上傳上去就花了一些空間，而隨著文章增加就會越需要引用更多張圖片，如果把圖片全部上傳在Github上會讓部署時間越來越久，所以Wordpress的媒體空間也提供一個網路圖庫空間給我的社群部落格儲存所有圖片

近期將Github Pages改到Cloudflare Pages上，雖然原本的Github Pages就挺夠用的了，但SEO就是唯一也是我最煩惱的問題，由於Github的CDN只有在美國地區比較完善，相較之下亞洲地區還不夠好，而不巧我的文章大部分都是中文的，目前TA都是亞太地區

我架設社群部落格已經一段時間了，但不是每一篇文章在Google搜尋引擎上可以有好的排名，所以決定換成CloudFlare Pages使用CloudFlare的DNS服務，原因光是免費方案就不限流量了，甚至防範DDoS、惡意爬蟲以及防火牆服務都是免費的

而且從Github Pages換到Cloudflare Pages很方便，只需要把原本放在Github上的repo連接到Cloudflare上就可以了，Cloudflare就會根據專案裡面的檔案自動部署出同樣的網站，而只要把網域指向Cloudflare就可以把整個網站換到Cloudflare Pages上

原先我每一篇文章在vim裡寫完markdown檔案後還要用Hugo compiler重新編譯，再到/public將輸出的檔案push到github repo裡讓Action部署，但我現在直接在repo裡修改就可以讓Cloudflare自動部署更新

## 你之前有在其他平台上寫過部落格文章嗎？
高職時期上科技應用課時，老師有教我們開Google Blogger網誌，但寫完一篇關於高一生活的文章，之後就沒有再開過了，那個Google帳號我也不確定還有沒有在用，後來就只在自己架設的地方寫文章

## 你如何撰寫文章？例如，使用本地編輯工具，還是在部落格的後台／控制面板中編寫？
不管是技術文章或是閱讀心得，我總會先在Obsidian上做許多卡片盒筆記，搜集好一定份量的素材後才決定開始寫文章

之後再貼到Wordpress上的撰寫區塊，調整字型，比較麻煩的就是Obsidian裡原生Latex是用錢字號(\$)，但換到Wordpress上的模板inline mode是用[latex]來標記

而Cloudflare Pages上的文章都是我從素材裡貼到Vim編輯器裡的Markdown檔案產出的，把文章範例模板儲存在一個txt檔案裡，每次開新的一篇都從裡面複製出來貼到vim上，再開始寫完整篇

## 你什麼時候最有寫作靈感？
每天晚上吃完晚餐後的休息時間，由於晚餐過後注意力也下降許多，所以會開始審視當日白天新增的卡片盒筆記資料庫，整理今天寫的卡片並且更新Obsidian Canvas時就會想到有哪些素材是可以寫成文章的

另外看RSS閱讀器時，看到有些部落格更新了新文章，覺得有趣的內容就決定延伸寫一篇我自己的想法

## 你會在寫完後立即發布，還是會先存成草稿醞釀一下？
我自己習慣寫完就馬上發出去，畢竟在Wordpress上有些題目是當初想寫的，但由於素材還沒整理好，所以就一直拖到現在也還躺在草稿區裡，但一直拖著也不是辦法，最近也把那些只有標題的草稿刪掉了

未來規劃要養成Obsidian裡有足夠的素材時才開始寫文章，不然東缺西缺一直放在資料夾裡我看了也心煩

## 你部落格上最喜歡的文章是哪一篇？
在我的技術部落格裡，我最喜歡的是《[PUF 晶片上的物理不可複製功能](https://scientia-potentia-est.com/zh/physical-unclonable-function/)》這文章，當初修硬體安全這門課時體驗很好，學到很多東西

也是讓我不後悔延畢後所遇到的一門課，讓我認識除了做純密碼研究之外還有更廣泛應用的領域，而裡面談保護晶片最重要的方法之一就是使用PUF，所以我認為這篇作為晶片安全的入門很適合

而個人部落格裡則是《[自主選擇乾淨的資訊，回歸RSS的懷抱吧！](https://scientiatw.live/p/you-should-use-rss/)》了吧，脫離了社群媒體之後，RSS閱讀器真的為我的人生帶來了不一樣的感受，感覺腦袋裡雲裡霧裡的感覺都消失了

也遇到了許多優秀的個人部落格，每天透過閱讀RSS新文章，就能夠為我每天的生活注入新的火焰

## 你對部落格有什麼未來計畫嗎？例如重新設計、搬到另一個平台，或是加入新功能？
技術部落格如我冀望它的名字，《[資通安全第一品牌](https://scientia-potentia-est.com/)》，成為台灣地區學習資安技術的指標之一，另外就是多補充詳細的數學文章彌補讀者的底層知識，讓網站成為自給自足(self-contained)的平台

以及目前開放免費的電子報註冊[https://scientia-potentia-est.com/zh/newsletter-zh/](https://scientia-potentia-est.com/zh/newsletter-zh/)，未來打算推出訂閱制的電子報，還有推出一些線上課程，Wordpress模板換了好幾次，目前這個消耗的計算資源最少，應該不會再換了

而個人部落格未來如果Cloudflare Pages開始收費的話可能又要換平台了，但我對目前的Hugo模板很滿意，之前換過好幾次模板只有這一次的滿足卡片式、關鍵字搜尋、目錄支援且最重要有meta tag的SEO優化，所以未來應該不會考慮換模板

未來素描作品比較能讓人看的話，考慮做一個類似雷歐的圖文版面[3]介面或者是Yelle的瀑布式相冊[4]來呈現圖片，可以展示出我每一張作品，應該會換網域名字，由於個人部落格主要就是推廣我自己，所以之後網域想要換成hshuang

除此之外就是把目前的文章翻譯成英文的版本了吧，以及預計未來學其他種新語言後可以把舊文章翻譯成該語言，除了練習該語言的語法之外，也希望讓母語人士了解我的心情

## Reference
[1] 皮皮, "部落格挑戰," [https://trashposts.com/blog/blog-questions-challenge](https://trashposts.com/blog/blog-questions-challenge/)

[2] Kev Quirk, "Blog Questions Challenge," [https://kevquirk.com/blog/blog-questions-challenge/](https://kevquirk.com/blog/blog-questions-challenge/)

[3] 朱智宇, "圖文," [https://revolc.blog/gallery/](https://revolc.blog/gallery/)

[4] Yelle, "相冊," [https://yelleis.top/gallery/](https://yelleis.top/gallery/)
