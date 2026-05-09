from behave import given, when, then
from playwright.sync_api import expect


@then(u'ska boken "Ormar på ett plan: En Python-berättelse" finnas med i Läslistan')
def step_impl(context):
    title = "Ormar på ett plan: En Python-berättelse"
    book_row = context.page.locator(".book", has_text=title)
    expect(book_row).to_be_visible()


@then(u'Läslistan ska innehålla minst 13 böcker')
def step_impl(context):
    book_row_13 = context.page.locator(".book").nth(12)
    expect(book_row_13).to_be_visible()

