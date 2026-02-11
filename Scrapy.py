import requests
from bs4 import BeautifulSoup
################# ILLegal way ###################
#scrapping tool: Zyte,Apify,Web Scraper (Chrome Extension),Octoparse,Playwright,scrapy,Selenium...

url = "https://www.ubuy.tn/en/category/electronics-10171"

# Headers are important! They tell the website you are a browser, not a bot(anti-scrapping mecanism).
#Rate limit: but that work only if you send too many request, usually Max 100 requests per minute per IP
#CAPTCHAs
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

print('start scraping from ' + url + ' ...')

try:
    # Send GET request
    response = requests.get(url, headers=headers)

    # Check if request was successful (200 OK)
    if response.status_code == 200:
        print("Successfully fetched the page.")
        print(f"Status code: {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all product containers based on the class 'listing-product'
        products = soup.find_all('div', class_='listing-product')

        scraped_data = []

        for product in products:
            item = {}

            # 1. Extract Title
            title_tag = product.find('a', class_='product-img')
            if title_tag and title_tag.get('title'):
                item['title'] = title_tag.get('title')
            else:
                header_tag = product.find(['h2', 'h3'])
                item['title'] = header_tag.get_text(strip=True) if header_tag else 'N/A'

            # 2. Extract Price
            price_tag = product.find('p', class_='product-price')
            item['price'] = price_tag.get_text(strip=True) if price_tag else 'N/A'

            # 3. Extract Product URL
            link_tag = product.find('a', href=True)
            item['url'] = link_tag['href'] if link_tag else 'N/A'

            # 4. Extract Image URL
            img_tag = product.find('img')
            if img_tag:
                # Prioritize data-src for lazy loading, fall back to src
                item['image_url'] = img_tag.get('data-src') or img_tag.get('src')
            else:
                item['image_url'] = 'N/A'

            scraped_data.append(item)

        # Print the results
        print(f"\nFound {len(scraped_data)} products:\n")
        for data in scraped_data:
            print(f"Title: {data['title']}")
            print(f"Price: {data['price']}")
            print(f"Link:  {data['url']}")
            print("-" * 40)

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")