#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implementing a SingletonType metaclass:
"""


class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class MySingleton(object):
    __metaclass__ = SingletonType

    def __init__(self):
        pass

# Cons: Other than some people considering metaclasses to be black magic,
# none that I can think of (besides general ‘singletons are evil’ complaints).
