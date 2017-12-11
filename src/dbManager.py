from src.database import Database
from src.store import Store
from src.items import Items
from src.location import Location

class Manager():
    def __init__(self):
        self.database = Database()

    def add_store(self, store_id, store_name, image_dir):
        store = Store(store_id, store_name, image_dir)
        self.database._add_store(store)

    def add_item(self, item_brand, item_name, item_category, loc_id):
        item = Items(item_brand, item_name, item_category, loc_id)
        self.database._add_item(item)

    def add_location(self, location_name):
        loc = Location(location_name)
        self.database._add_location(loc)

    def get_store_image(self, store_id):
        picture = self.database._search_store(store_id)
        return picture

    def get_store_name(self, store_id):
        name = self.database._search_store_name(store_id)
        return name

    def search_items_by_name(self, search_item):
        returned_items = self.database._search_store_items(search_item)
        return returned_items