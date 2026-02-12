# 🛒 Amazon Product Scraper - IMPROVED VERSION

## ✨ What's Fixed

### Previous Issues:
- ❌ Data extraction not working
- ❌ Empty CSV files
- ❌ No error handling for CAPTCHA
- ❌ Single selector strategy failing
- ❌ No debugging information

### Current Features:
- ✅ **Multiple fallback selectors** - Tries 5+ different selectors for each data field
- ✅ **Enhanced anti-bot detection** - Better headers and human-like behavior
- ✅ **CAPTCHA handling** - Detects blocks and allows manual intervention
- ✅ **Detailed debugging** - Shows exactly what's happening
- ✅ **Data validation** - Ensures CSV has actual data
- ✅ **Progress tracking** - Shows extraction progress
- ✅ **Interactive search** - Enter custom search queries

---

## 🚀 Quick Start

### 1. Run the scraper:
```bash
python amazon_websc.py
```

### 2. When prompted, enter a product to search:
```
Enter product to search (or press Enter for 'shoes'): laptop
```

### 3. If CAPTCHA appears:
- The script will pause
- Manually solve the CAPTCHA in the browser window
- Press Enter to continue

---

## 🔧 Troubleshooting

### Issue 1: "No products found"

**Cause:** Amazon is blocking automated access

**Solutions:**
```bash
# Run the test tool first
python test_amazon_scraper.py
```
This will show you:
- If Amazon is accessible
- Which selectors work
- If CAPTCHA is blocking you

**Other solutions:**
1. **Wait and retry** - Amazon may temporarily block IPs
2. **Use VPN** - Change your IP address
3. **Different network** - Try mobile hotspot or different WiFi
4. **Slower execution** - Increase delays in the code

### Issue 2: "CAPTCHA detected"

**This is normal** - Amazon actively blocks bots

**Solutions:**
1. **Manual solving** - Script pauses for you to solve CAPTCHA
2. **Residential proxy** - Use proxy services (costs money)
3. **Amazon API** - Use official Product Advertising API instead
4. **Different approach** - Consider using RSS feeds or official data exports

### Issue 3: "Empty CSV file"

**Run with debug enabled:**
```python
scraper = AmazonScraper("laptop")
scraper.debug = True  # Already enabled by default
scraper.run()
```

This will:
- Show sample extracted data
- Save page source to `amazon_debug_page.html`
- Display detailed error messages

---

## 📊 Output Format

The scraper creates `amazon_products.csv` with these columns:

| Column | Description | Example |
|--------|-------------|---------|
| Product_Name | Full product title | "Apple MacBook Pro 16-inch..." |
| Product_URL | Amazon product link | "https://www.amazon.com/dp/..." |
| Image_URL | Product image URL | "https://m.media-amazon.com/..." |
| Price | Product price | "$1,299.99" |
| Rating | Star rating | "4.5" |
| Review_Count | Number of reviews | "1234" |

---

## ⚙️ Configuration Options

### Change search query:
```python
scraper = AmazonScraper("wireless headphones")
scraper.run()
```

### Disable debugging:
```python
scraper = AmazonScraper("shoes")
scraper.debug = False  # Less console output
scraper.run()
```

### Custom output filename:
```python
scraper.save_csv("my_custom_name.csv")
```

---

## 🤖 Anti-Bot Features Implemented

1. **User Agent Spoofing** - Pretends to be real Chrome browser
2. **Webdriver Property Hiding** - Removes automation detection
3. **Human-like scrolling** - Random scroll patterns
4. **Random delays** - Variable waiting times
5. **Smart retries** - Multiple selector strategies

---

## 📝 Important Notes

### Legal Considerations:
- ⚠️ Web scraping Amazon violates their Terms of Service
- ⚠️ Use **only for educational purposes**
- ⚠️ For production use, consider **Amazon Product Advertising API**
- ⚠️ Excessive scraping may result in IP bans

### Better Alternatives:
1. **Amazon Product Advertising API** (Official)
   - Requires approval
   - 8,640 requests per day limit
   - Free with qualifying purchases
   - https://webservices.amazon.com/paapi5/documentation/

2. **Amazon Data Exports** (For sellers)
   - Official seller reports
   - No scraping needed

3. **Third-party APIs** (Paid services)
   - Rainforest API
   - ScraperAPI
   - Oxylabs

---

## 🔍 Testing Before Full Run

Always test first:
```bash
python test_amazon_scraper.py
```

This shows:
- If Amazon is accessible
- Which selectors work
- If you're being blocked

---

## 💡 Tips for Success

1. **Don't run too frequently** - Wait 10-30 minutes between runs
2. **Use VPN** - Rotate IP addresses
3. **Smaller searches** - Test with specific products first
4. **Check debug output** - Review `amazon_debug_page.html` if issues occur
5. **Be patient** - Amazon's anti-bot is aggressive

---

## 📦 Requirements

```bash
pip install selenium pandas
```

Plus Chrome browser and ChromeDriver (matching versions)

---

## 🎯 Expected Results

**Successful run:**
```
AMAZON PRODUCT SCRAPER
==================================================
🔧 Setting up Chrome driver...
✓ Driver ready

🌐 Loading: https://www.amazon.com/s?k=laptop
⏳ Waiting 4.2 seconds...
📄 Page title: Amazon.com : laptop
📜 Scrolling page (human-like behavior)...
✓ Found products with selector: div[data-asin]:not([data-asin=''])

📦 Extracting products...
✓ Found 60 containers with: div[data-asin]:not([data-asin=''])

🔄 Processing 60 products...
   Sample 1:
   Name: Apple 2023 MacBook Pro Laptop M3 chip with 8‑core CPU...
   Price: $1,599.00
   Rating: 4.5
   Reviews: 2847

✓ Successfully extracted 58 products

💾 Saved 58 products to: amazon_products.csv

📊 Data Summary:
   - Products with prices: 58
   - Products with ratings: 55
   - Products with reviews: 55
   - Products with images: 58

==================================================
✅ SCRAPING COMPLETED SUCCESSFULLY!
==================================================
```

---

## 🆘 Still Having Issues?

1. Check `amazon_debug_page.html` - See what Amazon actually returned
2. Run test tool - `python test_amazon_scraper.py`
3. Try different search query - Some products may not load properly
4. Wait longer - Amazon may have temporarily blocked your IP
5. Consider API alternative - More reliable for production use

---

## 📞 Support

If you continue having issues:
1. Check if Amazon.com loads normally in browser
2. Verify Chrome and ChromeDriver versions match
3. Review console output for specific errors
4. Inspect the saved HTML file for CAPTCHA or blocks

---

**Created for educational purposes only**  
**Last updated: February 2026**
