import multiprocessing

from urlo.domain import get_domain

from httpy import HttpRequest, HttpResponse, httpy

from httpy.client.requests import HttpRequests, cookie_jar


class SeleniumDriverGetPage(HttpRequests):

    def __init__(self, driver):
        self._driver = driver
        self._driver_lock = multiprocessing.Lock()

    def request(self, method, url, params=None, data=None, headers=None, **kwargs):
        if not 'method'.upper() == 'GET':
            raise NotImplementedError(method.upper())

        return self._get(url)

    def _get(self, url):
        with self._driver_lock:
            self._driver.get(url)

            return HttpResponse(HttpRequest('GET', url), self._driver.current_url, 200, body=self._driver.page_source)

    def update_cookies(self, cookies=cookie_jar):
        current_domain = get_domain(self._driver.current_url)
        if current_domain:
            site_cookies = [cookie for cookie in list(cookies) if current_domain in cookie.domain]
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
class SeleniumDriverRequests(SeleniumDriverGetPage):

    def __init__(self, driver, client=None):
        super(SeleniumDriverRequests, self).__init__(driver)
        self._client = client or httpy

    def request(self, method, url, **kwargs):
        return self._request_and_update_cookies(method, url, **kwargs) if method != 'GET' else self._get(url)

    def _request_and_update_cookies(self, method, url, **kwargs):
        with self._driver_lock:
            response = self._client.request(method, url, **kwargs)

            self.update_cookies()
        return response