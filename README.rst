===============
Django-JSONFeed
===============

.. image:: https://travis-ci.org/myles/django-jsonfeed.svg?branch=master
    :target: https://travis-ci.org/myles/django-jsonfeed
    :alt: CI Status
.. image:: https://readthedocs.org/projects/django-jsonfeed/badge/?version=latest
    :target: http://django-jsonfeed.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This library intends to support `JSON Feed`_ in Django_ and feedgenerator_.

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

Installation
------------

    $ pip install django-jsonfeed

.. _JSON Feed: https://jsonfeed.org/
.. _feedgenerator: https://pypi.python.org/pypi/feedgenerator
.. _Django: https://djangoproject.com/
