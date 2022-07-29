import pytest
from selene import have
from selene.support.shared import browser

url = 'https://github.com'
sign_in_locator = 'a[href="/login"'
burger_menu_locator = 'button[aria-label="Toggle navigation"'

chrome = pytest.fixture(params=[(1012, 946), (1200, 1000), (1011, 946), (900, 950)])


@chrome
def browser_size(request):
    """
    Fixture with params
    """

    return request


@pytest.fixture(scope='function', autouse=True)
def set_up_browser(browser_size):
    """
    Set up browser
    """

    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)


@pytest.mark.parametrize("browser_size", [(1200, 1200)], indirect=True)
def test_github_desktop_indirect(browser_size):
    """
    Desktop test with override params
    """

    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(600, 600)], indirect=True)
def test_github_mobile_indirect(browser_size):
    """
    Mobile test with override params
    """

    browser.element(burger_menu_locator).click()
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))
