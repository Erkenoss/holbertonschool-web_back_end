#!/usr/bin/env python3
""" function that lists all documents in a collection """


def list_all(mongo_collection):
    """ return a list of all docs """
    return list(mongo_collection.find())
