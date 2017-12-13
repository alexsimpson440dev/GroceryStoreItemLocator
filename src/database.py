import sqlite3
from src.store import Store
from src.items import Items
from src.location import Location
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import mapper, sessionmaker, relationship

METADATA = MetaData()
# Database class that handles database mapping, creating tables, creating sessions, and quering data
class Database():
    def __init__(self, connection_string="sqlite:///foodLocationDB.sqlite3"):
        self.sqlite_file = connection_string
        self.engine = self._get_connection()
        self.store = self._map_store()
        self.items = self._map_items()
        self.location = self._map_location()
        METADATA.create_all(bind=self.engine)

    # creates and maps the store data to its data model
    def _map_store(self):
        store = Table('Store', METADATA,
            Column('store_id', Integer, primary_key=True),
            Column('store_name', String),
            Column('image_dir', String))
        mapper(Store, store)
        return store

    # creates and maps the items data to its data model
    def _map_items(self):
        items = Table('Items', METADATA,
            Column('item_id', Integer, primary_key=True),
            Column('item_brand', String),
            Column('item_name', String),
            Column('item_category', String),
            Column('loc_id', Integer, ForeignKey('Location.location_id')))
        mapper(Items, items)
        return items

    # creates and maps the location table to its data model
    def _map_location(self):
        location = Table('Location', METADATA,
                         Column('location_id', Integer, primary_key=True),
                         Column('location_name', String))
        mapper(Location, location, properties={'loc_id': relationship(Items, backref='Location')})
        return location

    # gets a connection to the database via the file, which is linked to the connection string to find its location
    def _get_connection(self):
        engine = create_engine(self.sqlite_file)
        return engine

    # creates a session based off the engine that was created in the _get_connection
    def _get_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    # adds a store to the store table, commits changes
    def _add_store(self, store):
        session = self._get_session()
        session.add(store)
        session.commit()

    # adds an items to the items table, commits changes
    def _add_item(self, item):
        session = self._get_session()
        session.add(item)
        session.commit()

    # adds an item location to the location table, commits changes
    def _add_location(self, location_name):
        session = self._get_session()
        session.add(location_name)
        session.commit()

    #todo: combine this query and query below into one
    # queries the store table for the store id where the given data is equal to the store id
    def _search_store(self, store_id):
        session = self._get_session()
        for store in session.query(Store)\
            .filter(Store.store_id == store_id):
            session.commit()
            if store.store_id is None:
                return None
            else:
                return store.image_dir

    # queries the store table for the store name where the store id is equal to the data given
    def _search_store_name(self, store_id):
        session = self._get_session()
        for store in session.query(Store)\
            .filter(Store.store_id == store_id):
            return store.store_name

    # queries the items table for the item name and brand to display to user
    # loops table for the brand, name, and item location id
    # sets a list to those values for each that is like the item given, then loops them into a dictionary with a key that counts
    def _search_store_items(self, search_item):
        counter = 1
        items_dict = dict()
        session = self._get_session()
        for brand, name, loc in session.query(Items.item_brand, Items.item_name, Items.loc_id)\
            .filter(Items.item_name.ilike('%'+search_item+'%')):
            items_list = [brand, name, loc]
            for i in items_list:
                items_dict.setdefault(counter, []).append(i)
            counter+=1
        return items_dict
