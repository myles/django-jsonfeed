import datetime
import unittest

from feedgenerator import Enclosure


class JSONFeedTest(unittest.TestCase):
    def setUp(self):
        from jsonfeed import JSONFeed

        self.feed = JSONFeed(
            title="Hello, World!",
            link="https://example.com/",
            feed_url="https://example.com/feed.json",
            description="Hello, World!",
            author_link="https://example.com/",
            author_name="Myles Braithwaite",
            author_email="myles@example.com",
            language="en",
            categories=["example"],
            icon="https://example.com/icon.png",
            favicon="https://example.com/favicon.png",
            feed_guid="https://example.com/",
            feed_copyright="Copyright 2018",
            ttl=5000,
        )

        self.feed.add_item(
            unique_id="https://example.com/hello",
            title="Hello",
            link="https://example.com/hello",
            external_url="https://mylesb.ca/",
            description="Testing.",
            pubdate=datetime.datetime(1986, 9, 19, 8, 45),
        )

    def test_json_serial(self):
        self.assertEqual(
            self.feed.json_serial(datetime.date(2018, 4, 27)), "2018-04-27"
        )

    def test_json_serial_exception(self):
        with self.assertRaises(TypeError):
            self.feed.json_serial(datetime)

    def test_add_root_elements(self):
        root_elements = self.feed.add_root_elements()

        self.assertEqual(root_elements["title"], "Hello, World!")

        self.assertEqual(root_elements["home_page_url"], "https://example.com/")

        self.assertEqual(
            root_elements["authors"],
            [
                {
                    "name": "Myles Braithwaite",
                    "email": "myles@example.com",
                    "url": "https://example.com/",
                }
            ],
        )

        self.assertEqual(
            root_elements["_django"], {"copyright": "Copyright 2018", "ttl": "5000"}
        )

    def test_add_item(self):
        item = self.feed.add_item_elements(
            dict(
                title="Hello, World!",
                description="<p>Hello, World!</p>",
                content_text="Hello, World!",
                link="https://example.com/hello",
                external_url="https://mylesb.ca/",
                unique_id="https://example.com/hello",
                author_name="Myles Braithwaite",
                author_email="myles@example.com",
                author_link="https://example.com/",
                pubdate=datetime.datetime.now(),
                updateddate=datetime.datetime.now(),
                categories=["test"],
                copyright="Copyright 2018",
                enclosure_url="https://example.com/hello/image.png",
                enclosure_length=20,
                enclosure_mime_type="image/png",
                enclosures=[
                    Enclosure(
                        url="https://example.com/hello/audio.mp3",
                        length=20,
                        mime_type="audio/mpeg",
                    )
                ],
            )
        )

        self.assertEqual(item["title"], "Hello, World!")

        self.assertEqual(item["id"], "https://example.com/hello")

        self.assertEqual(item["content_html"], "<p>Hello, World!</p>")

        self.assertEqual(item["content_text"], "Hello, World!")

        self.assertEqual(
            item["authors"],
            [
                {
                    "name": "Myles Braithwaite",
                    "email": "myles@example.com",
                    "url": "https://example.com/",
                }
            ],
        )

        self.assertEqual(
            item["attachments"][1]["url"], "https://example.com/hello/image.png"
        )

        self.assertEqual(
            item["attachments"][0]["url"], "https://example.com/hello/audio.mp3"
        )

    def test_writeString(self):
        feed = self.feed.writeString("utf-8")
        self.assertTrue(feed)
