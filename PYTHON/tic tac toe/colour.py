from enum import Enum
class Color():
    red = "red"
    green = "green"
    blue = "blue"
print (Color.red)
#enum
#ininstance(Color.green,Color)
#True
print(repr(Color.red))

from subprocess import call

call('color a', shell=True) #this sets the color to light green
print('The quick brown fox jumps over the lazy dog.')


import time
from subprocess import call

for color in('a', 'e', 'c'): #cycles through different colours
    call('cls', shell=True) #clears the screen
    call('color ' + color, shell=True)
    print('The quick brown fox jumps over the lazy dog.')
    time.sleep(1)

input("\nPress enter to exit. ")

class bcolors:
    WARNING = '\033[95m'
    ENDC = '\033[0m'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
