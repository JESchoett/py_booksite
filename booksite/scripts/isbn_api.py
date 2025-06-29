#https://developers.google.com/books/docs/v1/using?hl=de
import requests

def get_book_info_by_isbn(isbn):
    """
    Calls the Google Books API using an ISBN to retireive book information.

    Args:
        isbn: The ISBN of the Book to search.

    Returns:
        A Dictionary containing: ....
    """
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": f"isbn:{isbn}"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        return_data = {}
        # TODO prüfe alle return daten auf interessante Informationen
        if data and 'items' in data:
            for item in data['items']:
                if item["volumeInfo"].get("title") and not return_data.get("titl"):
                    return_data["titl"] = item["volumeInfo"]["title"]

                if item["volumeInfo"].get("subtitle"):
                    if not return_data.get("subtitle"):
                        return_data["subtitle"] = item["volumeInfo"]["subtitle"]
                    else:
                        return_data["subtitle"] += item["volumeInfo"]["subtitle"]

                if item["volumeInfo"].get("authors") and not return_data.get("autor"):
                    return_data["autor"] = item["volumeInfo"]["authors"]

                if item["volumeInfo"].get("publishedDate") and not return_data.get("jahr"):
                    return_data["jahr"] = item["volumeInfo"]["publishedDate"][:4]

                if item["volumeInfo"].get("pageCount") and not return_data.get("seiten"):
                    return_data["seiten"] = item["volumeInfo"]["pageCount"]

                if item["volumeInfo"].get("previewLink") and not return_data.get("url"):
                    return_data["url"] = item["volumeInfo"]["previewLink"]

        else:
            print(f"ISBN {isbn} not in Google Book API.")
            return (f"Kein Buch mit der ISBN {isbn} gefunden.")

        return return_data

    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der API-Anfrage: {e}")
        return "Fehler bei der Google API-Anfrage: {e}"

def use_api():
    """
    Example usage of the get_book_info_by_isbn function.
    """
    isbn_to_search = "978-3-608-98701-0"
    book_info = get_book_info_by_isbn(isbn_to_search)

    if book_info:
        print(book_info)

def get_book_info_by_isbn_example():
    data_of_request = {'title': 'Der Herr der Ringe', 'subtitle': 'Band 1-3', 'authors': ['J. R. R. Tolkien'], 'publishedDate': '2022-09-02', 'industryIdentifiers': [{...}, {...}], 'readingModes': {'text': False, 'image': False}, 'pageCount': 1568, 'printType': 'BOOK', 'maturityRating': 'NOT_MATURE', 'allowAnonLogging': False, 'contentVersion': 'preview-1.0.0', 'panelizationSummary': {'containsEpubBubbles': False, 'containsImageBubbles': False}, 'language': 'de', 'previewLink': 'http://books.google.de/books?id=NlIdzwEACAAJ&dq=isbn:978-3-608-98701-0&hl=&cd=1&source=gbs_api', 'infoLink': 'http://books.google.de/books?id=NlIdzwEACAAJ&dq=isbn:978-3-608-98701-0&hl=&source=gbs_api', 'canonicalVolumeLink': 'https://books.google.com/books/about/Der_Herr_der_Ringe.html?hl=&id=NlIdzwEACAAJ'}
    data_of_request2 = {'title': 'Der Herr der Ringe', 'subtitle': 'In der überarbeiteten Übersetzung von Wolfgang Krege | Filmausgabe zur Serie Die Ringe der Macht', 'authors': ['J. R. R. Tolkien'], 'publishedDate': '2022-09-02', 'industryIdentifiers': [{...}, {...}], 'readingModes': {'text': False, 'image': False}, 'pageCount': 0, 'printType': 'BOOK', 'maturityRating': 'NOT_MATURE', 'allowAnonLogging': False, 'contentVersion': 'preview-1.0.0', 'panelizationSummary': {'containsEpubBubbles': False, 'containsImageBubbles': False}, 'language': 'de', 'previewLink': 'http://books.google.de/books?id=Zrg_0QEACAAJ&dq=isbn:978-3-608-98701-0&hl=&cd=2&source=gbs_api', 'infoLink': 'http://books.google.de/books?id=Zrg_0QEACAAJ&dq=isbn:978-3-608-98701-0&hl=&source=gbs_api', 'canonicalVolumeLink': 'https://books.google.com/books/about/Der_Herr_der_Ringe.html?hl=&id=Zrg_0QEACAAJ'}

    for key, value in data_of_request.items():
        print(f"{key}: {value}")
    print("\n---\n")
    for key, value in data_of_request2.items():
        print(f"{key}: {value}")

# Example data to simulate the response from the Google Books API
def main():
    user_input = input("use api or example? ([1] api/[2]example): ")
    if user_input == "1":
        use_api()
    else:
        get_book_info_by_isbn_example()

if __name__ == "__main__":
    main()