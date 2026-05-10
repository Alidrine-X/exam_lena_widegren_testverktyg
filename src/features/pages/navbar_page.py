from playwright.sync_api import Page, expect


class NavbarPage:
    def __init__(self, page: Page):
        self.page = page
        self.catalog_button = page.get_by_test_id("catalog")
        self.add_book_button = page.get_by_test_id("add-book")
        self.favorites_button = page.get_by_test_id("favorites")
        self.statistics_button = page.get_by_test_id("statistics")

    def check_all_buttons_visible(self):
        expect(self.catalog_button).to_be_visible()
        expect(self.add_book_button).to_be_visible()
        expect(self.favorites_button).to_be_visible()
        expect(self.statistics_button).to_be_visible()

    def click_catalog(self):
        self.catalog_button.click()

    def click_add_book(self):
        self.add_book_button.click()

    def click_favorites(self):
        self.favorites_button.click()

    def click_statistics(self):
        self.statistics_button.click()
