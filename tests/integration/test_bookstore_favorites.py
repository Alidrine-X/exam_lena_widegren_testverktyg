from src.bookstore.bookstore import BookStore
from src.bookstore.favorite_books import FavoriteBooks


# Testa att lägga till en bok som favorit
def test_add_to_favorites():
    # Arrange
    bookstore = BookStore()
    favorite_list = FavoriteBooks()

    book_id = 100
    author = "Guido van Rossum"
    title = "Ormar på ett plan: En Python-berättelse"

    # Act
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
def test_remove_from_favorites():
    # Arrange
    bookstore = BookStore()
    favorite_list = FavoriteBooks()

    book_id = 102
    author = "Dave Thomasson"
    title = "The Pragmatic Procrastinator"

    bookstore.add_book(book_id, author, title)
    bookstore.toggle_favorite(book_id)

    book = bookstore.get_book(book_id)
    favorite_list.add(book)

    # Act
    bookstore.toggle_favorite(book_id)
    favorite_list.remove(book)

    # Assert
    # Kontrollera att boken är borta som favorit i båda listorna
    assert book.favorite is False
    assert book not in favorite_list.favorites
    assert len(favorite_list.favorites) == 0
