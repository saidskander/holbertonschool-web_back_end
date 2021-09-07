#!/usr/bin/env python3
"""log_stats"""
from pymongo import MongoClient


def dictint(a: dict) -> int:
    """return log"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(a)


def nginx():
    """ get some Nginx stats stored in MongoDB """
    print(f"{dictint({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {dictint({'method': 'GET'})}")
    print(f"\tmethod POST: {dictint({'method': 'POST'})}")
    print(f"\tmethod PUT: {dictint({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {dictint({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {dictint({'method': 'DELETE'})}")
    print(f"{dictint({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
