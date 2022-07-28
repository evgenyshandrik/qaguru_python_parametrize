"""
Tests with different run parameterized
"""
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


def test_github_desktop(browser_size):
    """
    Desktop test with params fixture
    """

    width = browser_size.param[0]
    height = browser_size.param[1]

    if width < 1012:
        pytest.skip('Size for mobile version')

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    """
    Mobile test with params fixture
    """

    width = browser_size.param[0]
    height = browser_size.param[1]

    if width > 1011:
        pytest.skip('Size for desktop version')

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(burger_menu_locator).click()
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(1200, 1200)], indirect=True)
def test_github_desktop_indirect(browser_size):
    """
    Desktop test with override params
    """

    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(600, 600)], indirect=True)
def test_github_mobile_indirect(browser_size):
    """
    Mobile test with override params
    """

    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(burger_menu_locator).click()
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("width, height",
                         [
                             pytest.param(1012, 946, id='Chrome size 1012 x 946'),
                             pytest.param(1200, 1000, id='Chrome size 1200 x 1000')
                         ])
def test_github_desktop_parametrize(width, height):
    """
    Desktop test with parametrize
    """

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("width, height",
                         [
                             pytest.param(1011, 946, id='Chrome size 1011 x 946'),
                             pytest.param(900, 950, id='Chrome size 900 x 950')
                         ])
def test_github_mobile_parametrize(width, height):
    """
    Mobile test with parametrize
    """

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)
    browser.element(burger_menu_locator).click()
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))
