#syntax

def function_name(parameters):
    # block of code
    return "value"

#Example 1
def greet():
    print("Welcome to Automation Testing!")
greet()


#Example 2
def add_numbers(a,b):
    return a+b
result =add_numbers(1,1)
print(result)

#Example 3

def validate_login(expected, actual):
    if expected == actual:
        print("✅ Login Test Passed")
    else:
        print("❌ Login Test Failed")
validate_login("Success", "Success")

















