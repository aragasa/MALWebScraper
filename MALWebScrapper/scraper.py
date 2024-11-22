import requests
from bs4 import BeautifulSoup


def getAnime():
    
    url = 'https://myanimelist.net/anime/season'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    tv = soup.find_all('div', class_='js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')

    rawAniList = []

    for data in tv:
        title = data.find('a', class_='link-title').text
        #info = data.find('div', class_='info')
        genres = data.find('div', class_='genres js-genre').text
        
        scoremem = data.find('div', class_='scormem-container')
        
        score = scoremem.find('div').text

        members = scoremem.find('div', class_='scormem-item member').text

        rawAniList.append([title,genres,score,members])

    #aniList = []

    #for sub in rawAniList:
       #aniList.append(sub.replace('\n',' '))

    #print(aniList)
    return rawAniList
getAnime()
