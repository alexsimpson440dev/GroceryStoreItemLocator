# imports flask and the os
# os for setting a secret key
from src.dbManager import Manager
from src.store import Store
from src.database import Database
from flask import Flask, render_template, request, redirect
import os

MANAGER = Manager()

# sets the app that holds folder information and secret key
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = os.urandom(24)

# a list and dictionary for testing some basic logic in the application
# todo: move this information to a database
groceryStores = ['12331', '14333', '19882', '22314']
items = {'taco':'A5', 'milk':'A2', 'pizza':'A3'}

# sets route for the home page and methods used
@app.route('/')
@app.route('/index', methods=['get', 'post'])
@app.route('/index.html', methods=['get'])
def home():
    # if the server posts, information will be retrieved from a form in index.html
    if request.method == 'POST':
        # gets the store_id searched in html form
        store_id = request.form.get('store_id')
        # tries to find the index of the store id, if there is none and error is caught
        # and resets the home page
        try:
            store_image = MANAGER.get_store_image(store_id)
            if store_image is None:
                print('No store found!')
                return redirect('index.html')
            else:
                # verify_store_id = MANAGER.check_store_id(store_id)
                return render_template('index.html', store_id=store_id)

        except ValueError:
            print('Wrong Store Number')
            return render_template('index.html')

    # if the server does not post, index.html is loaded
    else:
        return render_template('index.html')

@app.route('/store/store_id=10121', methods=['get'])
def store():
    store_id = 10121
    if request.method == 'GET':
        store_map = MANAGER.get_store_image(store_id)
        store_name = MANAGER.get_store_name(store_id)
        return render_template('store.html', store_map=store_map, store_id=store_id, store_name=store_name)


# runs app on port 9999 and sets debug to True
if __name__ == '__main__':
    app.run(port=9999, debug=True)
