# imports flask and the os
# os for setting a secret key
from src.dbManager import Manager
from flask import Flask, render_template, request, redirect
import os

#sets manager class to MANAGER for calling
MANAGER = Manager()

# sets the app that holds folder information and secret key
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = os.urandom(24)

# sets route for the home page and methods used
@app.route('/')
@app.route('/index', methods=['get', 'post'])
@app.route('/index.html', methods=['get'])
def home():
    # if the server posts, information will be retrieved from a form in index.html
    if request.method == 'POST':
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
        #prints to console if there is no store number in the database with that id
        #todo: Flash user this information
        except ValueError:
            print('Wrong Store Number')
            return render_template('index.html')

    # if the server does not post, index.html is loaded
    else:
        return render_template('index.html')

#route for the store page
@app.route('/store/store_id=10121', methods=['get'])
@app.route('/store', methods=['get', 'post'])
def store():
    #hard coded store number
    #todo: get the store number data from previous page
    store_id = 10121
    store_map = MANAGER.get_store_image(store_id)
    store_name = MANAGER.get_store_name(store_id)
    cart = shopping_list(None)
    #if the page requests a post, it will search for the item placed in database
    #todo: show the user the results
    if request.method == 'POST':
        # todo: get information from the get in order to add an item to a list
        search_item = request.form.get('search_item')
        returned_items = MANAGER.search_items_by_name(search_item)
        return render_template('store.html', store_map=store_map, store_id=store_id, store_name=store_name, returned_items=returned_items, cart=cart)
    #else, the page will just post information to the page
    else:
        return render_template('store.html', store_map=store_map, store_id=store_id, store_name=store_name, cart=cart)

#temp route for adding items
@app.route('/_temp_add_items', methods=['post'])
@app.route('/_temp_add_items.html', methods=['get'])
def add_items():
    if request.method == 'POST':
        item_brand = request.form.get('item_brand')
        item_name = request.form.get('item_name')
        item_category = request.form.get('item_category')
        loc_id = request.form.get('loc_id')

        MANAGER.add_item(item_brand, item_name, item_category, loc_id)
        return render_template('_temp_add_items.html')

    else:
        return render_template('_temp_add_items.html')

@app.route('/add', methods=['get', 'post'])
def test():
    if request.method == 'POST':
        item = request.form.get('item')
        shopping_list(item)
        return redirect('store/store_id=10121')

def shopping_list(item, cart=list()):
    if item == None:
        return cart
    else:
        name = item
        name = name.replace("[", "")
        name = name.replace(']', "")
        name = name.replace("',", '|')
        name = name.replace("'", "")
        name = name.replace("| ", "|")
        cart.append(name)
        return cart

# runs app on port 9999 and sets debug to True
if __name__ == '__main__':
    app.run(port=9999, debug=True)
