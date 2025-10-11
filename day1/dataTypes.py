                           #DataType:

# 1.  Numeric              int, float, complex               10, 12.5, 3+4j
# 2. Text Type             str                               "Hello Tester"
# 3. Sequence Type         Sequence Type                     [1,2,3], (1,2,3), range(5)
# 4. Mapping Type          dict                              {"name": "Prakash", "age": 25}
# 5.Set Type               set, frozenset                    {1,2,3}, frozenset({1,2,3})
# 6. Boolean Type          bool                              True, False
# 7. Binary Types          bytes, bytearray, memoryview      b"test"


tools = ["Selenium", "Pytest", "Jenkins"]
tools.append("Docker")
print(tools)


#Tuple (Immutable – cannot be changed)
versions = (3.10, 3.11, 3.12)
print(versions)


browsers = {"Chrome", "Edge", "Firefox", "Chrome"}
print(browsers)  # duplicates removed


a=10;
b = float(a)
c = str(a)
print(type(b))
print(type(c))


#Dictionary (Key–Value pairs)
test_case = {
    "id": 101,
    "name": "Login Test",
    "status": "Passed"
}
print(test_case["status"])

browsers = {"Chrome", "Edge", "Firefox", "Chrome"}
print(browsers)  # duplicates removed