import sys
from controller import Controller

if __name__ == '__main__':
    c = Controller()

    if len(sys.argv) > 1 and sys.argv[1] == '-s':
        server = c.newEntity([
            c.newComponent('server')
        ])

    else:
        client = c.newEntity([
            c.newComponent('client')
        ])

    while True:
        c.tick()
