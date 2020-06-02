from flask import Flask
import requests
import os


app = Flask(__name__)


@app.route('/')
def home():
    html = get_header()
    for image in get_images():
        html += '<tr><td>' + image + '<br><img src=' + image + ' width=100%></td></tr>'
    html += '</table></body></html>'
    return html


def get_header():
    return '<html><head><title>protests and looting</title></head><body><table width=100%>' + \
           '<h1>Protest and Looting Images</h1>SEDME<p>'

def get_images():
    images = []
    payload = {'key': 'GOOGLE_API_KEY', 'cx': 'GOOGLE_SEARCH_ID', 'q': 'looting+protest'}
    r = requests.get('https://customsearch.googleapis.com/customsearch/v1', params=payload)
    for item in r.json()['items']:
        images.append(item['pagemap']['cse_image'][0]['src'])
    return images


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
