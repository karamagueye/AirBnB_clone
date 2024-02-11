#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
     """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):

        """
        Tests for init
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

        def test_save(self):

            """
            Test for save method
            """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())

    def test_str(self):
        """
        Test for string representation
        """

    my_model = BaseModel()

    self.assertTrue(str(my_model).startswith('[BaseModel]'))
    self.assertIn(my_model.id, str(my_model))
    self.assertIn(str(my_model.__dict__), str(my_model))

    if __name__ == "__main__":
        unittest.main()



