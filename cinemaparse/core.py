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

#MSK_PARSER = CinemaParser('msk')
#print(MSK_PARSER.get_films_list())
# MSK_PARSER.print_raw_content()
