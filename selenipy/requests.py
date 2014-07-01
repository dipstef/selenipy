import multiprocessing

from urlo.domain import get_domain
from httpy import HttpRequest, HttpResponse, httpy
from httpy.client.requests import cookie_jar, HttpRequestDispatch


class SeleniumDriver(object):

    def __init__(self, driver):
        self._driver = driver
        self._driver_lock = multiprocessing.Lock()

    def get(self, url):
        with self._driver_lock:
            self._driver.get(url)

            return HttpResponse(HttpRequest('GET', url), self._driver.current_url, 200, body=self._driver.page_source)

    def update_cookies(self, cookies=cookie_jar):
        domain = get_domain(self._driver.current_url)

        if domain:
            site_cookies = [cookie for cookie in list(cookies) if domain in cookie.domain]
            for cookie in site_cookies:
                self._driver.delete_cookie(cookie.name)
                self._driver.add_cookie({'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain})

    def close(self):
        self._driver.close()

    def __getattr__(self, item):
        return getattr(self._driver, item)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


#performs other http methods using an internal client and updates the selenium driver cookies after each request
class HttpySeleniumUpdate(HttpRequestDispatch):

    def __init__(self, driver):
        super(HttpySeleniumUpdate, self).__init__(httpy)
        self._driver = driver

    def execute(self, request, **kwargs):
        response = super(HttpySeleniumUpdate, self).execute(request, **kwargs)
        self._driver.update_cookies(cookie_jar)
        return response

    def close(self):
        self._driver.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()