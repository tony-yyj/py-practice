import requests
import os
import bs4

url = 'https://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # 下载网页
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    # 找到漫画的url
    comicElem = soup.select('#comic img')
    if comicElem:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s ...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')

    else:
        print('Count not find comic image.')


print('Done')


