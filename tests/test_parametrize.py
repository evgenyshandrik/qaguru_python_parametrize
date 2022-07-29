"""
Tests with different run parameterized
"""
import pytest
from selene import have
from selene.support.shared import browser

url = 'https://github.com'
sign_in_locator = 'a[href="/login"'
burger_menu_locator = 'button[aria-label="Toggle navigation"'


@pytest.fixture(scope='function', params=[(1012, 946), (1200, 1000)])
def set_up_browser_desktop(request):
    """
    Set up browser desktop
    """
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_desktop_parametrize(set_up_browser_desktop):
    """
    Desktop test with parametrize
    """
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.fixture(scope='function', params=[(1011, 946), (900, 950)])
def set_up_browser_mobile(request):
    """
    Set up browser mobile
    """
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_mobile_parametrize(set_up_browser_mobile):
    """
    Mobile test with parametrize
    """

    browser.element(burger_menu_locator).click()
    browser.element(sign_in_locator).click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))
