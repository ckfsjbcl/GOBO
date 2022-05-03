from flask import Flask
from flask import request

import start

#初始化
start.open()
"""
---------------------
Welcome to use GOBO 
It is a main function
Nothing more
---------------------
"""
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    main_in = request.json
    if main_in["post_type"]=="message":
        start.run(main_in)
    else:
        pass
    # TODO FUNCTION
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5701, debug=False)
