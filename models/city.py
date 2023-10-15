#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
        Summary: Definning the City class that inherits from BaseModel
        Public class attributes:
            name string - empty string
            state_id - empty string (it will be the State.id)
    """
    name = ""
    state_id = ""
