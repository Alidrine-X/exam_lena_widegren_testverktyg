from behave import then, when, given
from playwright.sync_api import expect


@given(u'att användaren är på webbsidan')
def step_user_on_page(context):
    context.page.goto(context.base_url, timeout=5000)


@then(u'ska fliken ha namnet "{expected_text}"')
def step_check_page_title(context, expected_text):
    expect(context.page).to_have_title(expected_text)


@then(u'rubriken ska vara "{expected_text}"')
def step_check_page_heading(context, expected_text):
    expect(context.page.locator("h1")).to_have_text(expected_text)


@then(u'ska alla navigeringsknapparna vara synliga')
def step_all_buttons_visible(context):
    context.navbar.check_all_buttons_visible()


@when(u'användaren klickar på knappen "Katalog"')
def step_user_click_on_catalog(context):
    context.navbar.click_catalog()


@then(u'ska undersidan för "catalog" visas')
def step_user_see_page_catalog(context):
    expect(context.page.locator(".book").first).to_be_visible()


@given(u'användaren klickat på knappen "Lägg till bok"')
@when(u'användaren klickar på knappen "Lägg till bok"')
def step_user_click_on_add_book(context):
    context.navbar.click_add_book()


@then(u'ska undersidan för "add-book" visas')
def step_user_see_page_add_book(context):
    expect(context.page.get_by_test_id("add-input-title")).to_be_visible()


@when(u'användaren klickar på knappen "Mina böcker"')
def step_user_click_on_favorites(context):
    context.navbar.click_favorites()


@then(u'ska undersidan för "favorites" visas')
def step_user_see_page_favorites(context):
    expect(context.page.get_by_text("När du valt, kommer dina favoritböcker "
                                    "att visas här.")).to_be_visible()


@when(u'användaren klickar på knappen "Statistik"')
def step_user_click_on_statistics(context):
    context.navbar.click_statistics()


@then(u'ska undersidan för "statistics" visas')
def step_user_see_page_statistics(context):
    expect(context.page.get_by_test_id("book-count")).to_be_visible()
