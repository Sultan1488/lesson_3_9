import bs4 as bs
import requests
import pandas as pd


class Writer:
    def __init__(self, advertisement):
        self.ads = pd.DataFrame(
            {'title': advertisement.titles,
             'link': advertisement.links,
             'category': advertisement.categories,
             }
        )

    def write_to_csv(self):
        csvFileContents = self.ads.to_csv(index=False)
        with open("kivano.csv", "a", encoding='utf-8') as f:
            f.write(csvFileContents)


class Advertisements:
    def __init__(self, products):
        self.products = products
        self.titles = []
        self.links = []
        self.categories = []

        for product in products:
            self.titles.append(product.title)
            self.links.append(product.link)
            self.categories.append(product.category)


class Product:
    def __init__(self, title, link, category):
        self.title = title
        self.link = link
        self.category = category


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = bs.BeautifulSoup(html, 'html.parser')
    pages = soup.find('ul', class_='pagination').find_all('a')[2].get('href')
    total_pages = pages.split('=')[1]
    return int(total_pages)


def get_data_1():
    base_url = 'https://www.kivano.kg/kompyutery?'
    url = 'https://www.kivano.kg/kompyutery?page=1'
    page_part = 'page='
    total_page = get_total_pages(get_html(url))
    products = []

    for i in range(1, total_page + 1):
        urls = base_url + page_part + str(i)
        html = get_html(urls)
        soup = bs.BeautifulSoup(html, 'html.parser')

        category = soup.find('ul', class_='breadcrumb2').find_all('li')[1].a.text
        ads = soup.find('div', class_='list-view').find_all('div', class_='item')

        for ad in ads:
            common_list = []
            title = ad.find('div', class_='listbox_title')
            link = ad.find('div', class_='listbox_title').a.get('href')
            common_list.append(title.text.replace('\n', ''))
            common_list.append('https://www.kivano.kg' + link)
            common_list.append(category)
            products.append(Product(common_list[0], common_list[1], common_list[2]))
    return products
get_data_1()

def get_data_2():
    base_url = 'https://www.kivano.kg/avtotovary?'
    url = 'https://www.kivano.kg/avtotovary?page=1'
    page_part = 'page='
    total_page = get_total_pages(get_html(url))
    products = []

    for i in range(1, total_page + 1):
        urls = base_url + page_part + str(i)
        html = get_html(urls)
        soup = bs.BeautifulSoup(html, 'html.parser')

        category = soup.find('ul', class_='breadcrumb2').find_all('li')[1].a.text
        ads = soup.find('div', class_='list-view').find_all('div', class_='item')

        for ad in ads:
            common_list = []
            title = ad.find('div', class_='listbox_title')
            link = ad.find('div', class_='listbox_title').a.get('href')
            common_list.append(title.text.replace('\n', ''))
            common_list.append('https://www.kivano.kg' + link)
            common_list.append(category)
            products.append(Product(common_list[0], common_list[1], common_list[2]))
    return products
get_data_2()


def get_data_3():
    base_url = 'https://www.kivano.kg/elektronika?'
    url = 'https://www.kivano.kg/elektronika?page=1'
    page_part = 'page='
    total_page = get_total_pages(get_html(url))
    products = []

    for i in range(1, total_page + 1):
        urls = base_url + page_part + str(i)
        html = get_html(urls)
        soup = bs.BeautifulSoup(html, 'html.parser')

        category = soup.find('ul', class_='breadcrumb2').find_all('li')[1].a.text
        ads = soup.find('div', class_='list-view').find_all('div', class_='item')

        for ad in ads:
            common_list = []
            title = ad.find('div', class_='listbox_title')
            link = ad.find('div', class_='listbox_title').a.get('href')
            common_list.append(title.text.replace('\n', ''))
            common_list.append('https://www.kivano.kg' + link)
            common_list.append(category)
            products.append(Product(common_list[0], common_list[1], common_list[2]))
    return products
get_data_3()


def get_data_4():
    base_url = 'https://www.kivano.kg/odezhda-i-aksessuary?'
    url = 'https://www.kivano.kg/odezhda-i-aksessuary?page=1'
    page_part = 'page='
    total_page = get_total_pages(get_html(url))
    products = []

    for i in range(1, total_page + 1):
        urls = base_url + page_part + str(i)
        html = get_html(urls)
        soup = bs.BeautifulSoup(html, 'html.parser')

        category = soup.find('ul', class_='breadcrumb2').find_all('li')[1].a.text
        ads = soup.find('div', class_='list-view').find_all('div', class_='item')

        for ad in ads:
            common_list = []
            title = ad.find('div', class_='listbox_title')
            link = ad.find('div', class_='listbox_title').a.get('href')
            common_list.append(title.text.replace('\n', ''))
            common_list.append('https://www.kivano.kg' + link)
            common_list.append(category)
            products.append(Product(common_list[0], common_list[1], common_list[2]))
    return products
get_data_4()

if __name__ == '__main__':
    advertisements_1 = Advertisements(get_data_1())
    advertisements_2 = Advertisements(get_data_2())
    advertisements_3 = Advertisements(get_data_3())
    advertisements_4 = Advertisements(get_data_4())


    writer_1 = Writer(advertisements_1)
    writer_2 = Writer(advertisements_2)
    writer_3 = Writer(advertisements_3)
    writer_4 = Writer(advertisements_4)

    writer_list = [writer_1, writer_2, writer_3, writer_4]
    for writer in writer_list:
        writer.write_to_csv()
