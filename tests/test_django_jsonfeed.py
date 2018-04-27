import datetime
import sys
import mock
import unittest


class DjangoJSONFeedTest(unittest.TestCase):

    def setUp(self):
        from django.contrib.syndication.views import Feed

        with mock.patch.dict(sys.modules, {'feedgenerator': None}):
            from jsonfeed import JSONFeed

        class TestFeed(Feed):
            type = JSONFeed

            def items(self):
                return [{
                            'pk': 1,
                            'name': 'Hello, World!',
                            'content': 'Hello, World!',
                            'published': datetime.datetime(2018, 1, 1),
                            'url': 'https://example.com/1'
                        }, {
                            'pk': 2,
                            'name': 'Hello, World!',
                            'content': 'Hello, World!',
                            'published': datetime.datetime(2018, 1, 2),
                            'url': 'https://example.com/2'
                        }]

            def item_title(self, item):
                return item['name']

            def item_description(self, item):
                return item['content']

            def item_link(self, item):
                return item['url']

        self.feed = TestFeed()
        self.item = self.feed.items()[0]

    def test_feed_items(self):
        self.assertEqual(len(self.feed.items()), 2)
