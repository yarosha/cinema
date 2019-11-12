"""Модуль содержит Class CinemaParser"""
import requests
from bs4 import BeautifulSoup
class CinemaParser():
    """Класс работает с фильмами"""
    def __init__(self, city="msk"):
        """Присваеваем город"""
        self.city = city
        self.beauty = []
        self.content = []

    def extract_raw_content(self):
        """Содержимое страницы"""
        response = requests.get(url='https://' + self.city + '.subscity.ru')
        self.content = response.text

    def print_raw_content(self):
        """Возвращение содержимого"""
        self.extract_raw_content()
        self.beauty = BeautifulSoup(self.content, 'html.parser')
        print(self.beauty.prettify())

    def get_films_list(self):
        """Возвращение списка фильмов"""
        self.extract_raw_content()
        self.beauty = BeautifulSoup(self.content, 'html.parser')
        films = []
        all_films = self.beauty.find_all("div", class_='movie-plate')
        for i in all_films:
            films.append(i["attr-title"])
        return films
    def get_films_nearest_session(self, film):
        """Ближайшее время сеанса сегодня"""
        self.extract_raw_content()
        self.get_films_list()
        beauty = BeautifulSoup(self.content, 'html.parser')
        names = beauty.find_all(class_ = 'movie-plate')
        for name in names:
            if name.get('attr-title') == film
            url = 'https://subscity/subscity/' + self.city + name.find('a').get('href')
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            cinemas = soup.find_all(class_ = 'row-entity')
            time_cinema = {}
            for cinema in cinemas:
                for cur_time in cinema.find_all(class_= 'text-center cell-screenings'):
                    cur_time = int(cur_time.get('attr-time'))
                    name = cinema.find(class_='underdashed').text
                    if time.time() < cur_time:
                        time_cinema[cur_time + 3600*3] = name
            time_cinema = sorted(time_cinema.items(), key = lambda key: key[0]
            earliest = datetime.utcfromtimestamp(time_ciema[0][0])
            now = datetime.today().strftime('%x')
            if earliest.strftime('%x') != now or len(time_cinema) == 0:
                return None, None
            return time_cinema[0][1], earliest.strftime('%H:%M')
        return None, None
            
                
