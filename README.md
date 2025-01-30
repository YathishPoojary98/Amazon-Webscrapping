# 📦 Amazon Webscrapping

This Python script scrapes **Amazon India** for phone listings, extracting **product names** and their **prices** using `BeautifulSoup` and `requests`. The scraped data is then saved into a **CSV file** for further analysis.

---

## 🚀 Features

✅ **Web Scraping** – Extracts phone names and prices from Amazon India.  
✅ **Saves Data to CSV** – Stores the extracted data in `Phones.csv`.  
✅ **User-Agent Handling** – Uses headers to simulate a real browser request.  
✅ **Efficient Parsing** – Uses `BeautifulSoup` to extract data accurately.  

---

## 🛠 Requirements

Ensure you have the following installed:

- **Python 3.x**
- **Libraries:** `requests`, `BeautifulSoup`, `csv`

To install the required dependencies, run:

```bash
pip install requests beautifulsoup4 lxml
```

---

## 📥 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YathishPoojary98/Amazon-Webscrapping.git
```

Navigate into the cloned directory:

```bash
cd amazon-phone-scraper
```

### 2️⃣ Run the Script

Execute the following command to start scraping:

```bash
python scraper.py
```

---

## 📊 Output

The scraped data will be saved in a file named **`Phones.csv`** with the following format:

| Sr.No | Phone Name | Prices |
|-------|-----------|--------|
| 1     | Example Phone 1 | ₹15,999 |
| 2     | Example Phone 2 | ₹22,499 |

---

## 🔍 How It Works

1️⃣ **Sends an HTTP request** to Amazon India with a **User-Agent** to mimic a real browser.  
2️⃣ **Parses the HTML response** using `BeautifulSoup`.  
3️⃣ **Extracts phone names and prices** from the parsed content.  
4️⃣ **Writes the extracted data** into `Phones.csv` in a structured format.  

---

## ⚠️ Disclaimer

This script **scrapes data from Amazon**, which may violate **Amazon’s Terms of Service**. Use it for educational purposes only. Amazon may block your requests if excessive scraping is detected.

---

