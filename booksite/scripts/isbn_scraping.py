# Extract Book Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from bs4 import BeautifulSoup

### these options are relevant to run selenium on a remote server
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


driver.get("https://www.isbn.de/")
book_data = {}

def search(driver, ISBN):
    try:
        search_box = driver.find_element(By.ID, "searchbox")

        search_box.clear()
        search_box.send_keys(ISBN)
    except Exception as e:
        print("Error while interacting with the input field:", e)
    search_box.send_keys(Keys.RETURN)

def get_data():
    try:
        try:
            ##Extracting the title of the book
            title_data = driver.find_element(By.CSS_SELECTOR, "#content > div.isbnbook > div.isbnhead")
            # Find all header elements within title_data
            header_elements = title_data.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6")

            title_text = title_data.text
            for element in header_elements:
                title_text += " " + element.text

            book_data["Title"] = title_text
            book_data["Url"] = driver.current_url
        except Exception as e:
            print("Error extracting title:", e)


        ##Extracting the data from the infotab with the book details
        infotab = driver.find_element(By.CSS_SELECTOR, "#main > div > div.layout-wrapper > div > div > div.layout-cell.sidebar.sbr > div > div.ISBNdata > div.infotab")
        rows = infotab.find_elements(By.XPATH, "./div")
        for row in rows:
            try:
                key = row.find_element(By.XPATH, "./div").text
                value_element = row.find_elements(By.XPATH, "./a | ./span | ./div[2]")
                value = " ".join([v.text for v in value_element]) if value_element else row.text.split(key, 1)[-1].strip()
                book_data[key] = value
            except Exception as e:
                print(f"Skipping a row due to error: {e}")

        #clean up book_data keys
        book_data['Einband'] = book_data.pop('Einband - flex.(Paperback)')
        book_data['Erscheinungsdatum'] = book_data.pop('erschienen am')

        try:
            ## Extracting the description of the book
            desc_data = driver.find_element(By.CSS_SELECTOR, "#bookdesc")
            desc_html = desc_data.get_attribute('innerHTML')
            soup = BeautifulSoup(desc_html, 'html.parser')
            desc_text = soup.get_text(separator=' ', strip=True)

            book_data["Beschreibung"] = desc_text
        except Exception as e:
            print("Error extracting description:", e)


    except Exception as e:
        print("Error:", e)


def get_ISBN_data(ISBN):
    book_data.clear()
    search(driver, ISBN)
    sleep(1)
    get_data()
    driver.quit()
    return(book_data)

#visual test of get_ISBN_data
#print(get_ISBN_data("978-3-608-98701-0"))