from src.bookstore.bookstore import BookStore


# Testa att lägga till bok som saknas i Läslistan
def test_add_book():
    # Arrange
    bookstore = BookStore()
    book_id = 115
    author = "George R.R. Martin"
    title = "The Bugs are Coming"

    # Act
    bookstore.add_book(book_id, author, title)
    new_book = bookstore.get_book(book_id)

    # Assert
    assert new_book.book_id == book_id
    assert new_book.author == author
    assert new_book.title == title


# Testa att markera boken som favorit
def test_mark_as_favorite():
    # Arrange
    bookstore = BookStore()
    book_id = 108
    author = "Sams Teachyourself"
    title = "Learn Python in 21 Years"
    bookstore.add_book(book_id, author, title)

    # Act: Sätt om till favorit (False -> True)
    new_favorite = bookstore.toggle_favorite(book_id)

    # Assert: Kontrollera att den blev True
    book = bookstore.get_book(book_id)
    assert new_favorite is True
    assert book.favorite is True


# Testa att avmarkera boken som favorit
def test_mark_as_not_favorite():
    # Arrange
    bookstore = BookStore()
    book_id = 111
    author = "Copy Pasta"
    title = "Stack Overflow: A Love Story"
    bookstore.add_book(book_id, author, title)
    bookstore.toggle_favorite(book_id)

    # Act: Sätt om till inte favorit (True -> False)
    not_favorite = bookstore.toggle_favorite(book_id)

    # Assert: Kontrollera att den blev False
    book = bookstore.get_book(book_id)
    assert not_favorite is True
    assert book.favorite is False


# Testa att bok med felaktigt ID-format inte läggs till
def test_not_valid_id():
    # Arrange
    bookstore = BookStore()
    book_id = "Hundraåtta"
    author = "Sams Teachyourself"
    title = "Learn Python in 21 Years"

    # Act: Skicka in en sträng i stället för ett heltal
    new_book = bookstore.add_book(book_id, author, title)

    # Assert: Ska returnera False och inte läggas till
    assert new_book is False
    assert len(bookstore.books) == 0


# Testa att bok med tom titel inte läggs till
def test_not_valid_title():
    # Arrange
    bookstore = BookStore()
    book_id = 108
    author = "Sams Teachyourself"
    title = " "

    # Act: Skicka in med blank titel
    new_book = bookstore.add_book(book_id, author, title)

    # Assert: Ska returnera False och inte läggas till
    assert new_book is False
    assert len(bookstore.books) == 0


# Testa att bok med tom författare inte läggs till
def test_not_valid_author():
    # Arrange
    bookstore = BookStore()
    book_id = 108
    author = " "
    title = "Learn Python in 21 Years"

    # Act: Skicka in med blank författare
    new_book = bookstore.add_book(book_id, author, title)

    # Assert: Ska returnera False och inte läggas till
    assert new_book is False
    assert len(bookstore.books) == 0


# Testa att False returneras om bok saknas
def test_book_not_found():
    # Arrange
    bookstore = BookStore()
    book_id = 99

    # Act
    new_favorite = bookstore.toggle_favorite(book_id)

    # Assert
    assert new_favorite is False
