from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="Field is either blank or unrecognised."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="Field is either blank or unrecognised."
    )

    def post(self):
        request_data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(request_data['username']):
            return {"message": "Username already exists."}, 400

        user = UserModel(**request_data)

        try:
            user.save_to_database()
        except:
                return {"message": "An error occurred while inserting the item to the database."}, 500

        return {"message": "User created successfully."}, 201
