import sys

from day9.pack1.module1 import display

sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/pack1")

#approach1
# import module1
# import module2
#
# module1.display()
# module2.show()

#approach2
from module1 import *
from module2 import *

display()
show()



