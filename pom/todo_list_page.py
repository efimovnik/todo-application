class TodoPage:

    def __init__(self, page):
        self.page = page
        self.field_add_item = page.get_by_placeholder("add a new todo...")
        self.items_list = page.get_by_role("listitem")
        self.button_add_item = page.get_by_role("button", name="+")
        self.undone_item = page.locator(".undone")
        self.done_item = page.locator(".done")
        self.item_parenthesis = page.locator(".icon")

    def delete_item(self, item_name=None):
        # delete item by item_name if provided, first - otherwise
        if item_name:
            self.items_list.filter(has_text=f"{item_name}").get_by_role("button", name="×").click()
        else:
            self.page.get_by_role("button", name="×").first.click()

    def search_item(self, item_name):
        # delete item by item_name if provided, first - otherwise
        return self.items_list.filter(has_text=f"{item_name}")

    def count_items_list(self):
        return self.items_list.count()

    def create_new_item(self, item_name):
        self.field_add_item.fill(item_name)
        self.button_add_item.click()

    def create_new_item_keyboard(self, item_name):
        self.field_add_item.fill(item_name)
        self.button_add_item.press("Enter")

    def count_undone_items(self):
        return self.undone_item.count()

    def count_done_items(self):
        return self.done_item.count()

    def tick_item(self, item_name=None):
        if item_name:
            self.items_list.filter(has_text=f"{item_name}").locator("//span[@class='icon']").click()
        else:
            self.items_list.first.locator("//span[@class='icon']").click()
