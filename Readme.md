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
