import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Re-completion of a previously completed item"
)
@allure.description(
    "Precondition: 1. Check if there is a completed item in the list, 2. Un-complete this item\n"
    "click on '[]' parenthesis in order to complete the item\n"
    "Selected item has changed its order - it appeared in the bottom of 'TODO list', 'X' appeared inside parenthesis"
)
def test_recomplete_item(set_up):
    # Arrange test: Check if there is a completed item in the list, and Un-complete this item
    page = TodoPage(set_up)
    if page.count_done_items() == 0:
        page.create_new_item(item_name="test complete item, undone precondition")
    name = page.done_item.first.text_content()
    page.tick_item(name)
    done_count_before = page.count_done_items()
    undone_count_before = page.count_undone_items()

    # Action: complete last item
    page.tick_item(name)

    # Assert: validate new item created and corresponds expectations in terms of name and format
    expect(page.done_item.last).to_have_text(name)
    expect(page.items_list.last).to_contain_text("[X]" + name)
    assert page.count_undone_items() == undone_count_before - 1
    assert page.count_done_items() == done_count_before + 1


