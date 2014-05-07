#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alexandre'

import unittest
import logging
import os
from datetime import timedelta
from config import ImmutableDict, Config


class Config_TestCase(unittest.TestCase):
    def setUp(self):
        #: Default configuration parameters.
        self.default_config = ImmutableDict({
            'DEBUG': False,
            'TESTING': False,
            'PROPAGATE_EXCEPTIONS': None,
            'PRESERVE_CONTEXT_ON_EXCEPTION': None,
            'SECRET_KEY': None,
            'PERMANENT_SESSION_LIFETIME': timedelta(days=31),
            'USE_X_SENDFILE': False,
            'LOGGER_NAME': None,
            'SERVER_NAME': None,
            'APPLICATION_ROOT': None,
            'SESSION_COOKIE_NAME': 'session',
            'SESSION_COOKIE_DOMAIN': None,
            'SESSION_COOKIE_PATH': None,
            'SESSION_COOKIE_HTTPONLY': True,
            'SESSION_COOKIE_SECURE': False,
            'MAX_CONTENT_LENGTH': None,
            'SEND_FILE_MAX_AGE_DEFAULT': 12 * 60 * 60,  # 12 hours
            'TRAP_BAD_REQUEST_ERRORS': False,
            'TRAP_HTTP_EXCEPTIONS': False,
            'PREFERRED_URL_SCHEME': 'http',
            'JSON_AS_ASCII': True,
            'JSON_SORT_KEYS': True,
            'JSONIFY_PRETTYPRINT_REGULAR': True,
        })

        self.c = Config("", self.default_config)

    def test_create_config_object(self):

        self.assertIsInstance(self.c, Config)

    def test_access_config_attr(self):

        self.assertFalse(self.c["DEBUG"])

    def test_change_with_config_file(self):

        config_file = os.path.join(os.path.dirname(__file__), "test.cfg")
        print ("current dir", os.getcwdu())
        print("config file :", config_file)

        self.c.from_pyfile(config_file)

        self.assertTrue(self.c["DEBUG"])
        self.assertEqual(self.c["LOG_LEVEL"], logging.INFO)

    def test_wrong_config_attr(self):
        with self.assertRaises(KeyError) as cm:
            self.c["ERROR_LEVEL"]

        the_exception = cm.exception
        self.assertEqual('ERROR_LEVEL', the_exception.message)

    def test_is_singleton(self):
        config2 = Config("", self.default_config)

        self.assertTrue(config2["DEBUG"])


if __name__ == '__main__':
    unittest.main()
