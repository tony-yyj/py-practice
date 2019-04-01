# coding=utf-8
import requests
import os
import bs4

host = 'http://www.baidu.com'

url = host +'/a/201904/22746.html'

i = 0

end = 20
while i < end:
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    img = soup.select('#content img')
    print('img %s' % img)
    if img:
        imageUrl = 'http:' + img[0].get('src')
        print('imageUrl %s' % imageUrl)

        res = requests.get(imageUrl)
        imageFile = open(os.path.join('image', os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()
    else:
        print('Not find img ')

    link = soup.select('.pages_y a')
    print('link %s' % link)
    if link:
        url = host + link[0].get('href')
    else:
        print('Not link')
        i = 999

    i = i + 1


print('Done')