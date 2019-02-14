import json

from entity import Entity
from systems import server
from systems import client


class Controller:
    def __init__(self):
        self.entities = []
        self.components = {}

        self.systems = {}
        self.systems['server'] = server.ServerSystem()
        self.systems['client'] = client.ClientSystem()

    def newEntity(self, component_list):
        new_entity = Entity(component_list)
        self.entities.append(new_entity)
        return new_entity

    def newComponent(self, variant):
        with open('components/' + variant + '.json') as f:
            component_data = json.load(f)

        if variant not in self.components:
            self.components[variant] = []

        self.components[variant].append(component_data)
        return component_data

    def tick(self):
        for s in self.systems:
            if s in self.components:
                for c in self.components[s]:
                    self.systems[s].update(c)
