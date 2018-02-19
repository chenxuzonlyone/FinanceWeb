import requests
from bs4 import BeautifulSoup


def web_spider(max_pages):
    page = 1
    character = 'a'
    while page <= max_pages:
        url = 'https://www.investopedia.com/terms/a/aaa.asp'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        # for link in soup.findAll('a', {'class': 'brand nav-link'}):
        #     data_content_type = link.get('data-content-type')
        #     print(data_content_type)
        for link in soup.findAll('div', {'class': 'content-box content-box-term'}):
            data = link.findAll('p')
            string = data[0]
            print(string)
        page += 1


web_spider(1)
