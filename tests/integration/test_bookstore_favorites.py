import pytest
from src.bookstore.bookstore import BookStore
from src.bookstore.favorite_books import FavoriteBooks


@pytest.fixture
def bookstore():
    return BookStore()


@pytest.fixture
def favorite_list():
    return FavoriteBooks()


@pytest.fixture
def book_list():
    return [
        {"id": 100, "title": "Ormar på ett plan: En Python-berättelse",
         "author": "Guido van Rossum"},
        {"id": 102, "title": "The Pragmatic Procrastinator",
         "author": "Dave Thomasson"},
        {"id": 103, "title": "Python för folk som hatar ormar",
         "author": "Monty Pythonsson"},
        {"id": 104, "title": "Why Your Tests Are Lying to You",
         "author": "Kent Backdoor"},
        {"id": 105, "title": "Playwright: Click It Till You Make It",
         "author": "Microslop Browserdóttir"},
        {"id": 107, "title": "Git Blame and Other Ways to Lose Friends",
         "author": "Linus Torvalds"},
        {"id": 108, "title": "Learn Python in 21 Years",
         "author": "Sams Teachyourself"},
        {"id": 109, "title": "Agile Is a Feeling", "author": "Jeff Sutherland"},
        {"id": 110, "title": "Playwright: Waiting for Selectors",
         "author": "Samuel Barclay Beckett"},
        {"id": 111, "title": "Stack Overflow: A Love Story",
         "author": "Copy Pasta"},
        {"id": 112, "title": "My First Regex (And Last)",
         "author": "Larry Wallström"},
        {"id": 113, "title": "The Developer Who Knew Nothing",
         "author": "George R.R. Martin"},
        {"id": 115, "title": "The Bugs are Coming",
         "author": "George R.R. Martin"},
    ]


# Testa att lägga till en bok som favorit
def test_add_to_favorites(bookstore, favorite_list):
    # Arrange
    book_id = 100
    author = "Guido van Rossum"
    title = "Ormar på ett plan: En Python-berättelse"

    # Act
    # Lägg till bok och sätt som favorit
    bookstore.add_book(book_id, author, title)
    bookstore.toggle_favorite(book_id)

    book = bookstore.get_book(book_id)
    favorite_list.add(book)

    # Assert
    # Kontrollera att boken finns och är favorit i båda listorna
    assert book is not None
    assert book.favorite is True
    assert book in favorite_list.favorites
    assert len(favorite_list.favorites) == 1


# Testa att ta bort en bok från favoriter
def test_remove_from_favorites(bookstore, favorite_list):
    # Arrange
    book_id = 102
    author = "Dave Thomasson"
    title = "The Pragmatic Procrastinator"

    # Lägg till bok och sätt som favorit
    bookstore.add_book(book_id, author, title)
    bookstore.toggle_favorite(book_id)

    book = bookstore.get_book(book_id)
    favorite_list.add(book)

    # Act
    # Ta bort favoritmarkering från boken
    bookstore.toggle_favorite(book_id)
    favorite_list.remove(book)

    # Assert
    # Kontrollera att boken är borta som favorit i båda listorna
    assert book.favorite is False
    assert book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0


# Testar att antal böcker och antal favoritböcker stämmer
def test_bookstore_and_favorites(bookstore, favorite_list, book_list):
    # Arrange
    # Startar med 0 böcker och 0 favoriter
    assert bookstore.get_total_books() == 0
    assert favorite_list.get_favorite_count() == 0

    # Act 1 - Lägg till alla böcker till Läslistan
    for book in book_list:
        bookstore.add_book(book["id"], book["author"], book["title"])

    # Assert
    # Kontrollera att totala räknaren ökat till 13 böcker
    # Kontrollera att det är 0 favoriter
    assert bookstore.get_total_books() == 13
    assert favorite_list.get_favorite_count() == 0

    # Act 2 - Markera en av böckerna som favorit och lägg till i favoritlistan
    bookstore.toggle_favorite(100)
    book = bookstore.get_book(100)
    favorite_list.add(book)

    # Assert 2 - Kontrollera att både totalt antal och favoriter stämmer nu
    assert bookstore.get_total_books() == 13
    assert favorite_list.get_favorite_count() == 1


# Testfall 3: Statistik över totalt antal böcker och favoriter (User Story 4 & 5)
def test_bookstore_and_favorites_statistics(bookstore, favorite_list):
    # Arrange: Vi definierar två tydliga böcker
    book1_id, author1, title1 = 201, "Författare X", "Titel X"
    book2_id, author2, title2 = 202, "Författare Y", "Titel Y"

    # Act 1: Lägg till båda böckerna i bokhandeln
    bookstore.add_book(book1_id, author1, title1)
    bookstore.add_book(book2_id, author2, title2)

    # Assert 1: Kontrollera att det totala antalet nu är 2, men 0 favoriter
    assert bookstore.get_total_books() == 2
    assert favorite_list.get_favorite_count() == 0

    # Act 2: Gör Bok 1 till favorit och flytta över den till favoritlistan
    bookstore.toggle_favorite(book1_id)
    book1 = bookstore.get_book(book1_id)
    favorite_list.add(book1)

    # Assert 2: Slutgiltig kontroll av statistiken (2 böcker totalt och 1 favorit)
    assert bookstore.get_total_books() == 2
    assert favorite_list.get_favorite_count() == 1
