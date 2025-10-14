#Example1: creating tuple
# mytuple1=("apple","banana","kiwi","cherry","mango")
#
# print(mytuple1)


#Example2: access tuple item
# mytuple2=("apple","banana","kiwi","cherry","mango")
# print(mytuple2[0])
# print(mytuple2[-1])

#Example3: range of indexes
# mytuple3=("apple","banana","kiwi","cherry","mango")
#
# print(mytuple3[2:4])
#
# print(mytuple3[-4:-1])

#Example4: range the items from the tuple(we can't change the immutable value)
#by default tuple not allow you change value becz it's immutable
#but there is work around
#tuple --> list(modify)--> tuple

# mytuple3=("apple","banana","kiwi","cherry","mango")
# mylist=list(mytuple3)
# mylist[1]="Dragon fruit"
# mytuple4 =tuple(mylist)
# print(mytuple4)


#reading tuple item using loop

# mytuple5=("apple","banana","kiwi","cherry","mango")
#
# for i in mytuple5:
#     print(i)

#Example6: check if item exits(search of item in tuple)
mytuple6=("apple","banana","kiwi","cherry","mango")
if "banana" in mytuple6:
    print("yes, banana is present")
else:
    print("no, banana is not present")


#Example7 tuple length-count item
mytuple7=("apple","banana","kiwi","cherry","mango")
print(len(mytuple7))


#removing item from tuple not possible
#copying is possible, we can copy a tuple to another tuple because in copying items not cange


#join/combine tuple is possible

















