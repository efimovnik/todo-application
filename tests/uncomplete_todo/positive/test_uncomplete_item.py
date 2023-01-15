import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Un-completion of an item by button"
)
@allure.description(
    "Precondition: Check if there are 3 items on the list: 1 is uncomplete, 2 - are completed\n"
    "click on '[X]' parenthesis in order to un-complete one of the completed items\n"
    "Selected item has changed its order - it appeared in the top of 'TODO list', X disappeared inside parenthesis '["
    "]' (on the left of the item name) "
)
def test_uncomplete_item(set_up):
    page = TodoPage(set_up)
    while page.count_done_items() < 2:
        precondition_name = "test uncomplete item, done precondition"
        page.create_new_item(precondition_name)
        page.tick_item(precondition_name)
    while page.count_undone_items() < 1:
        page.create_new_item(item_name="test complete item, undone precondition")
    done_count_before = page.count_done_items()
    undone_count_before = page.count_undone_items()

    name = page.done_item.first.text_content()
    page.tick_item(name)

    expect(page.undone_item.first).to_have_text(name)
    expect(page.items_list.first).to_contain_text("[  ]" + name)
    assert page.count_done_items() == done_count_before - 1
    assert page.count_undone_items() == undone_count_before + 1

