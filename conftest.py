import pytest


@pytest.fixture(scope="function")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://efimovnik.github.io/todo-application/")
    page.set_default_timeout(3000)
    yield page
