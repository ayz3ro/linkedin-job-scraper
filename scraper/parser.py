from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def scrape_jobs(query, location, pages=1):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    base_url = "https://www.linkedin.com/jobs/search/"
    full_results = []

    for page in range(pages):
        offset = page * 25
        url = f"{base_url}?keywords={query}&location={location}&start={offset}"

        print(f"[{page+1}/{pages}] Loading:", url)
        driver.get(url)
        sleep(4)

        job_cards = driver.find_elements(By.CSS_SELECTOR, "a.base-card__full-link")

        for card in job_cards:
            title = card.get_attribute("innerText").strip()
            link = card.get_attribute("href")
            full_results.append({
                "title": title,
                "link": link
            })

    driver.quit()
    return full_results