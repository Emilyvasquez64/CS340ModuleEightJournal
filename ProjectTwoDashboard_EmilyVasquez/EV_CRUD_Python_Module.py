from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self):
        """
        Initialize the MongoClient and establish connection to MongoDB
        Connects to the aac database and animals collection
        """
        # Connection Variables
        USER = 'aacuser'
        PASS = 'Apple' 
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            print("Connection successful")
        except Exception as e:
            print(f"Connection failed: {e}")
            raise
    
    def create(self, data):
        """
        Insert a document into the MongoDB animals collection
        
        Args:
            data (dict): A dictionary containing key/value pairs for the document
            
        Returns:
            bool: True if successful insert, False otherwise
        """
        if data is not None:
            try:
                # Insert the document into the collection
                result = self.collection.insert_one(data)
                # Check if the insert was successful by verifying an _id was created
                if result.inserted_id:
                    return True
                else:
                    return False
            except Exception as e:
                # Log the exception for debugging purposes
                print(f"An error occurred during insert: {e}")
                return False
        else:
            # Raise exception if data parameter is empty
            raise Exception("Nothing to save, because data parameter is empty")
    
    def read(self, query):
        """
        Query for documents from the MongoDB animals collection
        
        Args:
            query (dict): A dictionary containing key/value lookup pairs
                         for the MongoDB find operation
        
        Returns:
            list: A list of documents if successful, empty list otherwise
        """
        if query is not None:
            try:
                # Use find() to query the collection
                cursor = self.collection.find(query)
                # Convert cursor to list to return results
                result_list = list(cursor)
                return result_list
            except Exception as e:
                # Log the exception for debugging purposes
                print(f"An error occurred during read: {e}")
                return []
        else:
            # Return empty list if query parameter is None
            print("Query parameter is empty")
            return []
    def update(self, query, update_data):
        """
        Update document(s) in the MongoDB animals collection
        
        Args:
            query (dict): A dictionary containing key/value lookup pairs to find documents
            update_data (dict): A dictionary containing the update operations (e.g., {"$set": {...}})
            
        Returns:
            int: The number of documents modified
        """
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(query, update_data)
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            print("Query or update data parameter is empty")
            return 0
    
    def delete(self, query):
        """
        Delete document(s) from the MongoDB animals collection
        
        Args:
            query (dict): A dictionary containing key/value lookup pairs to find documents to delete
            
        Returns:
            int: The number of documents deleted
        """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            print("Query parameter is empty")
            return 0