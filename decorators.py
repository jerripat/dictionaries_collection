import time


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles to ice cream")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge to ice cream")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} of ice cream")


get_ice_cream('Vanilla')
