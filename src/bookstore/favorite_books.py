# ---------------------------------------------------------------
# User story 2:
# Som bokslukare,
# vill jag kunna markera en bok som en favorit
# för att få med boken på en lista över mina favoriter
#
# Acceptanskriterier:
# Given att en bok inte finns i favoritlistan
# When bokslukaren markerar en bok som favorit
# Then ska boken finnas med i favoritlistan
#
# Given att en bok redan finns i favoritlistan
# When jag försöker lägga till samma bok igen
# Then ska listan inte spara några dubbletter
# ---------------------------------------------------------------
# User story 3:
# Som bokslukare,
# vill jag kunna avmarkera en bok som en favorit
# för att ta bort boken från listan över mina favoriter
#
# Acceptanskriterier:
# Given att en bok finns i favoritlistan
# When bokslukaren avmarkerar en bok som favorit
# Then ska boken inte längre finnas med i favoritlistan
# ---------------------------------------------------------------

class FavoriteBooks:
    """Klass för en lista över favoritböcker"""
    def __init__(self):
        self.favorites = []

    def add(self, book):
        for existing_book in self.favorites:
            if existing_book.book_id == book.book_id:
                return
        self.favorites.append(book)

    def remove(self, book):
        if book in self.favorites:
            self.favorites.remove(book)
