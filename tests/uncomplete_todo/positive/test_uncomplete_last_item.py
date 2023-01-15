import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Un-completion of a last completed item"
)
@allure.description(
    "Precondition: Check if There are 2 items on the list: 1 is completed, 1 is uncompleted\n"
    "click on '[]' parenthesis in order to complete last uncompleted items\n"
    "Selected item has changed its order - it appeared in the bottom of 'TODO list', 'X' appeared inside parenthesis"
)
def test_uncomplete_last_item(set_up):
    page = TodoPage(set_up)
    while page.count_done_items() > 1:
        name = page.done_item.first.text_content()
        page.tick_item(name)
    if page.count_undone_items() == 0:
        page.create_new_item(item_name="test complete item, undone precondition")
    count_before = page.count_undone_items()

    name = page.done_item.first.text_content()
    page.tick_item(name)

    expect(page.undone_item.first).to_have_text(name)
    expect(page.items_list.first).to_contain_text("[  ]" + name)
    assert page.count_done_items() == 0
    assert page.count_undone_items() == count_before + 1


