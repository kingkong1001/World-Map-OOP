class Room(object):
    def __init__(self, name, north, south, east, west, up, down, desc):
        self.name = name
        self.description = desc
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]

bearCave = Room("The Bear's cave",'entrance','tunnels',None, None, None, None, 'This is where the giant cave bear lives')
