from flask import Flask, jsonify # Section3(, jsonify, render_template)
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from datetime import timedelta
from db import db

app = Flask(__name__)
app.secret_key = 'example-key'
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # tells SQLAlchemy that the database exists at the root folder of the project and that we're using SQLite (SQLAlchemy is interchangeable between database solutions which allows us to change solution, using this name, without changing any other line of code)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disables Flasks' native tracker but not SQLAlchemys': tracking twice would use more resources

db.init_app(app)
api = Api(app)

jwt = JWT(app, authenticate, identity)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
	return jsonify({
		'access_token': access_token.decode('utf-8'),
		'user_id': identity.id
	})

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	app.run(port=5000, debug=True)





### Udemy Section 5
# app.secret_key = 'example-key'
# app.config['JWT_AUTH_URL_RULE'] = '/login' # changes the authentication endpoint from '/auth' to '/login'
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # changes the JWT token time out from 5 minutes to half an hour
# # app.config['JWT_AUTH_USERNAME_KEY'] = 'email' # changes the authentication key name from 'username' to 'email'
# api = Api(app)

# jwt = JWT(app, authenticate, identity)

# @jwt.auth_response_handler # allows us to return more than just the 'access_token' from the '/auth'/'/login' endpoint
# def customized_response_handler(access_token, identity):
	# return jsonify({
		# 'access_token': access_token.decode('utf-8'),
		# 'user_id': identity.id
	# })

# # should allow you to handle JWT errors, but Python is saying that "'JWT' object has no attribute 'error_handler'"
# # @jwt.error_handler
# # def customized_error_handler(error):
	# # return jsonify({
		# # 'message': error.description,
		# # 'code': error.status_code
	# # }), error.status_code

# # can be used in the 'User' class to get a users' identity from the 'access_token'
# # from flask_jwt import jwt_required, current_identity
# # class User(Resource):
	# # @jwt_required()
	# # def get(self): # view all users
	# # user = current_identity
	# # # then implement admin auth method
	# # ...

# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(Items, '/items')
# api.add_resource(UserRegister, '/register')

# if __name__ == '__main__': # prevents the server from starting if we're running 'app.py' by importing it
	# app.run(port=5000, debug=True)





### Udemy Section 4
# app.secret_key = 'example-key' # at an industrial level, this should be really long and complicated to increase security
# api = Api(app)

# jwt = JWT(app, authenticate, identity) # creates a new endpoint '/auth'

# items = []

# # HTML responses
# # 200 = request ok
# # 201 = object created
# # 202 = accepted (same as 201 but used to signify a delayed creation)
# # 400 = bad request
# # 404 = not found
# # 500 = internal server error

# class Item(Resource):
	# parser = reqparse.RequestParser()
	# parser.add_argument('price',
		# type=float,
		# required=True,
		# help="Field is either blank or unrecognised."
	# # this is used to make sure that the data being added has the required attributes

	# @jwt_required() # makes this method require an access token, which is given during authentication (if you want this to apply to the other methods, you will need to give them this decorator too)
	# def get(self, name):
		# # 'next' takes the first value found matching the name (if we found more than one), you can call it again to get the second but you'd need to store the filter response to do so
		# item = next(filter(lambda x: x['name'] == name, items), None)
		# # the line above is the same as writing:
		# # for item in items:
		# # 	if item['name'] == name:
		# # 		return items

		# return {'item': item}, 200 if item else 404 # returns a 404 not found HTML response if no item was found, otherwise return 200

	# def post(self, name):
		# if next(filter(lambda x: x['name'] == name, items), None):
			# return {'message': "An item with name '{}' already exists.".format(name)}, 400

		# request_data = Item.parser.parse_args()

		# item = {'name': name, 'price': request_data['price']}
		# items.append(item)

		# return item, 201

	# def delete(self, name):
		# global items # we need to tell the method we're using the global 'items' list, otherise it will try to use a new, undefined variable in 'filter()'
		# items = list(filter(lambda x: x['name'] != name, items))

		# return {'message': 'Item deleted.'}

	# def put(self, name):
		# request_data = Item.parser.parse_args()

		# item = next(filter(lambda x: x['name'] == name, items), None)
		# if item is None:
			# item = {'name': name, 'price': request_data['price']}
			# # items.append(item)
		# else:
			# item.update(request_data)

		# return item

# class Items(Resource):
	# def get(self):
		# return {'items': items}

# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(Items, '/items')
# app.run(port=5000, debug=True) # port is, by default, set to 5000 by REST, so the parameter isn't necessary





### Udemy Section 3
# stores = [
# 	{
# 		'name': 'Store Example',
# 		'items': [
# 			{
# 				'name': 'Item Example',
# 				'price': 15.99
# 			}
# 		]
# 	}
# ]

# @app.route('/')
# def home():
# 	return render_template('index.html')

# @app.route('/store', methods=['POST']) # home directory, "https://www.example.com" becomes "https://www.example.com/"
# def create_store():
# 	request_data = request.get_json()
# 	new_store = {
# 		'name': request_data['name'],
# 		'items': []
# 	}
# 	stores.append(new_store)
# 	return jsonify(new_store)

# @app.route('/store')
# def get_stores():
# 	return jsonify({'stores': stores}) # we need to convert 'stores' from a list to a dictionary as 'jsonify' only accepts dictionaries

# @app.route('/store/<string:name>')
# def get_store(name):
# 	for store in stores:
# 		if store['name'] == name:
# 			return jsonify(store)
# 	return jsonify({'error': 'Store was not found'})

# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_store_item(name):
# 	for store in stores:
# 		if store['name'] == name:
# 			request_data = request.get_json()
# 			new_item = {
# 				'name': request_data['name'],
# 				'price': request_data['price']
# 			}
# 			store['items'].append(new_item)
# 			return jsonify(new_item)
# 	return jsonify({'error': 'Store was not found'})

# @app.route('/store/<string:name>/item')
# def get_store_items(name):
# 	for store in stores:
# 		if store['name'] == name:
# 			return jsonify({'items': store['items']})
# 	return jsonify({'error': 'Store was not found'})

# app.run(port=5000) # if this cuauses an error, the port may be in use so all you need to do is change the port
