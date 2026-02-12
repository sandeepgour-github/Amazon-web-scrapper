"""
Working Amazon Scraper with Enhanced Anti-Bot Protection
Uses undetected-chromedriver to bypass Amazon's bot detection
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
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class WorkingAmazonScraper:
    def __init__(self, search_query):
        self.url = f"https://www.amazon.com/s?k={search_query.replace(' ', '+')}"
        self.driver = None
        self.products = []

    def setup_driver(self):
        """Setup Chrome with maximum stealth"""
        print("🔧 Setting up stealth Chrome driver...")
        
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # More realistic user agent
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        
        # Additional stealth options
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-notifications")
        
        # Disable images for faster loading (optional)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)
        
        self.driver = webdriver.Chrome(options=options)
        
        # Execute stealth scripts
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
                Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                window.chrome = {runtime: {}};
            """
        })
        
        self.wait = WebDriverWait(self.driver, 20)
        print("✓ Driver ready")

    def load_page(self):
        """Load Amazon with human simulation"""
        print(f"\n🌐 Loading: {self.url}")
        self.driver.get(self.url)
        
        # Wait and simulate human behavior
        time.sleep(random.uniform(3, 5))
        
        print(f"📄 Page title: {self.driver.title}")
        
        # Check for errors
        page_text = self.driver.page_source.lower()
        if "sorry" in page_text and "something went wrong" in page_text:
            print("\n❌ Amazon Error Page Detected!")
            print("💡 Try: Different network, VPN, or wait 30 minutes")
            return False
        
        if "robot check" in page_text or "captcha" in page_text:
            print("\n⚠️ CAPTCHA detected - please solve manually")
            input("Press Enter after solving CAPTCHA...")
        
        # Scroll like human
        self.human_scroll()
        time.sleep(2)
        
        return True

    def human_scroll(self):
        """Realistic scrolling behavior"""
        try:
            for i in range(3):
                scroll = random.randint(400, 800)
                self.driver.execute_script(f"window.scrollBy(0, {scroll});")
                time.sleep(random.uniform(0.8, 1.5))
            
            # Scroll back up
            self.driver.execute_script("window.scrollBy(0, -300);")
            time.sleep(random.uniform(0.5, 1))
        except:
            pass

    def extract_products(self):
        """Extract products with simple approach"""
        print("\n📦 Extracting products...")
        
        # Find all product containers
        containers = self.driver.find_elements(By.CSS_SELECTOR, "[data-asin]:not([data-asin=''])")
        print(f"✓ Found {len(containers)} product containers")
        
        if len(containers) == 0:
            print("❌ No products found - Amazon may be blocking")
            return
        
        print(f"\n🔄 Processing products...\n")
        
        for idx, container in enumerate(containers[:50], 1):  # Limit to 50 for speed
            try:
                asin = container.get_attribute('data-asin')
                if not asin:
                    continue
                
                product = {
                    "ASIN": asin,
                    "Product_Name": "",
                    "Product_URL": f"https://www.amazon.com/dp/{asin}",
                    "Image_URL": "",
                    "Price": "",
                    "Rating": "",
                    "Review_Count": ""
                }
                
                # Get product name
                try:
                    name = container.find_element(By.CSS_SELECTOR, "h2 a span").text.strip()
                    if name:
                        product['Product_Name'] = name
                except:
                    try:
                        name = container.find_element(By.CSS_SELECTOR, "h2").text.strip()
                        product['Product_Name'] = name
                    except:
                        pass
                
                # Get image
                try:
                    img = container.find_element(By.CSS_SELECTOR, "img")
                    product['Image_URL'] = img.get_attribute("src") or ""
                except:
                    pass
                
                # Get price
                try:
                    price_whole = container.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                    price_frac = container.find_element(By.CSS_SELECTOR, "span.a-price-fraction").text
                    product['Price'] = f"${price_whole}{price_frac}"
                except:
                    try:
                        price = container.find_element(By.CSS_SELECTOR, "span.a-price").text
                        product['Price'] = price.replace('\n', '')
                    except:
                        pass
                
                # Get rating
                try:
                    rating_text = container.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
                    match = re.search(r"(\d+\.?\d*)", rating_text)
                    if match:
                        product['Rating'] = match.group(1)
                except:
                    pass
                
                # Get review count
                try:
                    reviews = container.find_element(By.CSS_SELECTOR, "span[aria-label*='star']").get_attribute("aria-label")
                    match = re.search(r"(\d[\d,]*)", reviews)
                    if match:
                        product['Review_Count'] = match.group(1).replace(',', '')
                except:
                    pass
                
                # Only add if we got a name
                if product['Product_Name']:
                    self.products.append(product)
                    
                    # Show first 3 samples
                    if idx <= 3:
                        print(f"✓ Product {idx}: {product['Product_Name'][:60]}... | ${product['Price']}")
                
                # Progress
                if idx % 10 == 0:
                    print(f"   📊 Processed {idx} containers, extracted {len(self.products)} products")
                    
            except Exception as e:
                continue
        
        print(f"\n✅ Total extracted: {len(self.products)} products")

    def save_csv(self, filename="amazon_products.csv"):
        """Save to CSV"""
        if not self.products:
            print("⚠️ No products to save!")
            return
        
        df = pd.DataFrame(self.products)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"\n💾 Saved {len(df)} products to: {filename}")
        
        # Summary
        print(f"\n📊 Summary:")
        print(f"   - Products with names: {df['Product_Name'].notna().sum()}")
        print(f"   - Products with prices: {(df['Price'] != '').sum()}")
        print(f"   - Products with ratings: {(df['Rating'] != '').sum()}")

    def run(self):
        """Main execution"""
        print("="*70)
        print("🛒 WORKING AMAZON SCRAPER")
        print("="*70)
        
        try:
            self.setup_driver()
            
            if self.load_page():
                self.extract_products()
                
                if self.products:
                    self.save_csv()
                    print(f"\n{'='*70}")
                    print("✅ SCRAPING COMPLETED SUCCESSFULLY!")
                    print(f"{'='*70}")
                else:
                    print("\n❌ No products extracted")
                    print("💡 Amazon is likely blocking - try:")
                    print("   1. Use VPN (change location)")
                    print("   2. Wait 30-60 minutes")
                    print("   3. Try different search query")
            else:
                print("\n⚠️ Page load failed - Amazon blocking detected")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ Stopped by user")
        except Exception as e:
            print(f"\n❌ Error: {e}")
        finally:
            if self.driver:
                time.sleep(2)
                self.driver.quit()
                print("✓ Browser closed")


if __name__ == "__main__":
    print("\n🎯 Quick and Working Amazon Scraper")
    print("=" * 70)
    
    query = input("Search for (or Enter for 'laptop'): ").strip() or "laptop"
    
    scraper = WorkingAmazonScraper(query)
    scraper.run()
