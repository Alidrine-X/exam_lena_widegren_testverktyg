from behave import when


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
