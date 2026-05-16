from behave import given, when, then
from playwright.sync_api import expect


@then(u'ska boken "{title}" av "{author}" finnas med i Läslistan')
def step_confirm_book_on_page(context, title, author):
    book = (context.page.locator(".book")
            .filter(has_text=title).filter(has_text=author))
    expect(book).to_be_visible()


@given(u'Läslistan innehåller 13 böcker')
@then(u'Läslistan innehåller 13 böcker')
def step_confirm_min_books_on_page(context):
    expect(context.page.locator(".book")).to_have_count(13)


@when(u'användaren klickar på raden framför boken "{title}" av "{author}"')
def step_mark_favorite_book(context, title, author):
    book = (context.page.locator(".book")
            .filter(has_text=title).filter(has_text=author))
    expect(book).to_be_visible()
    heart_button = book.get_by_test_id(f"star-{title}")
    heart_button.click()
    expect(heart_button).to_have_class("star selected")


@then(u'ska ett hjärta synas på raden framför boken "{title}" av "{author}"')
def step_verify_favorite_book(context, title, author):
    book = (context.page.locator(".book")
            .filter(has_text=title).filter(has_text=author))
    heart_button = book.get_by_test_id(f"star-{title}")
    expect(heart_button).to_have_class("star selected")
