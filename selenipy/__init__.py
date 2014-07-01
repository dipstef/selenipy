from selenium import webdriver
from httpy.client import user_agent

from .requests import SeleniumDriver, HttpySeleniumUpdate


class Firefox(SeleniumDriver):
    def __init__(self,):
        super(Firefox, self).__init__(webdriver.Firefox())

_phantom_js = dict(webdriver.DesiredCapabilities.PHANTOMJS)
_phantom_js['phantomjs.page.settings.userAgent'] = user_agent


class PhantomJs(SeleniumDriver):
    def __init__(self):
        driver = webdriver.PhantomJS(port=8910, desired_capabilities=_phantom_js)
        super(PhantomJs, self).__init__(driver)