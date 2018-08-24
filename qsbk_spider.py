# 爬取糗事百科文字页面的所有段子
import re
import requests


# 爬取段子信息
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text

    # 爬取段子内容
    contents_tag = re.findall('<div class="content">.*?<span>(.*?)</span>', html, re.DOTALL)  # 段子
    paragraph = {}  # 存放段子信息
    for index,content in enumerate(contents_tag):
        x = re.sub('<.*?>', "", content)
        title = '段子{}'.format(index)
        paragraph[title] = x.strip()
    # print(paragraph)
    return paragraph


def main():
    paragraphs = []  # 存放10页的段子信息
    for x in range(1, 11):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(x)
        paragraph = parse_page(url)
        paragraphs.append(paragraph)
    print(paragraphs)


if __name__ == '__main__':
    main()
