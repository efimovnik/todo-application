import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Last item deletion"
)
@allure.description("1. Precondition: Check if there is only 1 item in the list\n"
                    "2. Click on X deletion button of the last item\n"
                    "3. Validate that TODO list is empty\n"
)
def test_delete_last_item(set_up):
    page = TodoPage(set_up)
    i = page.count_items_list()
    while page.count_items_list() > 1 and i > 0:
        page.delete_item()
        i -= 1

    page.delete_item()

    expect(page.items_list).to_have_count(0)
