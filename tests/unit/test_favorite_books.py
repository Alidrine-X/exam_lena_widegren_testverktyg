import pytest

from src.bookstore.book import Book
from src.bookstore.favorite_books import FavoriteBooks


@pytest.fixture
def favorite_list():
    return FavoriteBooks()


@pytest.fixture
def book():
    return Book(105, "Microslop Browserdóttir",
                "Playwright: Click It Till You Make It")


# Testa att markera bok som favorit
def test_add_book(favorite_list, book):
    # Act
    favorite_list.add(book)

    # Assert
    assert book in favorite_list.favorites
    assert len(favorite_list.favorites) == 1


# Testa att favoritmarkera bok som redan finns som favorit
def test_add_same_book_again(favorite_list, book):
    # Act
    favorite_list.add(book)
    favorite_list.add(book)

    # Assert
    assert book in favorite_list.favorites
    assert len(favorite_list.favorites) == 1


# Testa att avmarkera bok som favorit
def test_remove_book(favorite_list, book):
    # Act
    favorite_list.add(book)
    favorite_list.remove(book)

    # Assert
    assert book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0


# Testa att favoritmarkera en icke-bok
def test_add_invalid_book(favorite_list):
    # Act
    book = ("inte en bok", "George R.R. Martin", "The Developer Who Knew Nothing")
    favorite_list.add(book)

    # Assert
    assert book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0
