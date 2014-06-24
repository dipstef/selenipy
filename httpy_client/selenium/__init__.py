from selenium import webdriver
from httpy.requests import user_agent

from .requests import SeleniumDriverRequests


class SeleniumFirefox(SeleniumDriverRequests):
    def __init__(self, client=None):
        super(SeleniumFirefox, self).__init__(webdriver.Firefox(), client)

_phantom_js = dict(webdriver.DesiredCapabilities.PHANTOMJS)
_phantom_js['phantomjs.page.settings.userAgent'] = user_agent


class SeleniumPhantomJs(SeleniumDriverRequests):
    def __init__(self, client=None):
        driver = webdriver.PhantomJS(port=8910, desired_capabilities=_phantom_js)
        super(SeleniumPhantomJs, self).__init__(driver, client)