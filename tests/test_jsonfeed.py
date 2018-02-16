import unittest


class JSONFeedTest(unittest.TestCase):

    def setUp(self):
        from jsonfeed import JSONFeed
        self.feed = JSONFeed(
            title='Hello, World!',
            link='https://example.com/',
            feed_url='https://example.com/feed.json',
            description='Hello, World!',
            language='en'
        )

        self.feed.add_item(
            title='Hello',
            link='https://example.com/hello',
            external_url='https://mylesb.ca/',
            description='Testing.'
        )

    def test_add_root_elements(self):
        root_elements = self.feed.add_root_elements()
        self.assertEqual(root_elements['title'], 'Hello, World!')
        self.assertEqual(root_elements['home_page_url'],
                         'https://example.com/')

    def test_add_item(self):
        self.feed.add_item(
            title='Hello',
            link='https://example.com/hello',
            external_url='https://mylesb.ca/',
            description='Testing.'
        )

        item = self.feed.items[-1]

        self.assertEqual(item['title'], 'Hello')
        self.assertEqual(item['external_url'], 'https://mylesb.ca/')

    def test_writeString(self):
        feed = self.feed.writeString('utf-8')
        self.assertTrue(feed)
