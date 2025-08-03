import logging
from time import strftime

from scraper.exporter import save_to_csv
from scraper.parser import scrape_jobs


def get_user_input() -> tuple[str, str, int]:
    """Receiving and validating user input."""
    query = input("🔍 Enter a keyword (e.g., python): ").strip()
    location = input("📍 Enter the location (e.g., Germany): ").strip()

    while True:
        try:
            pages = int(input("📄 How many pages to parse? "))
            if pages <= 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️  Please enter a valid positive integer for the number of pages.")

    return query, location, pages


def generate_filename(query: str, location: str) -> str:
    """Creating a file name with the current date."""
    date_str = strftime('%Y-%m-%d')
    return f"{query}_{location}_{date_str}.csv".replace(" ", "_")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    query, location, pages = get_user_input()
    logging.info(f"Starting scraping: query='{query}', location='{location}', pages={pages}")

    try:
        jobs = scrape_jobs(query, location, pages)
        if not jobs:
            logging.warning("No jobs found.")
        filename = generate_filename(query, location)
        save_to_csv(jobs, filename)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.exception("An error occurred during scraping or saving.")


if __name__ == '__main__':
    main()
