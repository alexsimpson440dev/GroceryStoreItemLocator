from src.database import Database
from src.store import Store
class Manager():
    def __init__(self):
        self.database = Database()

    def add_store(self, store_id, store_name, image_dir, dairy_loc, produce_loc, protein_loc, frozen_loc, grain_loc):
        store = Store(store_id, store_name, image_dir, dairy_loc, produce_loc, protein_loc, frozen_loc, grain_loc)
        self.database._add_store(store)

    def get_store_image(self, store_id):
        picture = self.database._search_store(store_id)
        return picture

    def get_store_name(self, store_id):
        name = self.database._search_store_name(store_id)
        return name