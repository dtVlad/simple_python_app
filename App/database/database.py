import pymongo
from gridfs import GridFS
from flask_pymongo import PyMongo

class Database(object):
    DATABASE = None
    FS = None

    def initialize(app):
        mongo = PyMongo(app)
        Database.DATABASE = mongo.db
        Database.FS = GridFS(mongo.db)


    # @staticmethod
    # def insert(collection, data):
    #     Database.DATABASE[collection].insert(data)

    # @staticmethod
    # def find_all(collection):
    #     return Database.DATABASE[collection].find({})

    @classmethod
    def get_all(cls, collection):
        data = Database.DATABASE[collection].find({})
        return [d for d in data]

    @staticmethod
    def insert_image(collection, img, content_type, filename):
        fields_id = Database.FS.put(img, content_type=content_type, filename=filename)
        Database.DATABASE[collection].insert({"filename": str(filename), "fields": fields_id})
         
