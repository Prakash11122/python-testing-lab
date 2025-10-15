#Exmaple-1
# global_val=20  #global varibale

# def func():
#     local_val =10 #local variable
#     print(local_val)
#     print(global_val)
# func()

# print(local_val) #invalid
# print(global_val) #valid

#Exmaple-2

# xy=100  #global varibale
#
# def cool():
#     xy=200 #local variable
#     print(xy)
# cool()

#Exmaple-3 i want to change the global variable value inside the function

num=11.11
def getGlobal():
    global num
    num =11
    print(num)
getGlobal()





































