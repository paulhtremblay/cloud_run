import os
import datetime


from flask import Flask
from flask import request


import pprint
pp = pprint.PrettyPrinter(indent = 4)


app = Flask(__name__)


@app.route("/")
def index():
    return 'v2: time is  {d}'.format(
            d = datetime.datetime.now())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

