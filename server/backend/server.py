from flask import Flask
from flask import jsonify
from inventoryAPI import inventory_api
app = Flask(__name__)
app.register_blueprint(account_api)


@app.route("/")
def index():
    raise NotImplementedError
    return "index"


if __name__ == "__main__":
    app.run()
