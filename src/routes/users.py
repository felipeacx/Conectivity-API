from flask import Blueprint, jsonify, request
from models.user import Usuario, UsuarioSchema
from utils.db import db

users = Blueprint("users", __name__)


@users.route("/data", methods=["GET"])
def get_data():
    try:
        users = Usuario.query.all()
    except Exception as err:
        print("err", err)
        return err
    else:
        size = len(users)
        if size <= 0:
            return "No users registered"
        else:
            serializer = UsuarioSchema(many=True)
            data = serializer.dump(users)
            return jsonify(
                data
            )


@users.route("/set-data", methods=["PUT"])
def set_data():
    try:
        data = request.json
        nombre = data["fname"]
        apellido = data["lname"]
        direccion = data["address"]
    except Exception as err:
        print("err", err)
        return err
    else:
        new_user = Usuario(nombre, apellido, direccion)
        db.session.add(new_user)
        db.session.commit()
        return "User created successful."
