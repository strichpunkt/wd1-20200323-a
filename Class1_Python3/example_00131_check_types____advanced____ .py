print(type(1))                           # <type 'int'>
print(type(1.))                          # <type 'float'>
print(type(1+3j))                        # <type 'complex'>
print(type("hello"))                     # <type 'str'>
print(type([1,2,3]))                    # <type 'list'>     # mutable
print(type((1,2,3)))                     # <type 'tuple'>    # immutable
print(type({"name": "pat", "age": 12}))  # <type 'dict'>


# use is_instance to check the type, they will give a bool
print(isinstance(1, int))    # True
print(isinstance(1, float))  # False
print(isinstance(1, str))    # False
