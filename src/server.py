# imports flask and the os
# os for setting a secret key
from src.dbManager import Manager
from src.store import Store
from src.database import Database
from flask import Flask, render_template, request, url_for
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
        '''store_id = 10121
        store_name = 'Cub'
        image_dir = '/static/images/store10121.png'
        dairy_loc = 'A5'
        produce_loc = 'A3'
        protein_loc = 'A4'
        frozen_loc = 'A1'
        grain_loc = 'A2'

        MANAGER.add_store(store_id, store_name, image_dir, dairy_loc, produce_loc, protein_loc,
                           frozen_loc, grain_loc)'''
        store_id = request.form.get('store_id')

        # tries to find the index of the store id, if there is none and error is caught
        # and resets the home page
        try:
            store_image = MANAGER.get_store(store_id)
            return render_template('store.html', store_image=store_image)

        except ValueError:
            print('Wrong Store Number')
            return render_template('index.html')

    # if the server does not post, index.html is loaded
    else:
        return render_template('index.html')

@app.route('/store', methods=['post', 'get'])
@app.route('/store.html', methods=['get'])
def store():
    return render_template('store.html')


# runs app on port 9999 and sets debug to True
if __name__ == '__main__':
    app.run(port=9999, debug=True)
