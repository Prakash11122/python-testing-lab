# import sys
# sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package1")
# sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package1/package2")

# import module1
# module1.display()

# import module2
# module2.show()

#approach-2
import sys

from day9.package1.module1 import display

sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package1")
sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package1/package2")

from module1 import *
from module2 import *

display()
show()

