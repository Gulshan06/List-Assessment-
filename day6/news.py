import requests
import json # java serialize object notation 
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
edata=data.json()
print(edata)
# articles= edata['articles']
# print(articles)
# print(len(articles))
# li = []
# for i in articles:
#     li.append(i['title'])
# count= 0
# message = ' '.join([str(i) for i in li])
# message=message.lower()
# for x in message:
#     if (x == 'a') or (x=='e') or (x=='i') or (x=='o') or (x=='u'):
#         count+=1
# print(count)
