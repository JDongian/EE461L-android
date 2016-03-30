from flask import Blueprint


inventory_api = Blueprint('account_api', __name__)


@inventory_api.route("/inventory/list")
def inventory_list():
    return jsonify(**{'socks': 1})
