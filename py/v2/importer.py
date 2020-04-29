# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, sys.path[0]+'\class')
sys.path.insert(1, sys.path[0]+'\gameEngine')
sys.path.insert(1, sys.path[0]+'\graphicEngine')

from particle import *
from physicEngine import *
from renderer import *