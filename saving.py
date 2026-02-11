import requests
import csv



url = "https://dummyjson.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()["posts"]  # list of posts
    print(f"Collected {len(data)} posts from API")
else:
    print("Failed to fetch data")
    data = []


csv_data = []
for post in data[:10]:  # limit to 10 for demo
    title = post["title"]
    likes = post["reactions"]
    csv_data.append([title, likes])

#  Write CSV
with open("dummy_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Likes"])
    writer.writerows(csv_data)

print("Data saved to dummy_data.csv for ETL processing")
