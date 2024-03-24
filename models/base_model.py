#!/usr/bin/python3
"""Defines the BaseModel class."""


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    pass
