import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Creation of a non-unique checked item"
)
@allure.description(
    "Precondition: Count total items before test, create item with 'Completed item' name, complete it\n"
    "Create a new todo item with same name as from precondition, by clicking '+' button\n"
    "Validate that there are 2 un-completed items with same name, and order of the 2nd one hasn't been changed"
)
@pytest.mark.parametrize("name", ["Un-completed item"])
def test_create_nonunique_checked(set_up, name):
    # Arrange test: Count total items before test, create item with 'Un-completed item' name
    page = TodoPage(set_up)
    page.create_new_item(name)
    page.item_parenthesis.first.click()
    count_before = page.search_item(name).count()

    # Action: Create a new item with same name as from precondition, by clicking '+' button
    page.create_new_item(name)

    # Assert: validate new item created and corresponds expectations in terms of name and format
    expect(page.search_item(name)).to_have_count(count_before + 1)
    expect(page.item_parenthesis.first).to_have_text("[  ]")
    expect(page.items_list.first).to_contain_text(f"[  ]{name}")
    expect(page.items_list.last).to_contain_text(f"[X]{name}")
