import pytest

from main import BooksCollector

@pytest.fixture()
def collector_empty():
    collector_empty = BooksCollector()
    return collector_empty

@pytest.fixture
def collector_full():
     collector_full = BooksCollector()
     collector_full.books_genre = {'Назад в будущее': 'Фантастика',
                'Кошмар на улице Вязов': 'Ужасы', 
                'Приключения Шерлока Холмса': 'Детективы', 
                'Ну, погоди!': 'Мультфильмы',
                'Двенадцать стульев': 'Комедии',
                'Оно': 'Ужасы',
                'Ново-добавленная книга': ''}
     return collector_full
