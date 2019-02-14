from .system import System

from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.RemoveUser(self)


class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.users = WeakKeyDictionary()

    def Connected(self, channel, addr):
        self.AddUser(channel)

    def AddUser(self, user):
        self.users[user] = True
        print(user.addr, 'connected')

    def RemoveUser(self, user):
        print(user.addr, 'disconnected')
        del self.users[user]

    def Tick(self):
        self.Pump()


class ServerSystem(System):
    def __init__(self):
        System.__init__(self)

    def update(self, component):
        if 'game_server' not in component:
            component['game_server'] = GameServer(
                localaddr=(component['host'], component['port'])
            )

        component['game_server'].Tick()
