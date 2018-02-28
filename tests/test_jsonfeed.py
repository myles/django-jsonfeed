import datetime
import unittest


class JSONFeedTest(unittest.TestCase):

    def setUp(self):
        from jsonfeed import JSONFeed
        self.feed = JSONFeed(
            title='Hello, World!',
            link='https://example.com/',
            feed_url='https://example.com/feed.json',
            description='Hello, World!',
            author_link='https://example.com/',
            author_name='Myles Braithwaite',
            author_email='myles@example.com',
            language='en',
            categories=['example'],
            icon='https://example.com/icon.png',
            favicon='https://example.com/favicon.png',
            feed_guid='https://example.com/',
            feed_copyright='Copyright 2018',
            ttl=5000
        )

        self.feed.add_item(
            title='Hello',
            link='https://example.com/hello',
            external_url='https://mylesb.ca/',
            description='Testing.',
            pubdate=datetime.datetime(1986, 9, 19, 8, 45)
        )

    def test_add_root_elements(self):
        root_elements = self.feed.add_root_elements()
        self.assertEqual(root_elements['title'], 'Hello, World!')
        self.assertEqual(root_elements['home_page_url'],
                         'https://example.com/')
        self.assertEqual(root_elements['author'],
                         {'name': 'Myles Braithwaite',
                          'email': 'myles@example.com',
                          'url': 'https://example.com/'})
        self.assertEqual(root_elements['_django'],
                         {'copyright': 'Copyright 2018',
                          'ttl': '5000'})

    def test_add_item(self):
        item = self.feed.add_item_elements(dict(
            title='Hello, World!',
            description='<p>Hello, World!</p>',
            content_text='Hello, World!',
            link='https://example.com/hello',
            external_url='https://mylesb.ca/',
            guid='https://example.com/hello',
            author_name='Myles Braithwaite',
            author_email='myles@example.com',
            author_link='https://example.com/',
            pubdate=datetime.datetime.now(),
            updateddate=datetime.datetime.now(),
            categories=['test'],
            copyright='Copyright 2018'
        ))

        self.assertEqual(item['title'], 'Hello, World!')
        self.assertEqual(item['content_html'], '<p>Hello, World!</p>')
        self.assertEqual(item['content_text'], 'Hello, World!')

    def test_writeString(self):
        feed = self.feed.writeString('utf-8')
        self.assertTrue(feed)
