#!/usr/bin/env python
# -*- coding: utf-8 -*-

#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alexandre'

import unittest
from datetime import timedelta
from config import ImmutableDict, Config


class Config_TestCase(unittest.TestCase):
    def setUp(self):

        #: Default configuration parameters.
        self.default_config = ImmutableDict({
                                'DEBUG':                                False,
                                'TESTING':                              False,
                                'PROPAGATE_EXCEPTIONS':                 None,
                                'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
                                'SECRET_KEY':                           None,
                                'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
                                'USE_X_SENDFILE':                       False,
                                'LOGGER_NAME':                          None,
                                'SERVER_NAME':                          None,
                                'APPLICATION_ROOT':                     None,
                                'SESSION_COOKIE_NAME':                  'session',
                                'SESSION_COOKIE_DOMAIN':                None,
                                'SESSION_COOKIE_PATH':                  None,
                                'SESSION_COOKIE_HTTPONLY':              True,
                                'SESSION_COOKIE_SECURE':                False,
                                'MAX_CONTENT_LENGTH':                   None,
                                'SEND_FILE_MAX_AGE_DEFAULT':            12 * 60 * 60, # 12 hours
                                'TRAP_BAD_REQUEST_ERRORS':              False,
                                'TRAP_HTTP_EXCEPTIONS':                 False,
                                'PREFERRED_URL_SCHEME':                 'http',
                                'JSON_AS_ASCII':                        True,
                                'JSON_SORT_KEYS':                       True,
                                'JSONIFY_PRETTYPRINT_REGULAR':          True,
                                })


    def test_CriaConfigObject(self):
        
        c = Config("", self.default_config)

        self.assertIsInstance(c, Config)


if __name__ == '__main__':
    unittest.main()
