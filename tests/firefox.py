from selenipy import Firefox


def main():
    with Firefox() as firefox:
        response = firefox.get('http://www.google.com')
        assert response.status == 200

if __name__ == '__main__':
    main()