import requests
import os
import bs4


def main():
    host = 'http://www.baidu.com'
    url = host + '/test/'

    end = 2
    i = 1
    print('page %s' % url)
    res = requests.get(url)
    res.raise_for_status()
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    # 获取链接
    urlList = soup.select('.pic-150 li a')
    for u in urlList:
        url = u.get('href')
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = 'utf-8'
        uSoup = bs4.BeautifulSoup(res.text, features="html.parser")
        # 获取图片
        imageUrlList = uSoup.select('.art-main img')
        for img in imageUrlList:
            imageUrl = img.get('src')
            print('image url %s' % imageUrl)
            # 下载图片
            download_gif(imageUrl)

    print(urlList)


def download_gif(url):
    res = requests.get(url)
    image_file = open(os.path.join('image', os.path.basename(url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


if __name__ == '__main__':
    main()
