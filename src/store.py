# data model for the store table


class Store(object):
    def __int__(self, store_id, image_id, dairy_loc, produce_loc, protein_loc, frozen_loc, grain_loc):
        self.store_id = store_id
        self.image_id = image_id
        self.dairy_loc = dairy_loc
        self.produce_loc = produce_loc
        self.protein_loc = protein_loc
        self.frozen_loc = frozen_loc
        self.grain_loc = grain_loc

    def __repr__(self):
        return '{sid}:{iid} \n' \
               '{dl} \n' \
               '{pdl} \n' \
               '{ptl} \n' \
               '{fl} \n' \
               '{gl} \n' \
               .format(sid=self.store_id, iid=self.image_id, dl=self.dairy_loc,
                       pdl=self.produce_loc, ptl=self.protein_loc,
                       fl=self.frozen_loc, gl=self.grain_loc)

    def __str__(self):
        return self.__repr__()
