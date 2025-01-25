# Web Scraping API: Attribute Extractor

This project provides an API built using Flask that extracts key metadata from a given URL, such as title, description, keywords, author, publish date, canonical URL, image URLs, and more. It uses BeautifulSoup for HTML parsing and fetching data from the web.

## Features

- Extracts key metadata from any valid URL:
  - Title
  - Description
  - Keywords
  - Author
  - Publish Date
  - Canonical URL
  - Image URLs
  - Links
  - Other meta tags (e.g., Open Graph properties)
  
- Returns data as a structured JSON response.

## Requirements

To run this project, ensure that you have the following installed:

- Python 3.6+
- Flask
- Requests
- BeautifulSoup4

You can install the required Python packages via `pip`:

```bash
pip install Flask requests beautifulsoup4
```

## Project Structure

```
/your_project
│
├── app.py                    # Main Flask application with API routes
├── services/
│   └── AttributeExtractorService.py  # Service to fetch and extract attributes from URLs
├── models/
│   └── AttributeExtractor.py       # Contains the logic for extracting metadata
├── utils/
│   └── api.py                  # Utility functions like fetching URL content
├── README.md                   # Project documentation (this file)
└── requirements.txt            # List of dependencies
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your_username/attribute_extractor.git
cd attribute_extractor
```

### 2. Install dependencies

Run the following command to install all dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start the Flask Application

Run the Flask app using the command:

```bash
python app.py
```

The Flask server will start locally at `http://127.0.0.1:5000`.

### 4. Test the API

You can test the API endpoint by sending a GET request to `/crawl` with the URL as a query parameter.

**Example Request**:

```bash
curl "http://127.0.0.1:5000/crawl?url=https://example.com"
```

**Example Response**:

```json
{
    "title": "Example Domain",
    "description": "This domain is established to be used for illustrative examples in documents.",
    "keyword": "example, domain, illustrative",
    "author": "John Doe",
    "publishDate": "2020-01-01",
    "canonicalUrl": "https://www.example.com",
    "imageUrls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
    "links": ["https://example.com/about", "https://example.com/contact"],
    "otherMetaTags": {
        "og:title": "Example Domain",
        "og:description": "This domain is established to be used for illustrative examples in documents."
    }
}
```

### API Endpoint

- **URL**: `/crawl`
- **Method**: `GET`
- **Query Parameter**: `url` (required) - The URL from which to extract metadata.
  
**Example**:
```bash
GET http://127.0.0.1:5000/crawl?url=https://example.com
```

**Response**: A JSON object containing the extracted metadata or an error message.

---

## Code Explanation

### 1. **`AttributeExtractor` Class**
   - This class is responsible for extracting various attributes like title, description, keywords, and other metadata from the HTML of the provided URL.
   - The BeautifulSoup library is used to parse the HTML content.

### 2. **`extract_attributes` Function**
   - This function initializes an instance of `AttributeExtractor` and uses it to extract attributes from the given URL.

### 3. **Flask API**
   - The Flask application exposes a single route `/crawl` which accepts a URL as a query parameter.
   - When a URL is provided, it calls `extract_attributes` to fetch metadata and returns it in JSON format.

---

## Troubleshooting

- **Missing URL parameter**: If the `url` query parameter is missing in the request, the API will respond with a `400 Bad Request` error.
  
- **Failed to fetch URL**: If the URL cannot be fetched or parsed, the API will return a `500 Internal Server Error`.

---

## Future Improvements

- Add error handling for invalid URLs or failed network requests.
- Implement caching to avoid repeatedly fetching the same URL.
- Add support for other metadata fields, such as Open Graph data or Twitter Card data.
- Allow users to specify additional metadata attributes to extract.
