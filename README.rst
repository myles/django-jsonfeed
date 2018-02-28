Django JSONFeed
===============

Adding a `JSON Feed`_ type to `Django Syndication Feed Framework`_ or any standard Python project.

Usage
-----

If you are using Django::

    from django.contrib.syndication.views import Feed
    from jsonfeed import JSONFeed

    class ExampleFeed(Feed):
        type = JSONFeed

If you are using this library without Django, you will first need to install the feedgenerator_ Python package::

    from jsonfeed import JSONFeed

    feed = JSONFeed(
        title='Hello, World!',
        link='https://example.com/',
        language='en'
    )

    feed.add_item(
        title='One',
        link='https://example.com/1/',
        pubdate=datetime(2018, 2, 28, 15, 16)
    )

    return feed.writeString()

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

.. _JSON Feed: https://jsonfeed.org/
.. _feedgenerator: https://pypi.python.org/pypi/feedgenerator
.. _Django Syndication Feed Framework: https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
