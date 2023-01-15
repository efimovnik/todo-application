import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Deletion of a non-unique uncompleted item"
)
@allure.description("1. Precondition: Check if There are 3 uncompleted items, and 2 of them are with the same name - "
                    "one in the bottom of the list, one - on the top\n "
                    "2. Click on X deletion button of first completed item\n"
                    "3. Validate that new item appeared in the top of TODO list\n"
                    "Total number of elements decreased by 1\n")
def test_delete_item(set_up):
    page = TodoPage(set_up)
    if page.count_done_items() < 1:
        precondition_name = "Precondition for deletion"
        page.create_new_item(precondition_name)
        page.tick_item(precondition_name)
    count_before = page.count_items_list()

    name = page.done_item.first.text_content()
    page.delete_item(name)

    expect(page.items_list).to_have_count(count_before - 1)
    expect(page.done_item.first).not_to_contain_text(name)
