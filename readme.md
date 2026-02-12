📦 Amazon Product Data Extractor

A Python-based product data extraction and analytics system that collects structured product information from Amazon search results and generates ranked insights.

🚀 Overview

Amazon Product Data Extractor is a web automation and data analytics project built using Python and Selenium. The system extracts structured product data such as title, price, rating, and review count from Amazon search results and exports the processed data into CSV format for analysis.

This project demonstrates:

Web automation

Dynamic content handling

Data cleaning and transformation

Ranking logic implementation

Structured dataset generation

🛠 Tech Stack

Programming Language: Python 3.x

Web Automation: Selenium WebDriver

Browser: Google Chrome + ChromeDriver

Data Processing: Pandas

Data Format: CSV

Optional (Advanced Version): Amazon Product Advertising API (PA-API 5.0)

📂 Features

Extracts product name

Extracts product URL

Extracts product image URL

Extracts price

Extracts rating score

Extracts review count

Visits product page for description (optional enrichment)

Generates Top-N ranking based on rating and reviews

Exports structured dataset to CSV

📊 Sample Extracted Fields
Field Name	Description
Product_Name	Product title
Product_URL	Direct Amazon link
Image_URL	Product image link
Price	Listed price
Rating	Star rating
Review_Count	Number of reviews
Description	Product feature bullets
🏗 Project Structure
amazon-data-extractor/
│
├── amazon_scraper.py
├── amazon_products.csv
├── README.md
└── requirements.txt

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/amazon-data-extractor.git
cd amazon-data-extractor

2️⃣ Install Dependencies
pip install -r requirements.txt


Or manually install:

pip install selenium pandas

3️⃣ Download ChromeDriver

Download ChromeDriver matching your Chrome version

Add it to system PATH

▶️ Usage

Run the script:

python amazon_scraper.py


The program will:

Launch Chrome browser

Load Amazon search results

Extract product data

Generate CSV file

📈 Ranking Logic

The system ranks products based on:

Higher rating score

Higher review count

This enables identification of high-performing products.