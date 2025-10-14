#how to create a list
# mylist=[10,20,30,40,40]
# mylist1=["apple","bababa","oranage","lichi"]


# mylist2=["apple","bababa",10,11]



# print(mylist)
# print(mylist1)

# print(mylist2)


#accessing item from the list

# fruit=["apple","bababa",10,11,"orange",12]
# print(fruit[2])
# print(fruit[3])
# print(fruit[-1])

#Example 3 :Range of indexes
# myFruits=["banana","mango","kiwi","lichi","papaya","coconut"]
# print(myFruits[2:5])
# print(myFruits[-2])


#example 4 Range of indexes
# myFruits1=["banana","mango","kiwi","lichi","papaya","coconut"]
#
# print(myFruits1)
#
# myFruits1[1]="mangooo"
#
# print(myFruits1)


#example 5 read the list using loop
# myFruits2=["banana","mango","kiwi","lichi","papaya","coconut"]
# for i in myFruits2:
#     print(i)

#example 6 check if the item is present or  not in the list

# myFruits3=["banana","mango","kiwi","lichi","papaya","coconut"]
# if "mango" in myFruits3:
#     print("yes in the list")

#example 7 length of list

# myFruits4=["banana","mango","kiwi","lichi","papaya","coconut"]
#
# print(len(myFruits4))

#example 8 add item in the list insert(), append()

#
# myFruits5=["banana","mango","kiwi","lichi","papaya","coconut"]
#
# myFruits5.append("pinapple")
# print(myFruits5)
#
# myFruits5.insert(2,"lichi")
# print(myFruits5)

#example9 remove item from the list
# myFruits6=["banana","mango","kiwi",]

#pop()
# myFruits6.pop(1)
# print(myFruits6)

##del
# del myFruits6[1]
# print(myFruits6)

#clear()
# myFruits6=["banana","mango","kiwi",]
# myFruits6.clear()
# print(myFruits6)

#copy from one list to another list

# myFruits7=["banana","mango","kiwi"]
# myFruits8 = list(myFruits7)
# print(myFruits8)

#Example 11 combine/join lists
# list1=[11,22,33,44]
# list2=[55,66,77,88]
# list3 = list1+list2
# print(list3)
# print(list1+list2)

list1=[11,22,33,44]
list2=["A","B","C"]

for i in list2:
    list1.append(i)
print(list1)