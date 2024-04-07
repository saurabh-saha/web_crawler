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
        'body': attribute_extractor.extract_body()
    }

    return meta_data
