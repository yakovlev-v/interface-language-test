url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_exist(browser):
    browser.get(url)
    a = len(browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert a == 1, 'На странице нет кнопки "Добавить в корзину"'
