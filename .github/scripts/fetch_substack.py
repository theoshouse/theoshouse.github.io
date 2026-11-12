"""Download the list of posts from Substack and save it for the website.

This script runs automatically on GitHub (see .github/workflows/substack.yml).
It reads the Substack address from _config.yml, downloads the RSS feed,
and writes the posts to _data/substack.json, which the website reads.
"""

import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "_config.yml"
OUTPUT = ROOT / "_data" / "substack.json"
MAX_POSTS = 20
CONTENT_NS = "{http://purl.org/rss/1.0/modules/content/}"


def substack_url():
    match = re.search(r'^substack_url:\s*["\']?([^"\'\s#]+)', CONFIG.read_text(), re.M)
    if not match:
        sys.exit("No substack_url found in _config.yml; nothing to do.")
    return match.group(1).rstrip("/")


def plain_text(fragment, limit=220):
    text = html.unescape(re.sub(r"<[^>]+>", " ", fragment or ""))
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + "…"
    return text


def fetch(url):
    request = urllib.request.Request(
        url, headers={"User-Agent": "personal-website-feed-reader (GitHub Actions)"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def parse(feed_xml):
    channel = ET.fromstring(feed_xml).find("channel")
    posts = []
    for item in channel.findall("item")[:MAX_POSTS]:
        date = item.findtext("pubDate")
        enclosure = item.find("enclosure")
        image = enclosure.get("url") if enclosure is not None else None
        if image and not (enclosure.get("type") or "").startswith("image"):
            image = None
        description = item.findtext("description") or item.findtext(CONTENT_NS + "encoded")
        posts.append(
            {
                "title": (item.findtext("title") or "Untitled").strip(),
                "url": (item.findtext("link") or "").strip(),
                "date": parsedate_to_datetime(date).date().isoformat() if date else None,
                "description": plain_text(description),
                "image": image,
            }
        )
    return posts


def main():
    feed_url = substack_url() + "/feed"
    print(f"Reading {feed_url}")
    posts = parse(fetch(feed_url))
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n")
    print(f"Saved {len(posts)} posts to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
