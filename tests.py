import pytest

from main import BooksCollector

ALLOWED_BOOKS_NAMES = ['A', 'B2', 'C' * 20, 'D' * 39, 'F' * 40, '     ', '$\'\"#?*@%!&>.<,=+~`-_()']
INVALID_BOOKS_NAMES = ['', 'N' * 41, 'E' * 42, 'T' * 100]
INVALID_GENRE = ['genre_1', 'genre_2', 'genre_3']


class TestBooksCollector:
       
    def test_init_none_books_collector_object(self, collector_empty):
        assert collector_empty.__dict__ == {'books_genre': {}, 'favorites': [], 'genre': ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'], 'genre_age_rating': ['Ужасы', 'Детективы']}

    @pytest.mark.parametrize('name', ALLOWED_BOOKS_NAMES)
    def test_add_new_book_allowed_book_name_new_book_in_books_genre(self, name, collector_empty):
        collector_empty.add_new_book(name)
        assert name in collector_empty.books_genre
    
    @pytest.mark.parametrize('name', INVALID_BOOKS_NAMES)
    def test_add_new_book_not_allowed_book_name_new_book_not_added(self, name, collector_empty):
        collector_empty.add_new_book(name)
        assert name not in collector_empty.books_genre

    def test_add_new_book_has_empty_genre_by_default(self, collector_empty):
        collector_empty.add_new_book('Новая книга')
        assert collector_empty.books_genre.get('Новая книга') == ''

    def test_add_new_book_duplicate_one_added(self, collector_empty):
        collector_empty.add_new_book('Дубликат')
        collector_empty.add_new_book('Дубликат')
        assert len(collector_empty.books_genre) == 1

    def test_set_book_genre_valid(self, collector_empty):
        collector_empty.add_new_book('Научиться писать автотесты без слёз')
        collector_empty.set_book_genre('Научиться писать автотесты без слёз', 'Фантастика')
        assert collector_empty.books_genre.get('Научиться писать автотесты без слёз') == 'Фантастика'

    def test_set_book_genre_invalid_genre_book_genre_not_found_genre(self, collector_empty):
        collector_empty.add_new_book('Успеть сдать проект за 60 секунд')
        collector_empty.set_book_genre('Успеть сдать проект за 60 секунд', 'Классика')
        assert collector_empty.books_genre.get('Успеть сдать проект за 60 минут') is None

    def test_set_book_genre_invalid_book_genre_not_added(self, collector_empty):
        collector_empty.set_book_genre('Книга, которой нет в словаре', 'Ужасы')
        assert 'Ужасы' not in collector_empty.books_genre.values()

    def test_get_book_genre_valid(self, collector_full):
        assert collector_full.get_book_genre('Оно') == 'Ужасы'

    def test_get_book_genre_invalid_book_not_found_genre(self, collector_full):
        assert collector_full.get_book_genre('Книга, которой нет в словаре') is None

    def test_get_book_genre_new_book_genre_contains_empty_string(self, collector_full):
        assert collector_full.get_book_genre('Ново-добавленная книга') == ''

    def test_get_books_with_specific_genre_valid(self, collector_full):
        assert collector_full.get_books_with_specific_genre('Ужасы') == ['Кошмар на улице Вязов', 'Оно']

    @pytest.mark.parametrize('genre', INVALID_GENRE)
    def test_get_books_with_specific_genre_invalid_genre_empty_list(self, genre, collector_full):
        assert collector_full.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_not_genre_empty_list(self, collector_full):
        assert collector_full.get_books_with_specific_genre('') == []

    def test_get_books_genre_valid_completed_dictionary(self, collector_full):
        assert collector_full.get_books_genre() == collector_full.books_genre

    def test_get_books_genre_valid_empty_dictionary(self, collector_empty):
        assert collector_empty.get_books_genre() == {}

    def test_get_books_for_children_valid_filtered_list(self, collector_full):
        assert collector_full.get_books_for_children() == ['Назад в будущее', 'Ну, погоди!', 'Двенадцать стульев']

    def test_add_book_in_favorites_valid_added_favorites_in_list(self, collector_full):
        collector_full.add_book_in_favorites('Оно')
        assert collector_full.favorites == ['Оно']

    def test_add_book_in_favorites_not_books_empty_list(self, collector_full):
        collector_full.add_book_in_favorites('Книга, которой нет в словаре')
        assert collector_full.favorites == []

    def test_delete_book_from_favorites_valid_deleted_book_is_missingin_list(self, collector_full):
        collector_full.add_book_in_favorites('Оно')
        collector_full.add_book_in_favorites('Ну, погоди!')
        collector_full.delete_book_from_favorites('Оно')
        assert collector_full.favorites == ['Ну, погоди!']

    def test_delete_book_from_favorites_not_books_favorites_empty_list(self, collector_full):
        collector_full.delete_book_from_favorites('Оно')
        assert collector_full.favorites == []

    def test_get_list_of_favorites_books_valid_favorites_books_is_list(self, collector_full):
        collector_full.add_book_in_favorites('Оно')
        collector_full.add_book_in_favorites('Ну, погоди!')
        assert collector_full.get_list_of_favorites_books() == ['Оно', 'Ну, погоди!']

    def test_get_list_of_favorites_books_not_books_favorites_empty_list(self, collector_full):
        assert collector_full.get_list_of_favorites_books() == []
