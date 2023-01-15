import allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Re-un-completion of a previously uncompleted item"
)
@allure.description(
    "Precondition: 1. Check if there is a un-completed item in the list, 2. complete this item\n"
    "click on '[X]' parenthesis in order to complete the item\n"
    "Selected item has changed its order - it appeared in the top of 'TODO list', 'X' disappeared inside parenthesis"
)
def test_reuncomplete_item(set_up):
    page = TodoPage(set_up)
    # Search if there is done item exists. If not - create new (undone), and complete it
    if page.count_done_items() == 0:
        precondition_name = "test complete item, undone precondition"
        page.create_new_item(precondition_name)
        page.tick_item(precondition_name)
    # Un-complete done item (1st time)
    name = page.done_item.last.text_content()
    page.tick_item(name)
    # Complete item (to make 2nd un-completion available)
    name = page.undone_item.first.text_content()
    page.tick_item(name)
    # Count done / undone items amount before test
    done_count_before = page.count_done_items()
    undone_count_before = page.count_undone_items()


    # Action - re-un-complete item
    page.tick_item(name)

    expect(page.undone_item.first).to_have_text(name)
    expect(page.items_list.first).to_contain_text("[  ]" + name)
    assert page.count_undone_items() == undone_count_before + 1
    assert page.count_done_items() == done_count_before - 1


