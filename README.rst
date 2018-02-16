Django JSONFeed
===============

Adding a `JSON Feed`_ type to Django's syndication.

Usage
-----

::

    from django.contrib.syndication.views import Feed
    from jsonfeed import JSONFeed

    class ExampleFeed(Feed):
        type = JSONFeed

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

.. _JSON Feed: https://jsonfeed.org/
