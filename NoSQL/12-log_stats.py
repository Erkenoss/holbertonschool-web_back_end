#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def nginx_logs_stats(mongo_collection):
    """ script that provides some stats about Nginx logs stored in MongoDB """
    try:
        total_logs = mongo_collection.count_documents({})
        print(f"Total logs: {total_logs}")

        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            count = mongo_collection.count_documents({"method": method})
            print(f"\t{method}: {count}")

        special_logs_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
        print(f"GET requests to /status: {special_logs_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')

    db = client.logs
    collection = db.nginx

    nginx_logs_stats(collection)

    client.close()
