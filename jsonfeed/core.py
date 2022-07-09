import datetime
import json

try:
    from feedgenerator import SyndicationFeed, rfc3339_date
except ImportError:
    from django.utils.feedgenerator import SyndicationFeed, rfc3339_date


def format_json_feed_author(author_link, author_name, author_email):
    if not author_link and not author_name and not author_email:
        return None

    author = {}

    if author_link:
        author["url"] = author_link

    if author_name:
        author["name"] = author_name

    if author_email:
        author["email"] = author_email

    return author


class JSONFeed(SyndicationFeed):
    content_type = "application/json; charset=utf-8"

    @staticmethod
    def json_serial(obj):
        """
        Custom JSON serializer for objects not serializable by default.
        """

        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        raise TypeError("Type {} not serializable.".format(type(obj)))

    def write(self, outfile, encoding):
        data = self.add_root_elements()

        for item in self.items:
            data["items"] += [
                self.add_item_elements(item),
            ]

        outfile.write(json.dumps(data, default=self.json_serial))

    def format_authors_root_elements(self):
        author = format_json_feed_author(
            author_link=self.feed.get("author_link"),
            author_name=self.feed.get("author_name"),
            author_email=self.feed.get("author_email"),
        )

        if author is not None:
            return [author]

    def add_root_elements(self, handler=None):  # noqa
        root_elements = {
            "version": "https://jsonfeed.org/version/1.1",
            "title": self.feed.get("title"),
            "home_page_url": self.feed.get("link"),
            "description": self.feed.get("description"),
        }

        authors = self.format_authors_root_elements()

        if authors is not None:
            root_elements["authors"] = authors

        if self.feed.get("feed_url"):
            root_elements["feed_url"] = self.feed["feed_url"]

        if self.feed.get("language"):
            root_elements["language"] = self.feed["language"]

        if self.feed.get("categories"):
            root_elements["categories"] = self.feed["categories"]

        if self.feed.get("icon"):
            root_elements["icon"] = self.feed["icon"]

        if self.feed.get("favicon"):
            root_elements["favicon"] = self.feed["favicon"]

        if self.feed.get("feed_guid"):
            root_elements["id"] = self.feed["feed_guid"]

        if self.feed.get("feed_copyright") or self.feed.get("ttl"):
            root_elements["_django"] = {}

        if self.feed.get("feed_copyright"):
            root_elements["_django"]["copyright"] = self.feed["feed_copyright"]

        if self.feed.get("ttl"):
            root_elements["_django"]["ttl"] = self.feed["ttl"]

        root_elements["items"] = list()

        return root_elements

    def format_authors_item_elements(self, item):
        author = format_json_feed_author(
            author_link=item.get("author_link"),
            author_name=item.get("author_name"),
            author_email=item.get("author_email"),
        )

        if author is not None:
            return [author]

    def add_item_elements(self, item, handler=None):  # noqa
        item_element = {}

        if item.get("title"):
            item_element["title"] = item.get("title")

        if item.get("description"):
            item_element["content_html"] = item.get("description")

        if item.get("content_text"):
            item_element["content_text"] = item.get("content_text")

        if item.get("link"):
            item_element["url"] = item.get("link")

        if item.get("unique_id"):
            item_element["id"] = item.get("unique_id")

        authors = self.format_authors_item_elements(item)

        if authors is not None:
            item_element["authors"] = authors

        if item.get("enclosures"):
            item_element["attachments"] = []

        for attachment in item.get("enclosures", []):
            item_element["attachments"] += [
                {
                    "url": attachment.url,
                    "size_in_bytes": attachment.length,
                    "mime_type": attachment.mime_type,
                }
            ]

        if (
            item.get("enclosure_url")
            or item.get("enclosure_length")
            or item.get("enclosure_mime_type")
        ):
            item_element["attachments"] += [
                {
                    "url": item.get("enclosure_url"),
                    "size_in_bytes": item.get("enclosure_length"),
                    "mime_type": item.get("enclosure_mime_type"),
                    "duration_in_seconds": item.get("enclosure_in_seconds"),
                }
            ]

        if item.get("pubdate"):
            item_element["date_published"] = rfc3339_date(item.get("pubdate"))

        if item.get("updateddate"):
            item_element["date_modified"] = rfc3339_date(item.get("updateddate"))

        if item.get("categories"):
            item_element["tags"] = item.get("categories")

        if item.get("copyright"):
            item_element["_django"] = {"copyright": item.get("copyright")}

        if item.get("external_url"):
            item_element["external_url"] = item.get("external_url")

        return item_element
