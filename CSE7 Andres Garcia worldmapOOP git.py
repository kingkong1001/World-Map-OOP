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

bearCave = Room("The Bear's cave", 'entrance', 'tunnels', None, None, None, None, 'This is where the giant cave bear lives')

entrance = Room("The Entrance", None, 'bearcave', None, None, None, None, 'This is where you came in')

tunnel = Room("The Tunnel", 'bearcave', 'stream', 'waterfall', 'quicksand', None, None, 'This will get you closer to the exit')

stream = Room("The Stream", 'tunnel', None, 'waterfall', 'quicksand', None, None, 'This is the bottom of the waterfall')

quicksand = Room("The Quicksand", 'tunnel', None, 'stream', None, None, None, 'This is the bottom of the waterfall')

waterfall = Room("The Waterfall", 'tunnel', None, 'caveexit', 'stream', None, None, 'This has a path to the exit')

caveExit = Room("The Cave exit", None, 'jungle', 'beach', 'waterfall', None, 'deadmansmountain', \
"This is the way out of the cave")

beach = Room("The Beach", None, None, 'ocean', 'caveexit', None, None, "This is the way to the ocean")

deadmansMountain = Room("Dead mans mountain", 'caveexit', None, 'mudslideclimb', None, None, None, \
'This mountain will kill you even if you can survive')

jungle = Room("The Jungle", 'Exit', 'treepath', None, 'monkey mayhem', None, 'wolfden', \
'This place is filled with wild animals')