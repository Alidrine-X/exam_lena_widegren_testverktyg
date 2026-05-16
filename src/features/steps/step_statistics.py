from behave import when, then
from playwright.sync_api import expect


@then(u'ska texten "Listan har {amount:d} böcker." visas')
def step_amount_of_books_in_list(context, amount):
    book_list_count = context.page.get_by_test_id("book-count")
    expect(book_list_count).to_contain_text(f"Listan har {amount} böcker.")


@then(u'ska texten "Våra användare har hjärtmarkerat {amount:d} '
      u'böcker." visas')
def step_amount_of_favorite_books_in_list(context, amount):
    favorite_list_count = context.page.get_by_test_id("stars-count")
    expected_text = f"Våra användare har hjärtmarkerat {amount} böcker."
    expect(favorite_list_count).to_contain_text(expected_text)


@when(u'användaren avmarkerar boken "{title}" av "{author}"')
def step_user_unmark_favorite_book(context, title, author):
    book = (context.page.locator(".book")
            .filter(has_text=title).filter(has_text=author))
    expect(book).to_be_visible()
    heart_button = book.get_by_test_id(f"star-{title}")

    expect(heart_button).to_have_class("star selected")
    heart_button.click()
    expect(heart_button).to_have_class("star")
