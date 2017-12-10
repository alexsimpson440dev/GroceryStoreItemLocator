class Location(object):
    def __init__(self, location_id, location):
        self.location_id = location_id
        self.location = location


    def __repr__(self):
        return '{lid}:{l}' \
               .format(lid=self.location_id, l=self.locaiton)

    def __str__(self):
        return self.__repr__()