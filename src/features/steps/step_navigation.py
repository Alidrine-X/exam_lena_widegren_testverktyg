from behave import then, when, given
from playwright.sync_api import expect
from src.features.pages.navbar_page import NavbarPage


@given(u'att användaren är på webbsidan')
def step_user_on_page(context):
    context.page.goto(context.base_url, timeout=5000)


@then(u'ska alla knapparna vara synliga')
def step_all_buttons_visible(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.check_all_buttons_visible()


@given(u'användaren klickar på knappen "Lägg till bok"')
@when(u'användaren klickar på knappen "Lägg till bok"')
def step_user_click_on_add_book(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.click_add_book()


@then(u'ska användaren hamna på undersidan "add-book"')
def step_user_see_page_add_book(context):
    expect(context.page.get_by_test_id("add-input-title")).to_be_visible()


@when(u'användaren klickar på knappen "Mina böcker"')
def step_user_click_on_favorites(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.click_favorites()


@then(u'ska användaren hamna på undersidan "favorites"')
def step_user_see_page_favorites(context):
    expect(context.page.get_by_text("När du valt, kommer dina favoritböcker "
                                    "att visas här.")).to_be_visible()


@when(u'användaren klickar på knappen "Statistik"')
def step_user_click_on_statistics(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.click_statistics()


@then(u'ska användaren hamna på undersidan "statistics"')
def step_user_see_page_statistics(context):
    expect(context.page.get_by_test_id("book-count")).to_be_visible()


@when(u'användaren klickar på knappen "Katalog"')
def step_user_click_on_catalog(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.click_catalog()


@then(u'ska användaren hamna på undersidan "catalog"')
def step_user_see_page_catalog(context):
    expect(context.page.locator(".book").first).to_be_visible()
