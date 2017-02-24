####
#World Map
####
import sys
class Room():
    def __init__(self, the_name, N, E, S, W, U, D, the_description):
        self.name = the_name
        self.description = the_description
        self.north = N
        self.east = E
        self.south = S
        self.west = W
        self.up = U
        self.down = D
        
        
    def move(self, direction):
#This function allows movement to a different node.
        global node 
        node = globals()[getattr(self.direction)]
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
Liege = Room('London, United Kingdom', None, 'Berlin', 'Switzerland', 'London', None, None,\
'There is a waffle store near you.')
Washington = Room('Liege, Belgium', None, 'Ocean', None, 'Plato', None, None,\
'Woodrow Wilson recently gave his inaugural speech, but the\
US hasn\'t entered the Great War yet')
Paris = Room('London, United Kingdom', 'London', 'Switzerland', None, 'Ocean', None, None,\
'You can see the eiffel tower')
Ocean = Room('The Pacific Ocean', None, 'Paris', None, None, 'Washington', None,\
'6,000 kilometers of blue water')
Switzerland = Room('Switzerland', 'North', 'Sarajevo', 'Gallipoli', None, None, None,\
'Your starting point')
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
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')
London = Room('London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,\
'Your starting point')

'''
#static variables
#Controller
is_alive = True
while is_alive:
    
    #Ask for input
    command = raw_input('> ')
    if command in ['q','quit','exit']:
        sys.exit(0)
    print node
        #Allows us to change nodes
    if command in  :
        command = 
    try:
        node = globals()[getattr(self.direction)]
    except:
        print 'You can\'s'
        
