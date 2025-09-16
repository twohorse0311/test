import requests

# GET 請求
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())  # JSON 資料

# 帶參數的 GET 請求
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)
data = response.json()
print(f"找到 {data['total_count']} 個 Python 專案")

# POST 請求
data = {'name': 'test', 'value': 123}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())

# 處理錯誤
try:
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()  # 檢查狀態碼
except requests.exceptions.RequestException as e:
    print(f"請求錯誤：{e}")
