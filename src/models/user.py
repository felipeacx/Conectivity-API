from marshmallow import Schema, fields
from utils.db import db


class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    apellido = db.Column(db.String(40))
    direccion = db.Column(db.String(40))

    def __init__(self, nombre, apellido, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion


class UsuarioSchema(Schema):
    id = fields.Integer()
    nombre = fields.String()
    apellido = fields.String()
    direccion = fields.String()
