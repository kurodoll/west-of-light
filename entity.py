import itertools


class Entity:
    uid = itertools.count()

    def __init__(self, component_list):
        self.uid = next(Entity.uid)
        self.components = component_list
