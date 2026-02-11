import requests
################# Legal way ###################
#this is a script that simulate a api request; so because i can get an api without token or in legal ,
#free way so i am gonna use https://dummyjson.com/ for testing
#this is the same way as postMan , Curl and SoapUI

url = "https://dummyjson.com/posts"

print('Requesting data...')
response = requests.get(url)#demande de data get http

if response.status_code == 200:
    data = response.json()

    print("Reels collected successfully!\n")

    for post in data["posts"][:5]:   # show 5 reels
        print("Reel ID:", post["id"])
        print("Content:", post["title"])
        print("Likes:", post["reactions"])
        #print(post) : i use this for the first time but then i orgonise it (it is way to transform data T)
        print("-" * 30)
else:
    print("Error:", response.status_code)
