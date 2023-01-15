import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Creation of a very first item"
)
@allure.description(
    "Precondition: Remove all the existent items from the list if they exist\n"
    "Create a new todo item by entering 'Enter'\n"
    "Validate that new item appeared in the top of TODO list"
)
@pytest.mark.parametrize("name", ["Zero item"])
def test_create_1st_item(set_up, name):
    # Arrange test: open browser, go to the page, count elements count before
    page = TodoPage(set_up)
    i = page.count_items_list()
    while page.count_items_list() != 0 and i > 0:
        page.delete_item()
        i -= 1

    # Action: create a new item by button
    page.create_new_item(name)

    # Assert: validate new item created and corresponds expectations in terms of name and format
    expect(page.undone_item.first).to_have_text(name)
    expect(page.item_parenthesis.first).to_have_text("[  ]")
    expect(page.items_list).to_have_count(1)

