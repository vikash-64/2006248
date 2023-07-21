from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
url = "http://20.244.56.144/numbers/rand"
def fetch_numbers_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("numbers", [])
    except:
        pass
    return []

@app.route('/numbers')
def get_numbers():
    urls = request.args.getlist('url')
    if not urls:
        return jsonify({"numbers": []})

    numbers = set()
    for url in urls:
        numbers.update(fetch_numbers_from_url(url))

    return jsonify({"numbers": sorted(list(numbers))})

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
