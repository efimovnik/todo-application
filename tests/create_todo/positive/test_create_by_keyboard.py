import re

import pytest, allure
from playwright.sync_api import expect
from pom.todo_list_page import TodoPage


@allure.title(
    "Creation of a new unique item by keyboard 'Enter' button"
)
@allure.description(
    "Precondition: Count total items before test\n"
    "Create a new todo item by input 'Enter'\n"
    "Validate that new item appeared in the top of TODO list"
)
@pytest.mark.parametrize("name", ["Second item",
                                  "  Spaces    Spaces everywhere    ",
                                  pytest.param(
                                      "Wikipedia was launched by Jimmy Wales and Larry Sanger on January 15, "
                                      "2001. Sanger "
                                      "coined its name as a blend of wiki and encyclopedia.[5][6] Wales was "
                                      "influenced by "
                                      "the spontaneous order ideas associated with Friedrich Hayek and the Austrian",
                                      marks=pytest.mark.xfail)])
def test_create_by_keyboard(set_up, name):
    # Arrange test: open browser, go to the page, count elements count before
    page = TodoPage(set_up)
    count_before = page.count_items_list()

    # Action: create a new item by button
    page.create_new_item_keyboard(name)

    # Assert: validate new item created and corresponds expectations in terms of name and format
    pat = re.compile(r"\s+")
    expect(page.undone_item.first).to_have_text(pat.sub(' ', name).strip())
    expect(page.item_parenthesis.first).to_have_text("[  ]")
    expect(page.items_list).to_have_count(count_before + 1)
