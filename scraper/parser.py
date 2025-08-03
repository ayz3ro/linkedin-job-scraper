import logging
from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


def scrape_jobs(query: str, location: str, pages: int = 1) -> List[Dict[str, str]]:
    """Parse job openings from LinkedIn by keyword and location."""

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
    except WebDriverException as e:
        logging.exception("Unable to launch Chrome WebDriver")
        return []

    base_url = "https://www.linkedin.com/jobs/search/"
    results = []

    try:
        for page in range(pages):
            offset = page * 25
            url = f"{base_url}?keywords={query}&location={location}&start={offset}"

            logging.info(f"[{page + 1}/{pages}] Loading: {url}")
            driver.get(url)
            sleep(4)

            job_cards = driver.find_elements(By.CSS_SELECTOR, "a.base-card__full-link")
            if not job_cards:
                logging.warning(f"⚠️ No results on page {page + 1}")

            for card in job_cards:
                title = card.get_attribute("innerText") or "No title"
                link = card.get_attribute("href") or "No link"
                results.append({
                    "title": title.strip(),
                    "link": link.strip()
                })

    except Exception as e:
        logging.exception("An error occurred while parsing job listings.")
    finally:
        driver.quit()

    return results