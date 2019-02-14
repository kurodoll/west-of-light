import json

from entity import Entity
from systems import server, client, gameWindow  # noqa: F401


class Controller:
    def __init__(self):
        self.entities = []
        self.components = {}
        self.systems = {}

        self.running = True

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

        if component_data['requiresSystem'] not in self.systems:
            self.initSystem(component_data['requiresSystem'])

        return component_data

    def initSystem(self, system):
        target_object = system + '.' + system[0].capitalize() + system[1:] + 'System()'  # noqa: E501
        self.systems[system] = eval(target_object)

    def tick(self):
        for s in self.systems:
            if s in self.components:
                for c in self.components[s]:
                    ret = self.systems[s].update(c)

                    if ret == 'exit':
                        self.running = False
