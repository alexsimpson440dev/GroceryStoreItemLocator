from src.database import Database
from src.store import Store
class Manager():
    def __init__(self):
        self.database = Database()

    def add_store(self, store_id, store_name, image_dir, dairy_loc, produce_loc, protein_loc, frozen_loc, grain_loc):
        store = Store(store_id, store_name, image_dir, dairy_loc, produce_loc, protein_loc, frozen_loc, grain_loc)
        self.database._add_store(store)
