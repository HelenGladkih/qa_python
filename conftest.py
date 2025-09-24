import pytest

from main import BooksCollector

@pytest.fixture()
def collector_empty():
    return BooksCollector()

@pytest.fixture
def collector_full(collector_empty):
    books_data = {
        'Назад в будущее': 'Фантастика',
        'Кошмар на улице Вязов': 'Ужасы', 
        'Приключения Шерлока Холмса': 'Детективы',
        'Ну, погоди!': 'Мультфильмы',
        'Двенадцать стульев': 'Комедии',
        'Оно': 'Ужасы',
        'Ново-добавленная книга': ''
    }
    
    for name, genre in books_data.items():
        collector_empty.add_new_book(name)
        if genre:  # устанавливаем жанр только если он не пустой
            collector_empty.set_book_genre(name, genre)
    
    return collector_empty
