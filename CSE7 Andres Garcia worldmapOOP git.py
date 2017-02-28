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
'This is the way out of the cave')

beach = Room("The Beach", None, None, 'ocean', 'cave exit', None, None, "This is the way to the ocean")

deadmansMountain = Room("Dead mans mountain", 'cave exit', None, 'mudslideclimb', None, None, None, \
'This mountain will kill you even if you can survive')

jungle = Room("The Jungle", 'cave exit', 'treepath', None, 'monkey mayhem', None, 'wolfden', \
'This place is filled with wild animals')

ocean = Room("The Ocean", None, 'shark territorry', 'volcano', 'beach', None, None, \
'This is a world of terror')

mudslideclimb = Room("Mudslideclimb", 'dead mans mountain', 'mammothgraveyard', None, None, None, None, \
'This is the slippery part of the mountain')

mammothGraveyard = Room("Mammoth graveyard", 'mudslideclimb', None, 'dessert', None, 'sharkterritory', \
None, 'This is where mammoths come to die')

dessert = Room("Dessert", 'sharkterritory', None, None, None, None, None, \
'This is the hottest place on earth')

monkeyMayhem = Room("Monkey mayhem", 'grassy fields', None, 'jungle', 'river', 'redwood', None, \
'This is monkey territory')

wolfden = Room("Wolf den", 'bone tunnel', 'wolf bed', None, None, None, None, 'This is the way closer')

#Controller

node = bearCave
is_alive = True
directions = ['north','south','east','west','up,','down']
short_directions =['n','s','e','w','u','d'] 
   
while is_alive:
    print node.name
    print node.description
    ut('> ')
    if command in ['q']
    sys.exit(0)
     
     if command in short_directions:
         command = directions[short_directions.index(command)]
     try:
          name_of_node = node.paths[command]
          node = world_map[node.paths[command]]        
         except:
             print 'You Can\'t'
             sys.exit(0)