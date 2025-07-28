# 🔍 LinkedIn Job Scraper (Python + Selenium)

A lightweight web scraper to extract job listings from LinkedIn based on your keyword, location, and desired number of pages.

> This project is ideal for building your portfolio, automating job search, or analyzing the tech job market.

---

## 🚀 Features

- ✅ Search by **keyword** and **location**
- ✅ Scrape **multiple pages** (25 jobs per page)
- ✅ Extract job **title** and **URL**
- ✅ Save results in CSV format in a `data/` folder
- ✅ Headless browser automation with `Selenium`

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayz3ro/linkedin-job-scraper.git
   cd linkedin-job-scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the script from terminal:

```bash
python linkedin_job_scraper.py
```

You will be prompted to enter:

- a job keyword (e.g. `python developer`)
- a location (e.g. `Germany`)
- how many pages to scrape

> Each page contains approximately 25 job listings.

Results will be saved to:  
`data/python_Germany_2025-07-28.csv` *(example)*

---

## 📁 Folder Structure

```
linkedin-job-scraper/
├── data/                    # CSV output files
├── linkedin_job_scraper.py  # Main script
├── README.md
└── requirements.txt
```

---

## 📘 Example Output

```csv
title,link
"Python Developer","https://www.linkedin.com/jobs/view/..."
"Senior Backend Engineer","https://www.linkedin.com/jobs/view/..."
...
```

---

## 🛡 Limitations & Tips

- This script **does not use login or API** – only public LinkedIn job search pages.
- LinkedIn may block frequent scrapers; avoid rapid repeated use.
- Add random delays or proxy support if needed.
- For more advanced scraping (e.g. company info, descriptions), login via Selenium may be required.

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share it.

---
