import time
import os

# Extract Book Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from bs4 import BeautifulSoup
import urllib.request

### these options are relevant to run selenium on a remote server
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.isbn.de/")
book_data = {}

def search(driver, ISBN):
    driver.get("https://www.isbn.de/")
    try:
        search_box = driver.find_element(By.ID, "searchbox")
        search_box.clear()
        search_box.send_keys(ISBN)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print("Error while interacting with the input field:", e)
        return False
    return True


def get_titel():
    try:
        ##Extracting the title of the book
        content = driver.find_element(By.ID, "content")
        title_data = content.find_elements(By.CSS_SELECTOR, "isbnhead")
        header_elements = title_data.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6")

        title_text = title_data.text
        for element in header_elements:
            title_text += " " + element.text

        book_data["Title"] = title_text
        book_data["Url"] = driver.current_url
    except Exception as e:
        print("Error extracting title:", e)


def get_ISBNtabel_data():
    ##Extracting the data from the infotab with the book details
    infotab = driver.find_element(By.CSS_SELECTOR, "#main > div > div.layout-wrapper > div > div > div.layout-cell.sidebar.sbr > div > div.ISBNdata > div.infotab")
    rows = infotab.find_elements(By.XPATH, "./div")

    elements = 0

    for row in rows:
        elements += 1
        try:
            key = row.find_element(By.XPATH, "./div").text
            value_element = row.find_elements(By.XPATH, "./a | ./span | ./div[2]")
            if value_element:
                value = " ".join([v.text for v in value_element])
            else:
                value = row.text.split(key, 1)[-1].strip()

            if key and value:
                if "Auflage" in key:
                    bis = value.find("bis")
                    value = key[bis:]
                elif "cover" in key.lower():
                    book_data["Einband"] = key
                    book_data["Laenge"] = value
                else:
                    book_data[key] = value

        except Exception as e:
            print(f"Error in row: {e}")


def get_beschreibung():
    try:
        ## Extracting the description of the book
        desc_data = driver.find_element(By.CSS_SELECTOR, "#bookdesc")
        desc_html = desc_data.get_attribute('innerHTML')
        soup = BeautifulSoup(desc_html, 'html.parser')
        desc_text = soup.get_text(separator=' ', strip=True)

        book_data["Beschreibung"] = desc_text
    except Exception as e:
        print("Error extracting description:", e)


def get_genre():
    try:
        ##Extracting the genre of the book
        category = driver.find_element(By.ID, "locator")
        last_li = category.find_elements(By.TAG_NAME, "li")[-1]
        book_data["Genre"] = last_li.text

    except Exception as e:
        print("Error extracting title:", e)


def save_cover():
    try:
        img = driver.find_element(By.ID, "ISBNcover")
        # get the image source
        if os.path.exists("booksite/static/tempCover.png"):
            os.remove("booksite/static/tempCover.png")

        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, "booksite/static/tempCover.png")

    except Exception as e:
        print("Error extracting img:", e)


def data_cleanup():
    try:
        #clean up book_data keys
        if "Autor" not in book_data:
            book_data["Autor"] = "Unbekannt"
        if "Jahr" not in book_data:
            if "erschienen am" in book_data:
                book_data["Jahr"] = book_data["erschienen am"][-4:]
            elif "erschienen im" not in book_data:
                book_data["Jahr"] = book_data["erschienen im"][-4:]

        book_data["Preis"] = book_data["Preis"].replace("*", "").replace(" ", "").replace("€", "").replace("$", "").replace(",", ".")
        book_data["ISBN-13"] = book_data["ISBN-13"].replace(" ", "")
        book_data["ISBN-10"] = book_data["ISBN-10"].replace(" ", "")

        title = book_data.get("Title", "")
        isbn = book_data.get("ISBN-13", "")
        if not isbn:
            isbn = book_data.get("ISBN-10", "")

        book_data["Bild"] = f"{title[:20].replace(' ', '')}_{isbn.replace('-', '')}.png"
    except Exception as e:
        print(f"Error in cleanup: {e}")

# Limit Requests to 2 per Min
MIN_REQUEST_INTERVAL = 30  # in Seconds
_last_request_time = 0

def wait_if_needed():
    global _last_request_time
    now = time.time()
    last_request_difference = now - _last_request_time

    if last_request_difference < MIN_REQUEST_INTERVAL:
        sleep_time = MIN_REQUEST_INTERVAL - last_request_difference
        print(f"Rate limit active. Waiting {sleep_time:.1f}s...")
        time.sleep(sleep_time)
    _last_request_time = time.time()


def get_ISBN_data(ISBN):
    wait_if_needed()
    book_data.clear()
    if not search(driver, ISBN):
        driver.quit()
        return {"error": "Failed to find the search box element"}
    get_titel()
    get_ISBNtabel_data()
    get_beschreibung()
    get_genre()
    data_cleanup()
    save_cover()

    # Ensure the WebDriver is closed when the script exits
    import atexit
    atexit.register(driver.quit)

    return(book_data)


