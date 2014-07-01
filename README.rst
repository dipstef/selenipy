Selenipy
========

``httpy`` selenium wrapper


Features
========

Use selenium drivers with an interface similar to ``requests``

Works in combination ``httpy`` to programmatically execute post requests and update selenium cookies

Usage
=====

.. code-block:: python

    from selenipy import Firefox, PhantomJs

    with Firefox() as firefox:
        response = firefox.get('http://www.google.com')
        assert response.status == 200

    with PhantomJs() as phantom_js:
        response = phantom_js.get('http://www.google.com')
        assert response.status == 200


Selenium drivers cookies update, can be useful for instance when you have an existing scraper using a basic http client,
but you want to extract javascript evaluated content. The site requires authentication, which you have already
implemented in your scraper and don't to handle through Selenium.


.. code-block:: python

    from selenipy import HttpySeleniumUpdate

    with PhantomJs() as phantom_js:
        #our content requires authentication, this won't work
        response = phantom_js.get('http://www.site.com')

        update_phantomjs = HttpySeleniumUpdate(phantom_js)

        #phantom js cookies will be updated
        update_phantomjs.post('http://www.site.com/login', data={'user': 'pippo', 'password': 'baudo'})

        #now we are authenticated
        response = phantom_js.get('http://www.site.com')