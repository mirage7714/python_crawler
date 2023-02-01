# CakeResume爬蟲

## 又是開始看工作機會的時候了，這次決定用爬蟲自動抓取CakeResume上更新的職缺
### CakeResume連結:<a href="https://www.cakeresume.com/">https://www.cakeresume.com/</a>
### 不過因為是直接搜尋QA相關的工作，就直接用已經帶有query的條件進行爬蟲會省事的多
### 帶有查詢參數的url會變成https://www.cakeresume.com/jobs?location_list%5B0%5D=Taiwan&profession%5B0%5D=it_qa-test-engineer&order=latest

### 首先建立基本的功能，來爬取最近有更新的職缺
