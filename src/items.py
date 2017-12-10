class Items(object):
    def __init__(self, item_brand, item_name, item_category, loc_id, item_id=None):
        self.item_brand = item_brand
        self.item_name = item_name
        self.item_category = item_category
        self.loc_id = loc_id
        self.item_id = item_id



    def __repr__(self):
        return '{iid}:{ib} {ina} \n'\
                     '{ic} - {lid}'\
               .format(iid=self.item_id, ib=self.item_brand, ina=self.item_name, ic=self.item_category, lid=self.location_id)

    def __str__(self):
        return self.__repr__()