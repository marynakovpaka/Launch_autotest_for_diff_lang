
def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"), "Add to basket button is absent"


