# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, sys.path[0]+'\..\class')
sys.path.insert(1, sys.path[0]+'\..\physicEngine')
sys.path.insert(1, sys.path[0]+'\..\graphicEngine')
sys.path.insert(1, sys.path[0]+'\..\ressources')

from particle import *
from box import *
from physicEngine import *
from collisionEngine import *
from renderer import *