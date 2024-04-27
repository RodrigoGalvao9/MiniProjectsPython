import pymongo
from pymongo import MongoClient
from fastapi import FastAPI

connection_string = ""
client = MongoClient(connection_string)

if client:
    print("conectando ao servidor")
