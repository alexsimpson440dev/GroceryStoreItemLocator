class Store(object):
    def __init__(self, store_id, store_name, image_dir):
        self.store_id = store_id
        self.store_name = store_name
        self.image_dir = image_dir


    def __repr__(self):
        return '{sid}:{sn} - {id}' \
               .format(sid=self.store_id, sn=self.store_name, id=self.image_dir)

    def __str__(self):
        return self.__repr__()
