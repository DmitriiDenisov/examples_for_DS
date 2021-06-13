from dataclasses import dataclass
from typing import NamedTuple
from enum import Enum
from mypy_extensions import TypedDict


# THIS FILE COMPARES THREE STRUCTURES: typedict, NamedTuple and dataclass


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


# Class definition: Almost the same
@dataclass
class UserDataC:
    name: str
    gender: Gender


class UserTuple(NamedTuple):
    name: str
    gender: Gender


class UserNDict(TypedDict):
    name: str
    gender: Gender


# Object Creation: Looks the same
anna_datac = UserDataC(name="Anna", gender=Gender.FEMALE)
anna_tuple = UserTuple(name="Anna", gender=Gender.FEMALE)
anna_ndict = UserNDict(name="Anna", gender=Gender.FEMALE)

# 1. Mutable values vs frozen values
anna_datac.gender = Gender.MALE
# anna_tuple.gender = Gender.MALE  # AttributeError: can't set attribute
anna_ndict["gender"] = Gender.MALE
# AttributeError: 'dict' object has no attribute 'gender'
# anna_ndict.gender = Gender.MALE

# 2. New attribute
# Note that you can add new attributes like this.
# Python will not complain. But mypy will.
anna_datac.password = "secret"  # Dataclasses are extensible
# anna_tuple.password = "secret"  # AttributeError - named tuples not
# anna_ndict.password = "secret"  # AttributeError - TypedDict not
anna_ndict["password"] = "secret"

# 3. isinstance
assert isinstance(anna_tuple, tuple)
assert isinstance(anna_ndict, dict)

# 4. Operation of ==
anna_tuple_1 = UserTuple(name="Anna", gender=Gender.FEMALE)
anna_tuple_2 = UserTuple(name="Anna", gender=Gender.FEMALE)
anna_tuple_3 = UserTuple(name="AnnaNew", gender=Gender.FEMALE)
print(anna_tuple_2 == anna_tuple_1)
print(anna_tuple_2 == anna_tuple_3)


# ---------------------------
# CONCLUSION: I would go for NamedTuple if possible and if I want the values to be frozen.
# Otherwise I would use a dataclass.
# Source: https://stackoverflow.com/a/63218574

# Now how to redeclare some functions:
class Point(NamedTuple):
    name: str
    x: float
    y: float

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.name + other.name, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.name + other.name, self.x - other.x, self.y - other.y)


point_1 = Point('A', 1, 3)
point_2 = Point('B', 4, 5)
print(point_1 + point_2)
print(point_1 - point_2)
