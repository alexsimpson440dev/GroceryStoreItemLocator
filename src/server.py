from flask import Flask, render_template, request
import os

app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = os.urandom(24)


groceryStores = ['12331', '14333', '19882', '22314']
items = {'taco':'A5', 'milk':'A2', 'pizza':'A3'}

@app.route('/')
@app.route('/index', methods=['get', 'post'])
@app.route('/index.html', methods=['get', 'post'])
def home():
    if request.method == 'POST':
        store_id = request.form.get('store_id')
        search_item = request.form.get('search_item')

        try:
            groceryStores.index(store_id)
            try:
                store_location = items[search_item]
                print(store_location)
            except KeyError:
                print('Item Does Not Exist!')

            return render_template('index.html')

        except ValueError:
            print('Wrong Store Number')
            return render_template('index.html')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=9999, debug=True)