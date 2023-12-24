# **************************************************************************** #
#                                                                              #
#                                                       -------------          #
#    optimizer.py                                       |     ____  |  P       #
#                                                       |    / __ \ |  l       #
#    By: jeremy <jeremy@plextech.net>                   |   / /_/ / |  e       #
#                                                       |  / .___/  |  x       #
#    Created: 2019/10/30 15:17:23 by jeremy             | /_/       |  u       #
#    Updated: 2019/10/30 16:04:27 by jeremy             |           |  s       #
#                                                       -------------          #
#                                                                              #
# **************************************************************************** #

import os
import random
import time

GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
NC = '\033[0m'
BREAK = '--------------------------------------------------------------------------------------'

print(BREAK)
print("Welcome to the PC optimizing program!")
print(BREAK)
print("")
print("Press enter to begin optimization")
input(">")

load = ['|', '/', '-', '\\']
spinCounter = 1
i = 0

while(True):
    os.system("clear")
    os.system("echo '"+BLUE+"' "+str(i)+"% Optimized  '"+load[spinCounter]+"' '"+NC+"'")
    print("<{}>".format("#"*i))
    spinCounter+=1
    time.sleep(0.3)
    if spinCounter > 3:
        spinCounter = 0
    if(random.randint(0,1) == 1):
        i+=1
    if i == 100:
        break

os.system("echo '"+GREEN+"' Done! '"+NC+"'")
speed = random.randint(37, 86)
print("Congratualions, you're PC is now {}% fast! :)".format(speed))
