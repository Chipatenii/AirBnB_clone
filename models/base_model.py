#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """Representing my base class model"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """prints string representation"""

        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates my public instance attribute
            updated_at with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary containing all keys/values of
            __dict__ of the instance:
        """

        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        if isinstance(dict_obj["created_at"], datetime):
            dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        if isinstance(dict_obj["updated_at"], datetime):
            dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()

        return dict_obj
