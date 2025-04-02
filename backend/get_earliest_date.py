from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


url = "https://checkvisaslots.com/latest-us-visa-availability.html"

def get_earliest_date():
    """Scrape the webpage using Selenium and return the earliest date found."""
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.headless = True  # Run in headless mode
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "table_B1B2Regular"))
        )
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', {'id': 'table_B1B2Regular'})
        if not table:
            print("Table not found!")
            return None

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0 and cells[0].text.strip() == "NEW DELHI VAC":
                earliest_date = cells[2].text.strip()
                return earliest_date

        print("No matching row found!")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        if driver:
            driver.quit()
