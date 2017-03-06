####
#World Map
####
import sys
class Character(object):
    def __init__(self, name, hp, mp, defense, attack):
        self.attack = attack
        self. name = name
        self.health = hp
        self.bag = []
        
    def pick_up(self, item):
        self.bag.append(item)
        print "You put the %s in your bag." % item
        
    def attack(self, target):
        target.take_damage(self.attack)
        print "You attack %s for %d damage." % (target.name, self.attack)
    def take_damage(self, damage):
        self.health -= damage
class Room():
    def __init__(self, the_name, n, e, s, w, u, d, the_description):
        self.name = the_name
        self.description = the_description
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.up = u
        self.down = d
        
        
    def move(self, direction):
#This function allows movement to a different node.
        global node 
        node = globals()[getattr(self,direction)]

#Rooms
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
Liege = Room('Liege, Belgium', None, 'Berlin', 'Switzerland', 'London', None, None,\
'There is a waffle store near you.')
Washington = Room('Washington DC', None, 'Ocean', None, 'Plato', None, None,\
'Woodrow Wilson recently gave his inaugural speech, but the\
US hasn\'t entered the Great War yet')
Paris = Room('Paris, France', 'London', None, None, 'Ocean', None, None,\
'You can see the eiffel tower')
Ocean = Room('The Pacific Ocean', None, 'Paris', None, 'Washington', None, None,\
'6,000 kilometers of blue water')
Switzerland = Room('Switzerland', 'Liege', 'Sarajevo', 'Gallipoli', None, None, None,\
'A completely neutral country, there is almost nothing to\
do here.')
Gallipoli = Room('Gallipoli, Italy', 'Switzerland', 'Constantinople', None, None, None, None,\
'The Central Powers have completely taken this area over.\
 Watch your step!')

Constantinople = Room('Constantinople, Ottoman Empire', 'Moscow', None, None, 'Gallipoli', None, None,\
'Capital of the Ottoman Empire, there are many people looking\
 at you with a concerned face')
Sarajevo = Room('Sarajevo, Austria-Hungary', None, None, None, 'Switzerland', None, None,\
'The hearth of this brutal war.\
 You can see Austro-Hungarian solders down the street.')
Moscow = Room('Moscow, Russian Empire', None, 'Maze', 'Constantinople', None, None, None,\
'Very cold. Atleast the Central Powers haven\'t \
 invaded yet...')

Plato = Room('Plato, Missouri', None, 'Washington', None, 'Fresno', None, None,\
'The mean center of the US population')
Philidelpha = Room('Philidelphia, Pennsylvania', 'New_York', None, 'Washington', None, None, None,\
'You can smell the Liberty bell where you are standing, or\
 it could be a cheesesteak...')
New_York = Room('New York, New York', None, None, 'Philidelphia', None, None, None,\
'Most populous US city.')
Fresno = Room('Fresno, California', None, 'Plato', None, None, None, None,\
'Agricultural center. There is a small shack that you can see\
in the corner')
Berlin = Room('Berlin, Germany', None, None, None, 'Liege', None, None,\
'Capital of the German Empire "Hallo!"')

Maze = Room('Start of Confusing Tundra', 'Maze3', 'Maze2', None, 'Moscow', None, None,\
'It\'s cold and you don\'t know where to go.')
Maze2 = Room('Confusing Tundra: This looks familiar...', 'Maze5', 'Maze4', None, 'Maze', None, None,\
'Your starting point')
Maze3 = Room('Confusing Tundra: This looks familiar...', None, None, 'Maze', None, None, None,\
'It\'s cold and you don\'t know where to go.')
Maze4 = Room('Confusing Tundra: This looks familiar...', None, 'Tokyo', None, 'Maze2', None, None,\
'It\'s cold and you don\'t know where to go.')
Maze5 = Room('Confusing Tundra: This looks familiar...', None, None, 'Maze2', None, None, None,\
'It\'s cold and you don\'t know where to go.')
Tokyo = Room('Tokyo, Japan', None, None, None, 'Maze4', None, None,\
'Capital of the Japanese Empire.')


        
        




#static variables
#Controller
node =  London
directions = ['north','south','east','west','up','down']
short_directions = ['n','s','e','w','u','d']
is_alive = True

while is_alive:
    print node.name
    print node.description

    #Ask for input
    command = raw_input('> ')
    if command in ['q','quit','exit']:
        sys.exit(0)
   
    print ""
        #Allows us to change nodes
    if command in short_directions:
        command = directions[short_directions.index(command)]

        
    try:
        node.move(command)
        
    except:
        print 'You can\'t'

