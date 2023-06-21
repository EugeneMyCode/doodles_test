""""Тест названия ссылки Doodles Archive"""

from pages.google_main import GooglePage

def test_doodles(driver):
    """'Doodles Archive' находится в тексте ссылки?"""
    page = GooglePage(driver)
    page.go_to_site()
    page.click_lucky_button()
    
    element = page.check_archive_on_page()
    assert "Doodles Archive" in element
