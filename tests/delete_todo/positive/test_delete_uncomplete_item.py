import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Uncompleted item deletion"
)
@allure.description("1. Precondition: Check if there is a uncompleted item in the list\n"
                    "2. Click on X deletion button of first completed item\n"
                    "3. Validate that new item appeared in the top of TODO list\n"
                    "Total number of elements decreased by 1\n")
def test_delete_item(set_up):
    page = TodoPage(set_up)
    if page.count_undone_items() < 1:
        page.create_new_item("Precondition for deletion")
    count_before = page.count_items_list()

    name = page.undone_item.first.text_content()
    page.delete_item(name)

    expect(page.items_list).to_have_count(count_before - 1)
    if page.count_undone_items() > 0:
        expect(page.undone_item.first).not_to_contain_text(name)
