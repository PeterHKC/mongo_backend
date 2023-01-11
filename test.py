import requests

# 設定要爬取的網址
url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2040"

# 使用 requests 庫發出 HTTP 請求
response = requests.get(url)

# 將資料解析成 HTML 格式
html = response.text

# 找到所有的 "<td>" 標籤
td_tags = html.find_all("td")

# 建立一個空的陣列，用來存放殖利率
yield_rates = []

# 將殖利率加入陣列中
for td_tag in td_tags:
    yield_rates.append(float(td_tag.text))

# 顯示陣列
print(yield_rates)

