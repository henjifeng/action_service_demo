import pytest
from pymongo import MongoClient
from action_service_demo.service import create_user

@pytest.fixture(scope="module")
def mongo_collection():
    client = MongoClient("mongodb://testuser:testpass@localhost:27017/")
    db = client.testdb
    collection = db.users
    collection.delete_many({})  # 清空集合
    yield collection
    collection.delete_many({})
    client.close()

def test_create_user(mongo_collection):
    user = create_user(mongo_collection, "Alice", "alice@example.com")
    assert user["name"] == "Alice"
    assert "email" in user

    # 验证是否真的插入数据库
    from_db = mongo_collection.find_one({"name": "Alice"})
    assert from_db is not None
    assert from_db["email"] == "alice@example.com"