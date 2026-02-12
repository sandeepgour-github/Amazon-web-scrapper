# Amazon Scraping - Why You're Getting Blocked ⚠️

## The Problem

Amazon has **advanced bot detection**. When you see "Sorry something went wrong", Amazon detected automation.

---

## 🎯 QUICK SOLUTION - Use 3 Options:

### ✅ **OPTION 1: Amazon India (EASIEST - Less Strict)**

```bash
python amazon_india_simple.py
```

- Amazon India (.in) is **less strict** than .com
- Same products, easier to scrape
- **Recommended for testing**

---

### ✅ **OPTION 2: Original with Stealth**

```bash
python amazon_working.py
```

- Maximum stealth settings
- Works sometimes on Amazon.com
- Try different times of day

---

### ✅ **OPTION 3: Undetected ChromeDriver (BEST)**

Install special library that hides automation better:

```bash
pip install undetected-chromedriver
```

Then create `amazon_undetected.py`:

```python
import undetected_chromedriver as uc
import time

driver = uc.Chrome()
driver.get("https://www.amazon.com/s?k=laptop")
time.sleep(10)
# Rest of your scraping code
```

---

## Why Amazon Blocks Selenium

1. **Webdriver Detection**: `navigator.webdriver` property
2. **Missing Browser Properties**: Real browsers have 100+ properties
3. **No Browser History**: Automation has no cookies/history
4. **Suspicious Behavior**: Perfect timing, no mouse movements
5. **Chrome Automation Extensions**: Visible to Amazon

---

## Legal Alternatives

### 🔹 **Amazon Product Advertising API** (Official)

- https://webservices.amazon.com/paapi5/documentation/
- Legal and unlimited
- Requires approval

### 🔹 **Paid Scraping Services**

- **ScraperAPI**: $49/month, handles Amazon blocking
- **Bright Data**: Residential proxies bypass detection

---

## Tips to Avoid Detection

✅ **DO THIS:**

- Use Amazon India (.in) - less strict
- Scrape at night (less traffic = less detection)
- Use `undetected-chromedriver` library
- Add random delays (2-5 seconds)
- Limit to 30-50 products per run
- Clear cache between runs

❌ **DON'T DO THIS:**

- Scrape during peak hours (Amazon more suspicious)
- Extract 1000+ products at once
- Run scraper multiple times in 10 minutes
- Use default Chrome options

---

## Quick Test - Which Works?

**Test Amazon India:**

```bash
python amazon_india_simple.py
```

Type: `laptop` and press Enter

**If that fails, install undetected:**

```bash
pip install undetected-chromedriver
```

---

## For Production Use

If you need to scrape Amazon regularly:

1. **Use official API** (best, legal)
2. **Use paid proxy service** (ScraperAPI, Bright Data)
3. **Scrape Amazon India** (less detection)
4. **Use undetected-chromedriver** (bypass automation detection)

---

## Current Files

| File                     | Purpose                       | Success Rate  |
| ------------------------ | ----------------------------- | ------------- |
| `amazon_india_simple.py` | ✅ Amazon India (less strict) | ⭐⭐⭐⭐ High |
| `amazon_working.py`      | Enhanced stealth for .com     | ⭐⭐ Medium   |
| `amazon_websc.py`        | Original (fixed)              | ⭐ Low        |

---

## ❓ Still Getting Blocked?

**Try this order:**

1. Run `amazon_india_simple.py` ← START HERE
2. If blocked, wait 30 minutes
3. Try different search term
4. Install `undetected-chromedriver`
5. Consider paid service for production

---

**Remember:** Amazon intentionally blocks scrapers to protect their data. This is normal and expected!
