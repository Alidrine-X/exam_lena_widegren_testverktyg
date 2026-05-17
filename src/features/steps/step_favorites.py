from behave import given, then
from playwright.sync_api import expect


@given(u'följande titlar av författare finns i Läslistan')
def step_books_exist_in_catalog(context):
    for row in context.table:
        title = row["title"]
        author = row["author"]
        book = (context.page.locator(".book")
                .filter(has_text=title).filter(has_text=author))
        expect(book).to_be_visible()


@given(u'att användaren markerat följande böcker som favoriter:')
def step_mark_favorite_book_loop(context):
    for row in context.table:
        title = row["title"]
        author = row["author"]

        # Anropa det befintliga steget via dess Gherkin-text
        step_text = (f'When användaren klickar på raden framför boken '
                     f'"{title}" av "{author}"')
        context.execute_steps(step_text)


@then(u'ska följande böcker visas:')
def step_show_books_in_favorite_list(context):
    for row in context.table:
        title = row['title']
        bok_id = f"fav-{title}"
        expect(context.page.get_by_test_id(bok_id)).to_be_visible()


@then(u'listan ska innehålla {antal:d} böcker')
def step_only_two_books_in_favorite_list(context, antal):
    list_items = context.page.locator('[data-testid="book-list"] li')
    expect(list_items).to_have_count(antal)


@given(u'att användaren inte har markerat några favoriter')
def step_user_has_no_favorites(context):
    expect(context.page.locator(".star.selected")).to_have_count(0)


@then(u'ska texten "När du valt, kommer dina favoritböcker '
      u'att visas här." visas')
def step_show_explaining_text(context):
    expected_text = "När du valt, kommer dina favoritböcker att visas här."
    expect(context.page.get_by_text(expected_text)).to_be_visible()


@then(u'favoritlistan ska vara tom')
def step_no_books_in_favorite_list(context):
    favorite_books = context.page.locator('[data-testid="book-list"] li')
    expect(favorite_books).to_have_count(0)
