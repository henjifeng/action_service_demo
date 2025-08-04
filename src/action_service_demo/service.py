from pymongo.collection import Collection

def create_user(collection: Collection, name: str, email: str) -> dict:
    user = {"name": name, "email": email}
    result = collection.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return user