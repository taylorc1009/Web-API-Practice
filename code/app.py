from flask import Flask, request # Section3(, jsonify, render_template)
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'example-key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		help="Field is either blank or unrecognised."
	)

	@jwt_required()
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)		# 		return items

		return {'item': item}, 200 if item else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': "An item with name '{}' already exists.".format(name)}, 400

		request_data = Item.parser.parse_args()

		item = {'name': name, 'price': request_data['price']}
		items.append(item)

		return item, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))

		return {'message': 'Item deleted.'}

	def put(self, name):
		request_data = Item.parser.parse_args()

		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': request_data['price']}
			items.append(item)
		else:
			item.update(request_data)

		return item

class Items(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=5000, debug=True)





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

# class Item(Resource):
	# parser = reqparse.RequestParser()
	# parser.add_argument('price',
		# type=float,
		# required=True,
		# help="Field is either blank or unrecognised."
	# ) # this is used to make sure that the data being added has the required attributes

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
