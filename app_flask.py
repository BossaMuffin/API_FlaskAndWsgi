from flask import Flask, request
import pprint

app = Flask(__name__)


@app.route("/", methods=["POST", "GET", "PUT"])
def hello_world():
    response = ["<p>Hello, You!</p>", "Get : "+pprint.pformat(request.args)]

    if request.method == "POST":
        response.append("Post : "+pprint.pformat(request.args))
    else:
        print('Other')
    return response
