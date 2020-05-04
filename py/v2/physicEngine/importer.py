#external imports
import sys
import numpy
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, sys.path[0]+'\..\class')
sys.path.insert(1, sys.path[0]+'\..\gameEngine')
sys.path.insert(1, sys.path[0]+'\..\graphicEngine')
sys.path.insert(1, sys.path[0]+'\..\ressources')

from box import *
from particle import *
from physicEngine import *
from renderer import *
