from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="Field is either blank or unrecognised."
    )

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {"message": "An error occurred while reading the item from the database."}, 500

        if item:
            return item.json(), 200
        return {'message': 'Item not found.'}, 404

    def post(self, name):
        try:
            if ItemModel.find_by_name(name): # we can't do "if self.get(name)" because the 'get' method required a JWT token, so the code to find the item had been moved to 'find_by_name'
                return {'message': "An item with name '{}' already exists.".format(name)}, 400
        except:
            return {"message": "An error occurred while reading the item from the database."}, 500

        request_data = Item.parser.parse_args()

        item = ItemModel(name, request_data['price'])

        try:
            item.save_to_database()
        except:
            return {"message": "An error occurred while inserting the item to the database."}, 500
        return item.json(), 201

    def delete(self, name):
        try:
            try:
                item = ItemModel.find_by_name(name)
            except:
                return {"message": "An error occurred while reading the item from the database."}, 500

            if item:
                item.delete_from_database()
        except:
            return {"message": "An error occurred while deleting the item from the database."}, 500
        return {'message': 'Item deleted.'}, 200

    def put(self, name):
        request_data = Item.parser.parse_args()

        try:
            item = ItemModel.find_by_name(name)
        except:
            return {"message": "An error occurred while reading the item from the database."}, 500

        if item is None:
            item = ItemModel(name, request_data['price'])
        else:
            try:
                item.price = request_data['price']
            except:
                return {"message": "An error occurred while updating the item in the database."}, 500

        try:
            item.save_to_database()
        except:
            return {"message": "An error occurred while inserting the item to the database."}, 500

        return item.json(), 200

class Items(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} # instead of list comprehension, you can also use 'list(map(lambda x: x.json(), ItemModel.query.all()))' (usually used when you need to interact with other languages as, notice how we use the 'map()' conversion, we can convert it to other data types)
