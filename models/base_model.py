#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key.value in kwargs.item():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
                    models.storage.new(self)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        def save(self):
            """

            """
            self.update_at = datetime.utcnow()
            models.storage.save()

            def to_dict(self):
                """

                """
                inst_dict = self.__dict__.copy()
                int_dict["__class__"] = self.__class__.__name__
                inst_dict["created_at"] = self.created_at.isoformat()
                inst_dict["updated_at"] = self.updated_at.isoformat()

                return inst_dict

            def __str__(self):
                """

                """
                classe_name = self.__class__.__name__
                return "[{}] ({}) {}".format(class_name.self.id.self.__dict__)
            if __name__ == "__main__":
                my_model = BaseModel()
                my_model.name = "My First Model"
                my_model.my_number = 89
                print(my_model)
                my_model.save()
                print(my_model)
                my_model_json = my_model.to_dict()
                print(my_model_json)
                print("JSON of my_model:")
                for key in my_model_json.keys():
                    print("\t{}:({})-{}".format(key, type(my_model_json[key]), my_model_json[key]))
