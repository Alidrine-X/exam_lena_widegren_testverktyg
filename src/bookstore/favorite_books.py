class FavoriteBooks:
    """Klass för en lista över favoritböcker"""
    def __init__(self):
        self.favorites = []

    def add(self, book):
        if not hasattr(book, 'book_id'):
            return

        for existing_book in self.favorites:
            if existing_book.book_id == book.book_id:
                return
        self.favorites.append(book)

    def remove(self, book):
        if not hasattr(book, 'book_id'):
            return

        if book in self.favorites:
            self.favorites.remove(book)

    def get_favorite_count(self):
        return len(self.favorites)
