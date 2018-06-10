"""
Yahooファイナンスより為替レートを取得するサンプル
"""
from bs4 import BeautifulSoup
import urllib.request as req

# HTMLの取得
url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
res = req.urlopen(url)

# HTMLの解析
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出
price = soup.select_one(".stoksPrice").string
print("used/jpy", price)
