"""
Amazon Scraper - Quick Test Tool
Tests if Amazon is accessible and shows what selectors work
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def quick_test():
    print("="*70)
    print("AMAZON SCRAPER - QUICK TEST")
    print("="*70)
    
    # Setup
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        # Test URL
        url = "https://www.amazon.com/s?k=laptop"
        print(f"\n🌐 Loading: {url}")
        driver.get(url)
        time.sleep(5)
        
        print(f"📄 Page Title: {driver.title}")
        
        # Check for CAPTCHA
        page_lower = driver.page_source.lower()
        if "captcha" in page_lower or "robot check" in page_lower:
            print("\n❌ CAPTCHA DETECTED!")
            print("💡 Amazon is blocking automated access")
            print("   Solutions:")
            print("   1. Wait and try again later")
            print("   2. Use VPN or different network")
            print("   3. Manually solve CAPTCHA")
            input("\n⏸️ Solve CAPTCHA if you can see it, then press Enter...")
        else:
            print("✓ No CAPTCHA detected")
        
        # Test selectors
        print("\n🔍 Testing product selectors...")
        
        selectors = [
            "div[data-component-type='s-search-result']",
            "div.s-result-item[data-asin]",
            "div[data-asin]:not([data-asin=''])",
            "h2 a span"
        ]
        
        for selector in selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    print(f"  ✓ {selector}: Found {len(elements)} elements")
                    if len(elements) > 0:
                        sample_text = elements[0].text[:60] if elements[0].text else "[No text]"
                        print(f"     Sample: {sample_text}")
                else:
                    print(f"  ✗ {selector}: Found 0 elements")
            except Exception as e:
                print(f"  ✗ {selector}: Error - {e}")
        
        print("\n✅ Test complete! Check results above.")
        print("💡 If selectors found 0 elements, Amazon might be blocking.")
        
        input("\n⏸️ Press Enter to close browser...")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    quick_test()
