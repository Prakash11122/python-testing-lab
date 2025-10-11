import keyword

user_input= input("Enter a keyword")

if user_input in keyword.kwlist:
    print(f"{user_input} is a python keyword")
else:
    print(f"{user_input} is not a pyhon keyword")