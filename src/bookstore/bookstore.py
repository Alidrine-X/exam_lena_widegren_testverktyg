# ---------------------------------------------------------------
# User story 1:
# Som bokslukare,
# behöver jag kunna lägga till en bok som saknas i läslistan,
# för att göra boken tillgänglig i systemet
#
# Acceptanskriterier:
# Given att en viss bok saknas i läslistan
# When bokslukaren lägger till boken
# Then ska den finnas med i listan
#
# Given att jag försöker registrera en ny bok i läslistan
# When jag anger ett ID som inte är ett positivt heltal
# Then ska boken inte sparas i läslistan
#
# Given att jag försöker registrera en ny bok i läslistan
# When jag lämnar fältet för titel tomt eller bara anger mellanslag
# Then ska boken inte sparas i läslistan
#
# Given att jag försöker registrera en ny bok i läslistan
# When jag lämnar fältet för författare tomt eller bara anger mellanslag
# Then ska boken inte sparas i läslistan
# ---------------------------------------------------------------
# User story 2:
# Som bokslukare,
# vill jag kunna ändra vilka böcker som är favoriter
# för att få med bara favoriter i en lista
#
# Acceptanskriterier:
# Given att en bok finns med i läslistan
# When bokslukaren markerar en bok som favorit
# Then ska boken ha status "favorit"
#
# Given att en bok finns med i läslistan
# When bokslukaren avmarkerar en bok som favorit
# Then ska boken ha inte ha status "favorit"
#
# ---------------------------------------------------------------
from src.bookstore.book import Book


class BookStore:
    """Klass för en läslista med böcker"""
    def __init__(self):
        self.books = []

    # Lägg till bok i boklista, kontrollera att id, författare
    # och titel ok samt att bok inte redan finns
    def add_book(self, book_id, author, title):
        if not isinstance(book_id, int) or book_id <= 0:
            return False

        if not author.strip() or not title.strip():
            return False

        for existing_book in self.books:
            if existing_book.book_id == book_id:
                return False

        self.books.append(Book(book_id, author, title))
        return True

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def get_total_books(self):
        return len(self.books)

    # Sätter om markering från tidigare värde mellan favorit/inte favorit
    def toggle_favorite(self, book_id):
        book = self.get_book(book_id)
        if book:
            book.favorite = not book.favorite
            return True
        return False
