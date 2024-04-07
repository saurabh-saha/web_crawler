from flask import Flask, request, jsonify
from services.AttributeExtractorService import extract_attributes

app = Flask(__name__)


@app.route('/crawl', methods=['GET'])
def crawl_url():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    try:
        attributes = extract_attributes(url)
        if attributes is None:
            return jsonify({'error': 'Failed to fetch URL'}), 500
    except Exception as e:
        return jsonify({'error': f'Failed to fetch URL: {str(e)}'}), 500
    return jsonify(attributes), 200


if __name__ == '__main__':
    app.run(debug=True)
