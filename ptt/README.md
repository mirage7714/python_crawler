# ptt爬蟲

## 身為資深鄉民，可以不看Facebook但是一定要看ptt，那就來個ptt爬蟲吧
### 網頁版ptt bbs首頁:<a href="https://www.ptt.cc/bbs/index.html">https://www.ptt.cc/bbs/index.html/</a>

<h2>一個新看板的誕生:</h2>
<p>雖然現在用ptt的人數已經大不如前，但是還是會有新的看板成立</p>
<p>為了見證一個看板從無到有的內容，先來測試怎麼抓取一個看板的所有文章吧</p>
<p>這次就決定挑少前板來當作研究的目標:</p>
<p>(不要問我為什麼選少前版，因為這是我少數可以玩超過一年的手遊XDD)</p>
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/python_crawler/blob/master/ptt/girlsfront/data_parser.ipynb">1. 將看板中所有文章的作者、標題、內文以及推文都抓下來並存成檔案</a></li>
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/python_crawler/blob/master/ptt/girlsfront/visualization.ipynb">2. 想知道大家到底都發了什麼文，用文字雲來看看吧</a></li>

<h2>下一步呢?</h2>
<p>每次都把整個看板的文章抓完也不是辦法，因為要花太多的時間了</p>
<p>改成只抓最新的文章就好了</p>
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/python_crawler/blob/master/ptt/girlsfront/daily_ptt_parser.ipynb">利用列表中的發文的時間，來當作判斷的標準</li>