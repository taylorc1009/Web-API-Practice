from flask import Flask, request # Section3(, jsonify, render_template)
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'example-key' # at an industrial level, this should be really long and complicated to increase security
api = Api(app)

items = []

# HTML responses
# 200 = request ok
# 201 = object created
# 202 = accepted (same as 201 but used to signify a delayed creation)
# 400 = bad request
# 404 = not found

class Item(Resource):
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None) # 'next' takes the first value found matching the name (if we found more than one), you can call it again to get the second but you'd need to store the filter response to do so
		# the line above is the same as writing:
		# for item in items:
		# 	if item['name'] == name:
		# 		return items

		return {'item': None}, 200 if item else 404 # returns a 404 not found HTML response if no item was found, otherwise return 200

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': "An item with name '{}' already exists.".format(name)}, 400

		request_data = request.get_json(silent=True) # silent causes this method to return None if the data couldn't be parsed as JSON

		item = {'name': name, 'price': request_data['price']}
		items.append(item)

		return item, 201

class Items(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=5000, debug=True) # port is, by default, set to 5000 by REST, so the parameter isn't necessary

## Udemy Section 3
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
