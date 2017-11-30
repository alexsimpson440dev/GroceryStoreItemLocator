# imports flask and the os
# os for setting a secret key
from flask import Flask, render_template, request
import os

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
        store_id = request.form.get('store_id')
        search_item = request.form.get('search_item')

        # tries to find the index of the store id, if there is none and error is caught
        # and resets the home page
        try:
            groceryStores.index(store_id)

            # tries to find an items location in the 'items' dictionary
            # excepts a key error if the item is not in the dictionary
            # will then reset the home page
            try:
                store_location = items[search_item]
                print(store_location)
            except KeyError:
                print('Item Does Not Exist!')

            return render_template('index.html')

        except ValueError:
            print('Wrong Store Number')
            return render_template('index.html')

    # if the server does not post, index.html is loaded
    else:
        return render_template('index.html')

# runs app on port 9999 and sets debug to True
if __name__ == '__main__':
    app.run(port=9999, debug=True)