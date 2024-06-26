#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                loaded_objects = json.load(f)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value
                    cls = globals()[class_name]
                    obj_instance = cls(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def classes(self):
        """Return a dictionary of supported classes for serialization"""
        from models import __all__ as models
        supported_classes = {}
        for model in models:
            cls = globals().get(model)
            if cls and issubclass(cls, BaseModel):
                supported_classes[model] = cls
        return supported_classes
