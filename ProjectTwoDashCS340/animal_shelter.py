import os
import pymongo
from pymongo import MongoClient

class AnimalShelter:
    def __init__(self):
        username = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASS')
        host = os.getenv('MONGO_HOST', 'localhost')
        port = os.getenv('MONGO_PORT', 27017)
        
        # Create MongoDB client connection
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/animal_shelter?authSource=admin')
        self.database = self.client['animal_shelter']

    def create(self, data):
        if data is not None:
            self.database.outcomes.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    def read(self, criteria):
        if criteria is not None:
            data = self.database.outcomes.find(criteria, {"_id": False})
            return list(data)
        else:
            raise Exception("Nothing to read, because criteria parameter is empty")

    def update(self, criteria, new_data):
        if criteria is not None:
            result = self.database.outcomes.update_many(criteria, {"$set": new_data})
            return result.modified_count
        else:
            raise Exception("Nothing to update, because criteria parameter is empty")
    
    def delete(self, criteria):
        if criteria is not None:
            result = self.database.outcomes.delete_many(criteria)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, because criteria parameter is empty")