#Testdata:
#book_data = get_ISBN_data("978-3-608-98701-0")
#print(book_data)
#
##visual test of get_ISBN_data
#for key, value in book_data.items():
#    print(f"{key}: {value}")
#
#Title: Der Herr der Ringe
#In der überarbeiteten Übersetzung von Wolfgang Krege | Filmausgabe zur Serie Die Ringe der Macht
#von J.R.R. Tolkien, aus dem Englischen übersetzt von Wolfgang Krege Der Herr der Ringe In der überarbeiteten Übersetzung von Wolfgang Krege | Filmausgabe zur Serie Die Ringe der Macht
#Url: https://www.isbn.de/buch/9783608987010/der-herr-der-ringe
#Einband: Softcover
#Laenge: 1568 Seiten
#Jahr: 2022
#Auflage: 1
#Verlag: Klett-Cotta
#Autor: J.R.R. Tolkien
#erschienen am: 02.09.2022
#ISBN-10: 3-608-98701-0
#ISBN-13: 978-3-608-98701-0
#Maße: 19,5 12,5 1201 gr
#Lieferstatus: verfügbar
#Preis: 35.00
#Beschreibung: »Ein Ring, sie zu knechten, sie alle zu finden, ins Dunkel zu treiben und ewig zu binden.« Dreibändige Ausgabe zur Serienverfilmung Vor unvordenklichen Zeiten wurden die Ringe der Macht von den Elben geschaffen und Sauron, der Dunkle Herrscher, schmiedete heimlich den Einen Ring und füllte ihn mit seiner Macht, auf dass er über alle anderen Ringe und ihre Träger gebieten konnte. Der Eine Ring wurde Sauron im Lauf der Zeit genommen und so sehr er ihn auch in ganz Mittelerde suchte, er blieb dennoch für ihn verloren. Zeitalter später fällt der Ring in die Hände des Hobbits Bilbo Beutlin, der ihn an seinen Neffen Frodo weitergibt … und so beginnt das größte und gefährlichste Abenteuer der Fantasyliteratur. Im ersten Band »Die Gefährten« bekommt der junge Frodo in einem ruhigen Dorf im Auenland ein Geschenk, das sein Leben für immer verändern wird – den Einen Ring, der seit Jahrhunderten als verschollen galt. Ein mächtiges und furchterregendes Ding, mit dem der Dunkle Herrscher einst Mittelerde versklavte. Nun erhebt sich die Dunkelheit erneut, und Frodo muss tief in das Reich des Dunklen Herrschers vordringen, bis zu dem einzigen Ort, an dem der Ring zerstört werden kann: dem Schicksalsberg. Die Reise wird Frodos Mut, seine Freundschaften und sein Herz auf die Probe stellen. Denn der Ring korrumpiert alle, die ihn tragen. Kann Frodo den Ring vernichten, bevor der Ring ihn vernichtet? In »Die zwei Türme« , dem zweiten Band, sind die Gefährten verstreut. Einige bereiten sich auf den Krieg gegen den Dunklen Herrscher vor, einige stellen sich dem Verrat des verderbten Zauberers Saruman entgegen. Nur Frodo und Sam sind übrig, um den verfluchten Ring in den Feuern des Schicksalsberges zu vernichten. Der Schicksalsberg liegt im Herzen des Reiches des Dunklen Herrschers. Ihr einziger Führer auf der gefährlichen Reise dorthin ist Gollum, eine hinterlistige und besessene Kreatur, die einst den Ring besaß und sich entsetzlich danach sehnt, ihn wieder zu kriegen. Als sich die dunklen Mächte sammeln, liegt das Schicksal von Mittelerde in den Händen von zwei einsamen Hobbits. Wird Gollum sie in den Tod führen? Im dritten und letzten Band »Die Rückkehr des Königs« ist der Dunkle Herrscher auferstanden. Und während er Horden von Orks entfesselt, um ganz Mittelerde zu unterwerfen, kämpfen sich Frodo und Sam tief in sein Reich nach Mordor vor. Um Sauron zu besiegen, muss der Eine Ring in den Feuern des Schicksalsberges vernichtet werden. Doch der Weg dorthin ist unvorstellbar schwer, und Frodos Kräfte schwinden. Der Ring macht sich alle, die ihn tragen, untertan und Frodo bleibt kaum noch Zeit. Werden Sam und Frodo ihr Ziel erreichen, oder wird der Dunkle Herrscher am Ende wieder über ganz Mittelerde herrschen?
#Genre: Epische Fantasy (High Fantasy)
#Erscheinungsdatum: 02.09.2022
#Bild: DerHerrderRingeIn_9783608987010.png