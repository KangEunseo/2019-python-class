from bs4 import BeautifulSoup       #html 구조적으로 변환하기
from urllib.request import urlopen  #url에 해당하는 html 가져오기

if __name__ == '__main__':
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=sat")
    soup = BeautifulSoup(data, "lxml")

    cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title">
    html = "<html><head><meta charset='utf-8'></head><body>"
    for title in cartoon_titles:
        t = title.find('a').text            #제목
        link = "http://comic.naver.com/" + title.find('a').get('href')  #링크
        html += "<a href=%s>%s</a><br>" % (link, t)
    html += "</body></html>"
    output = BeautifulSoup(html, "lxml")    #htmlstring -> BeautifulSoup 객체
    prettyHtml = str(output.prettify())     #html 줄 예쁘게

    with open("cellsOfYumi.html", mode="w", encoding="utf-8") as f:
        f.write(prettyHtml)