def calculate(n, **kwargs):
    print(kwargs)  # prints a dictionary with the arguments and value as {key: value} pair.

    # To get the key/value, we could do something like:
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # Or
    # print(kwargs["add"])
    # print(kwargs["multiply"])

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)


# We can use the **kwargs in our class
class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)  # prints None, if the argument is not given in Car().

# If a key is not present in our: def __init__ (e.g. self.model = kw["model"]), we can use the .get() keyword. The benefit is that is does not throw an error. We would use it like this: self.model = kw.get("model"). If the key argument is not present, the output will be: None
