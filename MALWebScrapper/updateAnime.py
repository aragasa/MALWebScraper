import schedule
import time
from scraper import getAnime
import csv

def makeCSV():

    filename = 'SeasonalAniList.csv'
    headers =['Title', 'Genres', 'Score', 'Members']

    with open(filename, 'w', newline='',encoding='utf-8') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(headers)
        csvWriter.writerows(getAnime())

makeCSV()

#schedule.every(90).days.do(makeCSV)

#while True:
    #schedule.run_pending()
    #time.sleep(1)