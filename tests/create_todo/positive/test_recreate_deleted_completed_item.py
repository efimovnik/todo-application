import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Re-creation of an item after deletion (completed)"
)
@allure.description(
    "Precondition: create, complete, and delete new TODO item\n"
    "Create a new todo item with same name as in precondition\n"
    "Validate that new item appeared in the top of TODO list"
)
@pytest.mark.parametrize("name", ["Re-creation of an item after deletion (completed)"])
def test_recreate_deleted_completed_item(set_up, name):
    # Preconditions:
    # 1) create 1 completed item exists with "Re-creation of an item after deletion (completed)" name
    page = TodoPage(set_up)
    page.field_add_item.fill(name)
    page.button_add_item.click()
    page.item_parenthesis.first.click()
    # 2) Delete the item from 1st step
    page.delete_item(name)
    count_before = page.count_items_list()

    # Action: create a new item by button
    page.field_add_item.fill(name)
    page.button_add_item.click()

    # Assert: validate new item created and corresponds expectations in terms of name and format
    expect(page.items_list).to_have_count(count_before + 1)
    expect(page.undone_item.first).to_have_text(name)
    expect(page.item_parenthesis.first).to_have_text("[  ]")

