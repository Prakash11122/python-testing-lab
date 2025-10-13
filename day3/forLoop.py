#forLoop
#print 1.....10 number using for loop

# for i in range(10):
#     print(i)


# print 5.10,15,20...100

# for i in range(5,100,5):
#     print(i)

#✅ Example 1 – Simple Loop
# for i in range(5):
#     print("Iteration",i)

#✅ Example 2 – Loop through a List

# tools = ["Python", "Selenium", "Pytest", "Jenkins"]
#
# for tool in tools:
#     print("Learning:", tool)

#✅ Example 3 – Loop with Condition

# for num in range(1,6):
#     if num%2==0:
#         print(num, "num is even")
#     else:
#         print(num, "num is odd")
#



#while-loop

#✅ Example 1 – Selenium-style Loop

# attempt = 1
# while attempt <= 3:
#     print("Trying to connect to server... Attempt", attempt)
#     attempt += 1


for num in range(1, 6):
   if num==3 or num==4:
       continue
   print(num)





