from behave import given, when, then
from playwright.sync_api import expect
from src.features.pages.navbar_page import NavbarPage


@given(u'användaren klickat på knappen "Lägg till bok"')
def step_user_click_add_book(context):
    context.navbar = NavbarPage(context.page)
    context.navbar.click_add_book()


@when(u'användaren skriver in titeln "{title}"')
def step_user_fill_in_title(context, title):
    title_element = context.page.get_by_test_id("add-input-title")
    title_element.fill(title)


@when(u'användaren skriver in författaren "{author}"')
def step_user_fill_in_author(context, author):
    author_element = context.page.get_by_test_id("add-input-author")
    author_element.fill(author)


@when(u'användaren klickar på knappen "Lägg till ny bok"')
def step_user_click_add_new_book(context):
    submit_button = context.page.get_by_test_id("add-submit")
    submit_button.click()


@then(u'ska boken "{title}" av "{author}" finnas med i Läslistan')
def step_confirm_book_added(context, title, author):
    book_row = context.page.locator(".book", has_text=title)
    expect(book_row).to_contain_text(author)
