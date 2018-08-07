import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    cards = [{
      "id": 0,
      "active": False,
      "imageUri": "/images/cornfield.jpg",
      "cardPrice": 50,
      "cardName": "cornfield"
    }, {
      "id": 1,
      "active": False,
      "imageUri": "/images/waterdrop.jpg",
      "cardPrice": 100,
      "cardName": "waterdrop"
    }, {
      "id": 2,
      "active": False,
      "imageUri": "/images/island.jpg",
      "cardPrice": 200,
      "cardName": "island"
    }, {
      "id": 3,
      "active": False,
      "imageUri": "/images/desert.jpg",
      "cardPrice": 500,
      "cardName": "desert"
    }, {
      "id": 4,
      "active": False,
      "imageUri": "/images/san_francisco.jpg",
      "cardPrice": 1000,
      "cardName": "San Francisco"
    }, {
      "id": 5,
      "active": False,
      "imageUri": "/images/castle.jpg",
      "cardPrice": 5000,
      "cardName": "Gemany Castle"
    }]
    return json.dumps(cards)

if __name__ == "__main__":
    ssl_context = ('D:\workspace\StarBuck\Server\crt\server.crt', 'D:\workspace\StarBuck\Server\crt\server.key')
    app.run(host="127.0.0.1", port=80, debug=True)
