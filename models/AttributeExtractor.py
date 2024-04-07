class AttributeExtractor:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def extract_title(self):
        try:
            return self.soup.title.text.strip() if self.soup.title else None
        except Exception as e:
            print('Error while extracting title:', e)
            return None

    def extract_description(self):
        try:
            description_tag = self.soup.find('meta', attrs={'name': 'description'})
            return description_tag['content'] if description_tag else None
        except Exception as e:
            print('Error while extracting description:', e)
            return None

    def extract_body(self):
        try:
            return self.soup.get_text().strip() if self.soup else None
        except Exception as e:
            print('Error while extracting body:', e)
            return None

    def extract_keywords(self):
        try:
            keywords_tag = self.soup.find('meta', attrs={'name': 'keywords'})
            return keywords_tag['content'] if keywords_tag else None
        except Exception as e:
            print('Error while extracting keywords:', e)
            return None

    def extract_author(self):
        try:
            author_tag = self.soup.find('meta', attrs={'name': 'author'})
            return author_tag['content'] if author_tag else None
        except Exception as e:
            print('Error while extracting author:', e)
            return None

    def extract_publish_date(self):
        try:
            publish_date_tag = self.soup.find('meta', attrs={'name': 'publish-date'})
            return publish_date_tag['content'] if publish_date_tag else None
        except Exception as e:
            print('Error while extracting publish date:', e)
            return None

    def extract_canonical_url(self):
        try:
            canonical_tag = self.soup.find('link', attrs={'rel': 'canonical'})
            return canonical_tag['href'] if canonical_tag else None
        except Exception as e:
            print('Error while extracting canonical URL:', e)
            return None

    def extract_image_urls(self, limit=5):
        try:
            return [img['src'] for img in self.soup.find_all('img')][:limit] if self.soup else None
        except Exception as e:
            print('Error while extracting image URLs:', e)
            return None

    def extract_links(self, limit=5):
        try:
            return [a['href'] for a in self.soup.find_all('a')][:limit] if self.soup else None
        except Exception as e:
            print('Error while extracting links:', e)
            return None

    def extract_other_meta_tags(self):
        try:
            other_meta_tags = self.soup.find_all('meta')
            meta_data = {}
            for tag in other_meta_tags:
                if tag.get('name'):
                    meta_data[tag['name']] = tag.get('content')
                elif tag.get('property'):
                    meta_data[tag['property']] = tag.get('content')
            return meta_data
        except Exception as e:
            print('Error while extracting other meta tags:', e)
            return None
