import sqlite3
from src.store import Store
from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper, sessionmaker

METADATA = MetaData()

class Database():
    def __init__(self, connection_string="sqlite:///foodLocationDB.sqlite3"):
        self.sqlite_file = connection_string
        self.engine = self._get_connection()
        self.store = self._map_store()
        METADATA.create_all(bind=self.engine)

    def _map_store(self):
        store = Table('Store', METADATA,
            Column('store_id', Integer, primary_key=True),
            Column('store_name', String),
            Column('image_dir', String))
        mapper(Store, store)
        return store

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
