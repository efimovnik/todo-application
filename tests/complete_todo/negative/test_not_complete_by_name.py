import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Item is not completed by clicking on his name"
)
@allure.description(
    "Precondition: Check if there is an un-completed item in the list\n"
    "click on item name (not on '[]' parenthesis)\n"
    "Item hasn't been changed, it's still displayed un-complete"
)
def test_not_complete_by_name(set_up):
    page = TodoPage(set_up)
    while page.count_undone_items() < 1:
        page.create_new_item(item_name="test complete item, undone precondition")
    count_before = page.count_done_items()

    name = page.undone_item.first.text_content()
    page.search_item(name).click()

    expect(page.undone_item.first).to_have_text(name)
    expect(page.items_list.first).to_contain_text("[  ]" + name)
    assert page.count_done_items() == count_before

