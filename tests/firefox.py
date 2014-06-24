from selenipy import SeleniumFirefox


def main():
    firefox = SeleniumFirefox()
    response = firefox.request('GET', 'http://www.repubblica.it')
    assert response.status == 200

    firefox.close()

if __name__ == '__main__':
    main()