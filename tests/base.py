# -*- coding: utf-8 -*-
import unittest
from api_teste.models import db
from api_teste.app import create_app
from flask_testing import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.app.config = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        db.create_all()

    def tearDown(self):
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
