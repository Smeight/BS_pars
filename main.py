import requests
from bs4 import BeautifulSoup

url = input("Введите URL сайта для парсинга: ")

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Парсинг заголовков новостей
news_headlines = []
for headline in soup.find_all('h3', class_='news__item-title'):
    news_headlines.append(headline.text.strip())

# Парсинг дат новостей
news_dates = []
for date in soup.find_all('time', class_='news__item-date'):
    news_dates.append(date.text.strip())

# Вывод результатов парсинга
for i in range(len(news_headlines)):
    print("Новость " + str(i+1) + ":")
    print("Заголовок: " + news_headlines[i])
    print("Дата: " + news_dates[i])
    print("\n")
