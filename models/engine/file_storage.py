#!/usr/bin/python3
"""This is the module that defines a class to
manage file storage for hbnb clone"""
import json


class FileStorage:
    """This is the class that manages storage
of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """This returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        dct = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                dct[key] = self.__objects[key]
        return dct

    def new(self, obj):
        """This adds new object to storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """This saves storage dictionary to file"""
        with open(self.__file_path, 'x') as g:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, g)

    def reload(self):
        """This loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 's') as g:
                temp = json.load(g)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' This deletes the object obj from the attribute
            __objects if it's inside it
        '''
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        if obj_key in self.__objects.keys():
            del self.__objects[obj_key]

    def close(self):
        """ This calls the reload method"""
        self.reload()
