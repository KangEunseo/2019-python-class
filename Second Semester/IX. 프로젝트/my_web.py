#유튜브 영상 순위
# from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # with urlopen("https://www.youtube.com/feed/trending") as response:
    #     soup = BeautifulSoup(response, "lxml")

    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    video_titles = soup.findAll("a", attrs={'class':'yt-uix-tile-link'})
    print("[ 유튜브 실시간 인기 동영상 Top30 ]")
    n = 1
    for video_title in video_titles[:30]:
        print(str(n) + ". " + video_title.text + "\n\thttps://www.youtube.com/" + video_title["href"])
        n += 1