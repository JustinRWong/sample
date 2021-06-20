# -*- coding: utf-8 -*-
from app import db

class User(db.Model):
    __tablename__ = 'User'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __repr__(self):
        content = {"id": self._id,
                    "first": self.first_name,
                    "last": self.last_name
                    }
        return str({"User": content})

    def get_id(self):
           return (self._id)
