import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
print(data.text)