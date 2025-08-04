下面是一个\*\*快速一步步在当前目录构建 Python 项目（PMD 风格）\*\*的方法，适合基于 `pytest` 进行集成测试，也兼顾可维护性和清晰结构。

---

## ✅ 一键式结构（当前目录）

假设当前目录是 `action_service_demo/`，你可以运行以下命令快速初始化结构：

### 🧱 创建文件结构

```bash
mkdir -p src/action_service_demo
mkdir -p tests/integration
touch src/action_service_demo/__init__.py
touch tests/integration/__init__.py
touch requirements.txt
touch pytest.ini
touch README.md
```

---

## ✅ 示例业务逻辑代码

**`src/action_service_demo/core.py`**:

```python
def add(x, y):
    return x + y
```

---

## ✅ 示例集成测试

**`tests/integration/test_core.py`**:

```python
import pytest
from action_service_demo.core import add

def test_add():
    assert add(2, 3) == 5
```

---

## ✅ `pytest.ini` 配置

```ini
[pytest]
pythonpath = src
testpaths = tests
```

---

## ✅ 安装依赖

```bash
python3 -m venv venv
source venv/bin/activate

pip install pytest
pip freeze > requirements.txt
```

---

## ✅ 运行测试

```bash
pytest
```

---

## ✅ 最小 `.gitignore` 示例（可选）

```bash
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

---

## ✅ 最终结构

```bash
action_service_demo/
├── src/
│   └── action_service_demo/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── integration/
│       ├── __init__.py
│       └── test_core.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

需要我生成一个脚本一键初始化以上结构吗？例如 `init_project.sh`？
















下面是一个完整示例，演示如何为 **Python 服务集成 MongoDB**，并实现一个集成测试：**新增用户到 MongoDB 的功能**。

---

## 📦 项目结构（简洁版）

```
your_project/
├── src/
│   └── your_project/
│       ├── __init__.py
│       └── service.py           # 用户服务逻辑
├── tests/
│   └── integration/
│       └── test_service.py      # 集成测试
├── requirements.txt
├── pytest.ini
└── .gitignore
```

---

## ✅ 1. 安装依赖

```bash
pip install pymongo pytest
pip freeze > requirements.txt
```

---

## ✅ 2. 业务代码（`src/your_project/service.py`）

```python
# src/your_project/service.py

from pymongo.collection import Collection

def create_user(collection: Collection, name: str, email: str) -> dict:
    user = {"name": name, "email": email}
    result = collection.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return user
```

---

## ✅ 3. 配置 `pytest.ini`

```ini
[pytest]
pythonpath = src
testpaths = tests
```

---

## ✅ 4. 集成测试代码（`tests/integration/test_service.py`）

```python
# tests/integration/test_service.py

import pytest
from pymongo import MongoClient
from your_project.service import create_user

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
```

---

## ✅ 5. Docker 启动 MongoDB（开发调试用）

```bash
docker run -d \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=testuser \
  -e MONGO_INITDB_ROOT_PASSWORD=testpass \
  --name local-mongo \
  mongo:6
```

---

## ✅ 6. 运行测试

```bash
pytest
```

---

## ✅ 补充建议

如果你希望这段逻辑用于生产，可以封装成如下结构：

```python
class UserService:
    def __init__(self, collection: Collection):
        self.collection = collection

    def create(self, name: str, email: str) -> dict:
        return create_user(self.collection, name, email)
```

---

是否需要我补充：

* GitHub Actions 的 CI 示例
* `act` 本地测试配置
* 使用 `docker-compose` 启动 MongoDB + App？

你可以选择补充方向。
