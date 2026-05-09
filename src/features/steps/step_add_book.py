from behave import given, when, then
from playwright.sync_api import expect


@given(u'att användaren är på webbsidan')
def step_impl(context):
    context.page.goto(context.base_url, timeout=5000)


@given(u'användaren klickat på knappen "Lägg till bok"')
def step_impl(context):
    add_button = context.page.get_by_test_id("add-book")
    add_button.click()


@when(u'användaren skriver in titeln "{title}"')
def step_impl(context, title):
    title_element = context.page.get_by_test_id("add-input-title")
    title_element.fill(title)


@when(u'användaren skriver in författaren "{author}"')
def step_impl(context, author):
    author_element = context.page.get_by_test_id("add-input-author")
    author_element.fill(author)


@when(u'användaren klickar på knappen "Lägg till ny bok"')
def step_impl(context):
    submit_button = context.page.get_by_test_id("add-submit")
    submit_button.click()


@when(u'användaren klickar på knappen "Katalog"')
def step_impl(context):
    catalog_button = context.page.get_by_test_id("catalog")
    catalog_button.click()


@then(u'ska boken "{title}" av "{author}" finnas med i Läslistan')
def step_impl(context, title, author):
    book_row = context.page.locator(".book", has_text=title)
    expect(book_row).to_contain_text(author)
