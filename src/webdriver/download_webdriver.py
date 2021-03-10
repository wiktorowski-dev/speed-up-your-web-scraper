from requests import get


def download():
    path = r'src/webdriver/'
    name = 'webdriver.zip'
    url = r'https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip'
    response = get(url)
    with open(f'{path}{name}', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    download()
