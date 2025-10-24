import sys
sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package2")
sys.path.append("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day9/package3")


#approach-1

# import emp
# empobj=emp.Employee(101,"prakash",4000000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.Student(11,"prakash",'A')
# stuobj.displaystu()

#approach-2

from emp import Employee
empobj=Employee(111,"Hanuman",1000)
empobj.displayemp()



from stu import Student
stuobj=Student(1,"krishna",200)
stuobj.displaystu()




