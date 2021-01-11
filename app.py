from flask import Flask

app = Flask(__name__)

stores = [
	{
		'name': 'Store Example',
		'items': [
			{
				'name': 'Item Example',
				'price': 15.99
			}
		]
	}
]

@app.route('/store', methods=['POST']) # home directory, "https://www.example.com" becomes "https://www.example.com/"
def create_store():
	pass

@app.route('/store')
def get_stores():
	pass

@app.route('/store/<string: name>')
def get_store(name):
	pass

@app.route('/store/<string: name>/item', methods=['POST'])
def create_store_item(name):
	pass

@app.route('/store/<string: name>/item')
def get_store_items(name):
	pass

app.run(port=5000) # if this cuauses an error, the port may be in use so all you need to do is change the port