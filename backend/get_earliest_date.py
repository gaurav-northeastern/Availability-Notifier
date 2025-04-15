from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_earliest_dates(visa_type, location, vac):
    
    url = "https://checkvisaslots.com/latest-us-visa-availability.html"
    table_id = visa_type if visa_type.startswith("table_") else f"table_{visa_type}"
    driver = None

    try:
        options = webdriver.ChromeOptions()
        options.headless = True
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
            EC.presence_of_element_located((By.ID, table_id))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', {'id': table_id})
        if not table:
            print(f"❌ Table with ID '{table_id}' not found!")
            return None

        result = {}
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 3:
                continue

            label = cells[0].text.strip()
            date = cells[2].text.strip()

            if label == location:
                result[location] = date
            elif vac and label == f"{location} VAC":
                result[f"{location} VAC"] = date

            # Break if enough data collected
            if vac and location in result and f"{location} VAC" in result:
                break
            elif not vac and location in result:
                break

        return result if result else None

    except Exception as e:
        print(f"❌ Error in get_earliest_dates: {e}")
        return None

    finally:
        if driver:
            driver.quit()
