from flask import Blueprint, jsonify, request
from models.functions import get_primes

routes = Blueprint("routes", __name__)


@routes.route("/")
def hi():
    return "Welcome to Conectivity API"


@routes.route('/get-prime-numbers', methods=["GET"])
def prime_numbers():
    try:
        number = int(request.args.get("query_string"))
        if number < 1:
            return "The query_string should be a positive number"
    except Exception as err:
        print("Exception: The query_string parameter is mandatory and should be a positive number"+err)
        return "The query_string parameter is mandatory and should be a positive number. "+err
    else:
        return get_primes(number)


@routes.route("/convert-height", methods=["POST"])
def convert_height():
    try:
        data = request.json
        name = data["name"]
        convert_height = data["height"]
        splitter = convert_height.split(" ")
        pulgadas = int(splitter[0])
        height = "{:.2f}".format(pulgadas/39.370) + " metros"
    except Exception as err:
        print("Exception: Enter the name and height in valid format"+err)
        return "Enter the name and height in valid format. "+err
    else:
        return jsonify({"name": name, "height": height})
