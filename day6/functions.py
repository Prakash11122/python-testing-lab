#Example-1  Syntax of function

# def myFun():
#     print("Hello")
# myFun() #Here we can call the function using function name

#Example-2

# def myfun1(name):
#     print("Hello",name)
# myfun1("prakaash")

#Example-2
# def cal(a,b):
#     return (a+b)
# sum=cal(11,11)
# print(sum)

#Example-3
# def func():
#     return
# print(func())#none

#Example-4
# def func():
#     i=10
# print(func()) #none

#Example-5
# def cal(a,b):
#     return (a+b)
# print(cal(11,1))

#✅ Example 2 — Function with Parameters

# def add_numbers(a, b):
#     return a + b
#
# result = add_numbers(10, 5)
# print("Sum is:", result)

# ✅ Example 3 — Function with Default Argument

# def greet_user(name="Tester"):
#     print("Welcome,", name)
#
# greet_user()
# greet_user("Prakash")

#✅ Example 5 — Function in Testing Context
def validate_login(username, password):
    if username=="Admin" and password=="prakash@12":
        return "Login successful"
    else:
        return "Login fail"
print(validate_login("Admin", "prakash@12"))
print(validate_login("user", "prakash@12"))




