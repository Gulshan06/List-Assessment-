# import requests
# import json # java serialize object notation 
# data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
# edata=data.json()
# # print(edata)
# articles = edata['articles']
# vowel = 'aeiou'
# for i in articles:
#     title = i['title']
#     count={}.fromkeys(vowel,0)
#     print(title)
#     for j in title.lower():
#         if j in count:
#             count[j]+=1
#     print(count)



# import requests
# import json # java serialize object notation 
# data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
# edata=data.json()
# # print(edata)
# articles = edata['articles']
# vowel = 'aeiou'
# for i in articles:
#     title = i['title']
#     count={}.fromkeys(vowel,0)
#     print(title)
#     for j in title.lower():
#         if j in count:
#             count[j]+=1
#     print(count)



# import requests
# import json # java serialize object notation 
# data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
# edata=data.json()
# # print(edata)
# articles = edata['articles']
# vowel = 'aeiou'
# for i in articles:
#     title = i['title']
#     count={}.fromkeys(vowel,0)
#     print(title)
#     for j in title.lower():
#         if j in count:
#             count[j]+=1
#     print(count)

import requests
import json # java serialize object notation 
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1366bfd40f3e4d21929d6fad75d406ea")
edata=data.json()
# print(edata)
articles = edata['articles']
vowel = 'aeiouAEIOU'
for i in articles:
    title = i['title']
    count={}.fromkeys(vowel,0)
    print(count)
    for j in title:
        if j in count:
            count[j]+=1
    print(count)