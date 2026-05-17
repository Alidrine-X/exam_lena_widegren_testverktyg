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
