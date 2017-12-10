class Location(object):
    def __init__(self, location_name, location_id=None):
        self.location_name = location_name
        self.location_id = location_id


    def __repr__(self):
        return '{lid}:{ln}' \
               .format(lid=self.location_id, ln=self.location_name)

    def __str__(self):
        return self.__repr__()