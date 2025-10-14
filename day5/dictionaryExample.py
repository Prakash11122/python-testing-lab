# mydic={
#     "brand":"Hyudai",
#     "model":"i20",
#     "year":"2023"
# }

# print(mydic["brand"])
# print(mydic["model"])


#using get()

# print(mydic.get("brand"))

#change the value in dictionary

# print(mydic)
# mydic["year"]=2024
# print(mydic)




# Creating a simple dictionary
# test_data = {
#     "username": "admin",
#     "password": "1234",
#     "expected_result": "Login Successful"
# }

# print(test_data)

#1️⃣ Accessing Values using key
# print(test_data["username"])
# print(test_data["password"])


# Adding a new key-value pair

# test_data["url"]="http:8080/Admin/pasword"
# test_data["password"]="prakash@12"
# print(test_data)

# Delete a specific key
# test_data.pop("username")
# print(test_data)

# del test_data["url"]

# Remove all items
# test_data.clear()
# print(test_data)

#4️⃣ Dictionary Length
# print(len(test_data))

# 5️⃣ Looping Through a Dictionary
# You can loop through keys, values, or both.
#
# for dic in test_data:
#     print(dic, ":" ,test_data[dic])


#keys() — Get all keys
test_data = {"username": "admin", "password": "1234", "result": "Success"}
print(test_data.keys())
#Get all values
print(test_data.values())

# Get all key-value pairs
print(test_data.items())









