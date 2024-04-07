from models.AttributeExtractor import AttributeExtractor
from utils.api import fetch_url_content
from bs4 import BeautifulSoup


def extract_attributes(url):
    attribute_extractor = AttributeExtractor(url)
    response = fetch_url_content(url)
    if response:
        attribute_extractor.soup = BeautifulSoup(response.content, 'html.parser')

    meta_data = {
        'title': attribute_extractor.extract_title(),
        'description': attribute_extractor.extract_description(),
        # 'body': attribute_extractor.extract_body(),
        'keyword': attribute_extractor.extract_keywords(),
        'author': attribute_extractor.extract_author(),
        'publishDate': attribute_extractor.extract_publish_date(),
        'canonicalUrl': attribute_extractor.extract_canonical_url(),
        'imageUrls': attribute_extractor.extract_image_urls(),
        'links': attribute_extractor.extract_links(),
        'otherMetaTags': attribute_extractor.extract_other_meta_tags()
    }

    return meta_data
