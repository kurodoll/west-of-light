from .system import System
from PodSixNet.Connection import connection, ConnectionListener


class Client(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))

    def Tick(self):
        connection.Pump()
        self.Pump()

    def Network_connected(self, data):
        print('Connected to the server')

    def Network_error(self, data):
        print('Error:', data)
        connection.Close()

    def Network_disconnected(self, data):
        print('Disconnected from the server')
        exit()


class ClientSystem(System):
    def __init__(self):
        System.__init__(self)

    def update(self, component):
        if 'client' not in component:
            component['client'] = Client(
                component['host'],
                int(component['port'])
            )

        component['client'].Tick()
