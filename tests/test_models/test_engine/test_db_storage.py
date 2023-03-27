#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "This test only works with DBStorage")
class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage"""

    @classmethod
    def setUpClass(cls):
        """Set up database connection and initialize session"""
        cls.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                   .format(os.getenv('HBNB_MYSQL_USER'),
                                           os.getenv('HBNB_MYSQL_PWD'),
                                           os.getenv('HBNB_MYSQL_HOST'),
                                           os.getenv('HBNB_MYSQL_DB')),
                                   pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    def setUp(self):
        """Create a new instance of DBStorage and initialize database"""
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """Remove all data from the tables"""
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        """Close the database connection"""
        cls.session.close()

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_all(self):
        """Test the all() method of DBStorage"""
        objects = self.storage.all()
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)
        self.assertEqual(len(objects), 0)

    def test_new(self):
        """Test the new() method of DBStorage"""
        state = State(name="California")
        self.storage.new(state)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        key = "{}.{}".format(type(state).__name__, state.id)
        self.assertIsNotNone(objects[key])

    def test_save(self):
        """Test the save() method of DBStorage"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = "{}.{}".format(type(state).__name__, state.id)
        objects = self.storage.all()
        self.assertIsNotNone(objects[key])

    def test_delete(self):
        """Test the delete() method of DBStorage"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = "{}.{}".format(type(state).__name__, state.id)
        objects = self.storage.all()
        self.assertIsNotNone(objects[key])
        self.storage.delete(state)
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

    def test_reload(self):
        """Test the reload() method of DBStorage"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = "{}.{}".format(type(state).__name__, state.id)
        self.assertIsNotNone(self.storage.all()[key])


if __name__ == "__main__":
    unittest.main()
