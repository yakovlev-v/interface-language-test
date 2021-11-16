url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_interface_language(browser):
    browser.get(url)
    assert len(
        browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")) == 1, "А где кнопка?!"
