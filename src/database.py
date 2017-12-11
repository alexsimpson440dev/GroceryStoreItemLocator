import sqlite3
from src.store import Store
from src.items import Items
from src.location import Location
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import mapper, sessionmaker, relationship

METADATA = MetaData()

class Database():
    def __init__(self, connection_string="sqlite:///foodLocationDB.sqlite3"):
        self.sqlite_file = connection_string
        self.engine = self._get_connection()
        self.store = self._map_store()
        self.items = self._map_items()
        self.location = self._map_location()
        METADATA.create_all(bind=self.engine)

    def _map_store(self):
        store = Table('Store', METADATA,
            Column('store_id', Integer, primary_key=True),
            Column('store_name', String),
            Column('image_dir', String))
        mapper(Store, store)
        return store

    def _map_items(self):
        items = Table('Items', METADATA,
            Column('item_id', Integer, primary_key=True),
            Column('item_brand', String),
            Column('item_name', String),
            Column('item_category', String),
            Column('loc_id', Integer, ForeignKey('Location.location_id')))
        mapper(Items, items)
        return items

    def _map_location(self):
        location = Table('Location', METADATA,
                         Column('location_id', Integer, primary_key=True),
                         Column('location_name', String))
        mapper(Location, location, properties={'loc_id': relationship(Items, backref='Location')})
        return location


    def _get_connection(self):
        engine = create_engine(self.sqlite_file)
        return engine

    def _get_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def _add_store(self, store):
        session = self._get_session()
        session.add(store)
        session.commit()

    def _add_item(self, item):
        session = self._get_session()
        session.add(item)
        session.commit()

    def _add_location(self, location_name):
        session = self._get_session()
        session.add(location_name)
        session.commit()

    def _search_store(self, store_id):
        session = self._get_session()
        for store in session.query(Store)\
            .filter(Store.store_id == store_id):
            session.commit()
            if store.store_id is None:
                return None
            else:
                return store.image_dir

    def _search_store_name(self, store_id):
        session = self._get_session()
        for store in session.query(Store)\
            .filter(Store.store_id == store_id):
            return store.store_name

    def _search_store_items(self, search_item):
        items_list = list()
        session = self._get_session()
        for items in session.query(Items.item_brand, Items.item_name)\
            .filter(Items.item_name.ilike('%'+search_item+'%')):
            items_list.append(items)
        return items_list
