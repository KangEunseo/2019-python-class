from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/yearly") as response:
        soup = BeautifulSoup(response, "lxml")

    # print(soup)
    movie_titles = soup.findAll("a", attrs={"class":"link_g"})
    print("< 다음 영화 연간 박스오피스 >")
    n = 1
    for movie_title in movie_titles[2:]:
        print(n, movie_title.text)
        n += 1