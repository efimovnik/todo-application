import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Item is not un-completed by clicking on his name"
)
@allure.description(
    "Precondition: Check if there is an completed item in the list\n"
    "click on item name (not on '[X]' parenthesis)\n"
    "Item hasn't been changed, it's still displayed complete"
)
def test_not_uncomplete_by_name(set_up):
    page = TodoPage(set_up)
    while page.count_done_items() < 1:
        precondition_name = "test complete item, done precondition"
        page.create_new_item(precondition_name)
        page.tick_item(precondition_name)
    done_count_before = page.count_done_items()
    undone_count_before = page.count_undone_items()

    name = page.done_item.last.text_content()
    page.search_item(name).click()

    expect(page.done_item.last).to_have_text(name)
    expect(page.items_list.last).to_contain_text("[X]" + name)
    assert page.count_done_items() == done_count_before
    assert page.count_undone_items() == undone_count_before

