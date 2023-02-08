from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class cases_types(str, Enum):
    openzaak = "openzaak"
    gzac = "gzac"

class create_access_levels(BaseModel):
    access_levels_name: str
    cases_id: int
    class Config():
        orm_mode = True

class access_levels(BaseModel):
    access_levels_name: str
    class Config():
        orm_mode = True

class create_cases(BaseModel):
    cases_name: cases_types
    roles_id: int
    cases_identifier: str
    class Config():
        orm_mode = True

class cases(BaseModel):
    cases_name: str
    access_levels: List[access_levels]
    cases_identifier: str
    class Config():
        orm_mode = True

class create_roles(BaseModel):
    roles_name:str
    class Config():
        orm_mode = True

class roles(BaseModel):
    roles_name:str
    cases_name: List[cases] = []
    class Config():
        orm_mode = True