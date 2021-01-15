import sqlite3
from db import db

class UserModel(db.Model):
     # SQLAlchemy attributes:
    __tablename__ = 'users' # tells SQLAlchemy the table that is being used
    id = db.Column(db.Integer, primary_key=True) # there's a column 'id' of type 'INTEGER' that's a primary key
    username = db.Column(db.String(80)) # character limit of 80; it's good practice to limit this as some users might abuse a limitless length
    password = db.Column(db.String(80)) # same as above

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # the second paramater gives the paramater the query needs ('?'), which should always be given as a tuple

        row = result.fetchone() # gets the first returned value
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
