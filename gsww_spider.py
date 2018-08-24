import requests
import re


# 爬取页面，解析页面数据
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text

    # 提取数据
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', html, re.DOTALL)  # 标题  re.S和re.DOTALL可以让.匹配到\n
    dynasties = re.findall(r'<p class="source">.*?<a .*?>(.*?)</a>', html, re.DOTALL)  # 朝代
    authors = re.findall(r'<p class="source">.*?<a .*?>.*?<a .*?>(.*?)</a>', html, re.DOTALL)  # 作者
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>', html, re.DOTALL)  # 诗词内容
    contents = []  # 存放诗词内容
    for content in content_tags:
        x = re.sub('<.*?>', "", content)
        contents.append(x.strip())

    poems = []  # 存放爬取到的完整的诗词
    # 将所有的数据组合到一起形成一个字典
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)
        print(poem)
        print("=" * 30)


# 要爬取的页面url
def main():
    for x in range(1, 11):
        url = 'https://www.gushiwen.org/default_%s.aspx' % x
        parse_page(url)


if __name__ == '__main__':
    main()
