# 愛評網爬蟲

## 因為最近在練習爬蟲，加上工作有需要一些POI的資料，就找了愛評網來當作練習目標
### 雖然愛評網的網頁結構算是清楚的，不過因為在分類面上電話是用圖檔的方式來顯示，用一般的html parser是沒辦法破解的，這時候剛好前陣子練習的deep learning就派上用場了!!

### 先從建立模型開始
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/ipeen/blob/master/model/image_process.ipynb">1. 因為電話號碼數字長度不一定，所以先進行數字分割</a></li>
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/ipeen/blob/master/model/train_model.ipynb">2. 用上面步驟建立的資料集來訓練模型</a></li>
<li><a href="http://nbviewer.jupyter.org/github/mirage7714/ipeen/blob/master/model/predict_phone_number.ipynb">3. 測試一下訓練出來的模型是否可以正確判斷數字</a></li>

### 確定模型可以正確判斷電話號碼之後，就是開始進行爬蟲的工作了
