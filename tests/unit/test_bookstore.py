# ---------------------------------------------------------------
# User story 1: Lägga till böcker i Läslistan
# Som bokslukare, vill jag kunna lägga till en bok som saknas i läslistan
# för att göra boken tillgänglig i systemet
#
# Acceptanskriterier:
# AK 1.1: Boken ska sparas i läslistan om all data är giltig.
# AK 1.2: ID måste vara ett positivt heltal för att boken ska accepteras.
# AK 1.3: Titel får inte vara tom eller endast bestå av mellanslag.
# AK 1.4: Författare får inte vara tomt eller endast bestå av mellanslag.
# AK 1.5: Om bokens ID redan existerar i listan, läggs inte boken till.
# ---------------------------------------------------------------
# User story 2: Hantera favoritstatus i Läslistan
# Som bokslukare vill jag kunna ändra status på en bok i läslistan
# för att välja ut vilka böcker som ska visas som favoriter.
#
# Acceptanskriterier:
# AK 2.1: En bok i katalogen ska kunna få status som favorit.
# AK 2.2: En favoritmarkerad bok ska kunna få sin status avmarkerad.
# AK 2.3: Systemet ska returnera False om man försöker ändra
# favoritstatus på en bok som inte finns.
# ---------------------------------------------------------------

from src.bookstore.bookstore import BookStore


def test_add_book():
    """Testar AK 1.1: Boken ska sparas i läslistan om all data är giltig."""
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


def test_not_valid_id():
    """Testar AK 1.2: ID måste vara ett positivt heltal för att boken
    ska accepteras."""
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


def test_not_valid_title():
    """Testar AK 1.3: Titel får inte vara tom eller endast
    bestå av mellanslag."""
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


def test_not_valid_author():
    """Testar AK 1.4: Författare får inte vara tomt eller endast
    bestå av mellanslag."""
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


def test_add_duplicate_book_id():
    """Testar AK 1.5: Om bokens ID redan existerar i listan,
    läggs inte boken till."""
    # Arrange
    bookstore = BookStore()
    bookstore.add_book(109, "Jeff Sutherland", "Titel 1")

    # Act: Försök lägga till en annan bok med samma ID
    result = bookstore.add_book(109, "Copy Pasta", "A Love Story")

    # Assert: Ska returnera False och listan ska bara ha 1 bok
    assert result is False
    assert bookstore.get_total_books() == 1


def test_mark_as_favorite():
    """Testar AK 2.1: En bok i katalogen ska kunna få status som favorit."""
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


def test_mark_as_not_favorite():
    """Testar AK 2.2: En favoritmarkerad bok ska kunna få sin status
    avmarkerad."""
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


def test_book_not_found():
    """Testar AK 2.3: Systemet ska returnera False om man försöker ändra
    favoritstatus på en bok som inte finns."""
    # Arrange
    bookstore = BookStore()
    book_id = 99

    # Act: Skifta, inte favorit / favorit
    new_favorite = bookstore.toggle_favorite(book_id)

    # Assert
    assert new_favorite is False
