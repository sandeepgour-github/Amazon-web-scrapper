"""
SIMPLE AMAZON SCRAPER - Amazon India (Less Strict)
This scrapes Amazon.in instead of .com (easier to scrape)
"""

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def setup_browser():
    """Setup Chrome"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def scrape_amazon_india(search_query):
    """Scrape Amazon India"""
    print(" Starting Amazon India Scraper...\n")
    
    driver = setup_browser()
    products = []
    
    try:
        # Use Amazon India (less strict)
        url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}"
        print(f" Loading: {url}")
        driver.get(url)
        time.sleep(5)
        
        print(f" Page: {driver.title}\n")
        
        # Scroll
        for i in range(3):
            driver.execute_script(f"window.scrollBy(0, {500 + i*200});")
            time.sleep(1)
        
        # Find products
        items = driver.find_elements(By.CSS_SELECTOR, "[data-asin]")
        print(f"Found {len(items)} items\n")
        
        count = 0
        for item in items[:40]:
            try:
                asin = item.get_attribute('data-asin')
                if not asin or len(asin) != 10:
                    continue
                
                # Name
                name = ""
                try:
                    name = item.find_element(By.CSS_SELECTOR, "h2").text.strip()
                except:
                    pass
                
                if not name:
                    continue
                
                # Price
                price = ""
                try:
                    price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                except:
                    pass
                
                # Rating  
                rating = ""
                try:
                    rating = item.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text.split()[0]
                except:
                    pass
                
                # Image
                img = ""
                try:
                    img = item.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
                except:
                    pass
                
                product = {
                    'ASIN': asin,
                    'Name': name,
                    'Price': f"₹{price}" if price else "",
                    'Rating': rating,
                    'Image': img,
                    'URL': f"https://www.amazon.in/dp/{asin}"
                }
                
                products.append(product)
                count += 1
                
                if count <= 5:
                    print(f"{count}. {name[:60]}... | {product['Price']}")
                
            except:
                continue
        
        print(f"\n Extracted {len(products)} products")
        
        # Save CSV
        if products:
            filename = "amazon_india_products.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['ASIN', 'Name', 'Price', 'Rating', 'Image', 'URL'])
                writer.writeheader()
                writer.writerows(products)
            print(f" Saved to: {filename}")
        
    except Exception as e:
        print(f" Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    search = input("Search product (or Enter for 'laptop'): ").strip() or "laptop"
    scrape_amazon_india(search)
