"""
SUMOの特定サイトからスクレイピング
"""
from bs4 import BeautifulSoup
import urllib.request as req

# HTMLの取得
url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=14&sc=14102&sc=14104&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1"
res = req.urlopen(url)

# HTMLの解析
soup = BeautifulSoup(res, "html.parser")

# ヘッダーデータを抽出
print(soup.select_one("h1").text)

# リスト内の家賃を抽出
print("ページ内の家賃抽出開始...")

tds = soup.find_all(class_="cassetteitem_other-emphasis ui-text--bold")  # 全ての指定セレクタ内の要素を取得
for td in tds:
    print(td.text)  # .textでテキストを取得

print("抽出完了...")