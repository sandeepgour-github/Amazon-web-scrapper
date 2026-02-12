"""
Amazon Search Scraper (Educational Use Only)

This scraper:
- Loads Amazon search results
- Extracts product name, URL, image, price, rating, reviews
- Detects CAPTCHA block
"""

import time
import random
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AmazonScraper:

    def __init__(self, search_query):
        self.url = f"https://www.amazon.com/s?k={search_query.replace(' ', '+')}"
        self.driver = None
        self.products = []

    # ---------------------------------------------------------
    # DRIVER SETUP
    # ---------------------------------------------------------
    def setup_driver(self):

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    # ---------------------------------------------------------
    # LOAD PAGE
    # ---------------------------------------------------------
    def load_page(self):

        self.driver.get(self.url)
        time.sleep(random.uniform(4, 6))

        print("Page title:", self.driver.title)

        # Detect CAPTCHA / Robot Check
        page_lower = self.driver.page_source.lower()
        if "captcha" in page_lower or "robot check" in page_lower:
            print("⚠ Amazon blocked this request (CAPTCHA detected)")
            return False

        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.s-search-result")
                )
            )
            return True
        except TimeoutException:
            print("⚠ Products did not load (possible block)")
            return False

    # ---------------------------------------------------------
    # EXTRACT PRODUCTS
    # ---------------------------------------------------------
    def extract_products(self):

        containers = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.s-search-result[data-component-type='s-search-result']"
        )

        print(f"Found {len(containers)} product containers")

        for container in containers:
            try:
                name_elem = container.find_element(By.CSS_SELECTOR, "h2 a")
                name = name_elem.text.strip()
                url = name_elem.get_attribute("href")

                # Image
                img_url = ""
                try:
                    img = container.find_element(By.CSS_SELECTOR, "img.s-image")
                    img_url = img.get_attribute("src")
                except:
                    pass

                # Price
                price = ""
                try:
                    whole = container.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                    fraction = container.find_element(By.CSS_SELECTOR, "span.a-price-fraction").text
                    price = f"${whole}.{fraction}"
                except:
                    pass

                # Rating
                rating = ""
                try:
                    rating_elem = container.find_element(By.CSS_SELECTOR, "span.a-icon-alt")
                    match = re.search(r"(\d+\.?\d*)", rating_elem.text)
                    if match:
                        rating = match.group(1)
                except:
                    pass

                # Reviews
                reviews = ""
                try:
                    review_elem = container.find_element(
                        By.CSS_SELECTOR,
                        "span.a-size-base.s-underline-text"
                    )
                    reviews = review_elem.text.replace(",", "")
                except:
                    pass

                self.products.append({
                    "Product_Name": name,
                    "Product_URL": url,
                    "Image_URL": img_url,
                    "Price": price,
                    "Rating": rating,
                    "Review_Count": reviews
                })

            except:
                continue

        print(f"✓ Extracted {len(self.products)} products")

    # ---------------------------------------------------------
    # SAVE CSV
    # ---------------------------------------------------------
    def save_csv(self, filename="amazon_products.csv"):
        df = pd.DataFrame(self.products)
        df.to_csv(filename, index=False)
        print(f"✓ Saved {filename}")

    # ---------------------------------------------------------
    # MAIN RUN
    # ---------------------------------------------------------
    def run(self):

        try:
            print("AMAZON SCRAPER STARTED\n")

            self.setup_driver()

            if self.load_page():
                self.extract_products()

                if self.products:
                    self.save_csv()
                else:
                    print("No products extracted.")
            else:
                print("Stopping due to block detection.")

        finally:
            if self.driver:
                self.driver.quit()


if __name__ == "__main__":
    scraper = AmazonScraper("shoes")
    scraper.run()
