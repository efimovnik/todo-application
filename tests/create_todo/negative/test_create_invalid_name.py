import re

import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Creation of a new unique item by keyboard 'Enter' button"
)
@allure.description(
    "Precondition: Count total items before test\n"
    "Create a new todo item by input 'Enter'\n"
    "Validate that new item appeared in the top of TODO list"
)
@pytest.mark.parametrize("name", ["",
                                  "    ",
                                  ""])
def test_create_invalid_name(set_up, name):
    # Arrange test: open browser, go to the page, count elements count before
    page = TodoPage(set_up)
    count_before = page.count_items_list()

    # Action: create a new item by button
    page.create_new_item_keyboard(name)

    # Assert: validate new item created and corresponds expectations in terms of name and format
    expect(page.items_list).to_have_count(count_before)
