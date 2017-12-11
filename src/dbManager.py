from src.database import Database
from src.store import Store
from src.items import Items
from src.location import Location

# class that manages requests from the server to the database
class Manager():
    def __init__(self):
        self.database = Database()

    # sends data to add a store to database
    def add_store(self, store_id, store_name, image_dir):
        store = Store(store_id, store_name, image_dir)
        self.database._add_store(store)

    # sends data to add an items to the database
    def add_item(self, item_brand, item_name, item_category, loc_id):
        item = Items(item_brand, item_name, item_category, loc_id)
        self.database._add_item(item)

    # sends data to add an item location to database
    def add_location(self, location_name):
        loc = Location(location_name)
        self.database._add_location(loc)

    # sends data to search the store table for the map directory
    def get_store_image(self, store_id):
        picture = self.database._search_store(store_id)
        return picture

    # sends data to get the store name from the store table
    def get_store_name(self, store_id):
        name = self.database._search_store_name(store_id)
        return name

    # sends data to search an item by its name
    def search_items_by_name(self, search_item):
        returned_items = self.database._search_store_items(search_item)
        return returned_items