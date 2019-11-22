from bs4 import BeautifulSoup       #html 구조적으로 변환하기
from urllib.request import urlopen  #url에 해당하는 html 가져오기

if __name__ == '__main__':
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=sat")
    soup = BeautifulSoup(data, "lxml")

    cartoon_titles = soup.find_all("td", attrs={'class':'title'})
    for title in cartoon_titles:
        t = title.find('a').text
        print(t)

    # data = urlopen("http://webtoon.daum.net/webtoon/view/guricomeback")
    # soup = BeautifulSoup(data, "lxml")
    #
    # cartoon_titles = soup.find_all("strong", attrs={'class': 'tit_wt'})
    # for title in cartoon_titles:
    #     print(title)