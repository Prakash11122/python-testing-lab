# class MyClass:
#     def myfun(self):  #this is method 1
#         pass
#     def display(self,name):   #this is method 2
#         print(name)
#
# obj1=MyClass()  #Object creation as assine to object to object reference
# obj1.myfun()   #Here i'm calling myfun() method using MyClas object reference (onj1)
# obj1.display("scott")


#Example2
# class MyClass:
#     def m1(self):  #this is instance method
#         print("this is instance method...")
#
#     @staticmethod   #this is static method
#     def m2(self,num):
#         print(self,num)
#
# mc = MyClass()
# mc.m1()
# # mc.m2(100,200)  #here calling static method through class object
# MyClass.m2(10,20)  # 10, 20 # here calling static method  m2() directly using class name not through object

#Example 3
# class MuClass:
#     a,b=11,12  #this is class level variable
#     def add(self):   #here we can't access directly class level varible in method level so we can use self ke word for access class level variable in method level
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc = MuClass()  #here object created
# mc.add() #here i'm call add() methos using class reference
# mc.mul() #here i'm call mul() methos using class reference


#Example4
# i,j=15,25   # global variables
# class MyClass:
#     a,b=10,20   # class variables
#     def add(self,x,y):
#         print("Local variable",x+y)  #x, y are local variables
#         print(self.a+self.b)  # a, b are class variables
#         print(i+j)   # i, j are global variables
#
# mc=MyClass()
# mc.add(100,200)




# Example5:

# a,b=15,25   # global variables
# class MyClass:
#     a,b=10,20   # class variables
#     def add(self,a,b):
#         print(a+b)  # local varaibles
#         print(self.a+self.b)  # class variables
#         print(globals()['a']+globals()['b'])  # global variables
#
# mc=MyClass()
# mc.add(100,200)

#Example6: once class can have multiple ojects
class MyClass:
    def display(self,name):
        print("this is display method....")
        print(name)

obj1=MyClass()
obj1.display("john")

obj2=MyClass()
obj2.display("scott")

#EXAMPLE7: constructor example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#     def m1(self):
#         print("hello...")
#     def m2(self,x,y):
#             return(x+y)
#
# mc=MyClass()    # invke constructor automatically
# mc.m1()  # method we have call explicitely by using object
# print(mc.m2(10,20))  # 20












