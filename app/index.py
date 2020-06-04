from flask import Flask, request
import requests
import os


app = Flask(__name__)


@app.route('/')
def home():
    html = get_header()
    for image in get_images():
        html += '<p>' + image + '<br><img src=' + image + ' width=100%>'
    html += get_footer()
    return html


def get_header():
    return '<html><head><title>protests and looting</title></head><body>' + \
           '<h1>Protest and Looting Images</h1>SEDME -- Hex7 Internet Solutions<p>'

def get_images():
    images = []
    payload = {'key': 'GOOGLE_API_KEY', 'cx': 'GOOGLE_SEARCH_ID', 'q': 'looting+protest'}
    r = requests.get('https://customsearch.googleapis.com/customsearch/v1', params=payload)
    for item in r.json()['items']:
        images.append(item['pagemap']['cse_image'][0]['src'])
    return images


def get_footer():
    return '<p><br><p><center><b><font size=5>&copy;2000-2020 </font></b>' + \
           '<a target=_blank href=http://hex7.com><b><font size=5>Hex 7 Internet Solutions</font></b></a><br>' + \
           request.headers.get('User-Agent') + '<br>' + get_ip() + '</body></html>'


def get_ip():
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    else:
        return request.remote_addr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
