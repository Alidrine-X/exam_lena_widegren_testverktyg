from playwright.sync_api import Page


class CatalogPage:
    def __init__(self, page: Page):
        self.page = page









        self.add_book_button.click()