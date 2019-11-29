#다음 웹툰 > 어쩌다 발견한  7월
from urllib import response
from urllib.request import urlopen

import json

if __name__ == '__main__':
    # response = urlopen("http://webtoon.daum.net/data/pc/webtoon/view/findjuly")
    # response_byte = response.read()
    # response_json = json.loads(response_byte)

    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/findjuly") as data:
        response_byte=response.read()
    response_json = json.loads(response_byte)
    #print(json.loads(response.read()))
   # print(response_json['data']['webtoon']['webtoonEpisodes'][11]['title'])

    cartoon_titles = response_json['data']['webtoon']['webtoonEpisodes']
    for item in cartoon_titles:
        title=item['title']
        thumbnail = item['thumbnailImage']['url']
        print(title)
        print(thumbnail)