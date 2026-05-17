# ---------------------------------------------------------------
# User Story 3: Hantera favoritlistan
# Som bokslukare vill jag att favoritlistan uppdateras vid markering
# eller avmarkering av favorit så att jag ser en aktuell lista över mina val.
#
# Acceptanskriterier:
# AK 3.1: En favoritmarkerad bok ska läggas till i favoritlistan.
# AK 3.2: Dubbletter av samma bok ska förhindras i listan.
# AK 3.3: En avmarkerad bok ska tas bort från favoritlistan.
# AK 3.4: Endast giltiga bokobjekt ska accepteras i listan.
# ---------------------------------------------------------------

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


def test_add_book(favorite_list, book):
    """Testar AK 3.1: En favoritmarkerad bok ska läggas till i
    favoritlistan."""
    # Act
    favorite_list.add(book)

    # Assert
    assert book in favorite_list.favorites
    assert len(favorite_list.favorites) == 1


def test_add_same_book_again(favorite_list, book):
    """Testar AK 3.2: Dubbletter av samma bok ska förhindras i listan."""
    # Act
    favorite_list.add(book)
    favorite_list.add(book)

    # Assert
    assert book in favorite_list.favorites
    assert len(favorite_list.favorites) == 1


def test_remove_book(favorite_list, book):
    """Testar AK 3.3: En avmarkerad bok ska tas bort från favoritlistan."""
    # Act
    favorite_list.add(book)
    favorite_list.remove(book)

    # Assert
    assert book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0


def test_add_invalid_book(favorite_list):
    """Testar AK 3.4: Endast giltiga bokobjekt ska accepteras i listan."""
    # Act
    invalid_book = ("inte en bok", "George R.R. Martin",
            "The Developer Who Knew Nothing")
    favorite_list.add(invalid_book)

    # Assert
    assert invalid_book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0
