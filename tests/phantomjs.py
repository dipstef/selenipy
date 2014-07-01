from selenipy import PhantomJs


def main():
    with PhantomJs() as phantom_js:
        response = phantom_js.get('http://www.google.com')
        assert response.status == 200

if __name__ == '__main__':
    main()