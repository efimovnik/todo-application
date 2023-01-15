import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Completion of a last not completed item"
)
@allure.description(
    "Precondition: Check if There are 2 items on the list: 1 is completed, 1 is uncompleted\n"
    "click on '[]' parenthesis in order to complete last uncompleted items\n"
    "Selected item has changed its order - it appeared in the bottom of 'TODO list', 'X' appeared inside parenthesis"
)
def test_complete_last_item(set_up):
    page = TodoPage(set_up)
    while page.count_undone_items() > 1:
        name = page.items_list.first.text_content()
        page.tick_item(name)
    if page.count_undone_items() == 0:
        page.create_new_item(item_name="test complete item, undone precondition")
    count_before = page.count_done_items()

    name = page.undone_item.first.text_content()
    page.tick_item(name)

    expect(page.done_item.last).to_have_text(name)
    expect(page.items_list.last).to_contain_text("[X]" + name)
    assert page.count_undone_items() == 0
    assert page.count_done_items() == count_before + 1


