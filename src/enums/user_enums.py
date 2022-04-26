from enum import Enum
from src.basedclasses.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(PyEnum):
    inactive = "inactive"
    active = "active"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"


#print(Statuses.list())