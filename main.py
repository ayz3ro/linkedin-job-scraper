from time import strftime

from scraper.exporter import save_to_csv
from scraper.parser import scrape_jobs

if __name__ == '__main__':
    query = input("🔍 Enter a keyword (e.g., python): ").strip()
    location = input("📍 Enter the location (e.g., Germany): ").strip()
    pages = int(input("📄 How many pages to parse? "))
    jobs = scrape_jobs(query, location, pages)
    filename = f"{query}_{location}_{strftime('%Y-%m-%d')}.csv".replace(" ", "_")
    save_to_csv(jobs, filename)
