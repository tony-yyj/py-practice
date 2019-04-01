import requests
import re
from requests.exceptions import RequestException


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>'
                         r'.*?poster-default.*?src="(.*?)"'
                         r'.*?name"><a.*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'thumb': item[1],
            'name': item[2],
        }


def download_thumb(name, url):
    try:
        response = requests.get(url)
        with open('thumb/' + name + '.jpg', 'wb') as f:
            f.write(response.content)
            print('电影封面下载完毕')
            print('-----')
    except RequestException as e:
        print(e)


def main():
    url = 'https://maoyan.com/board'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        download_thumb(item['name'], item['thumb'])


if __name__ == '__main__':
    main()
