import pytest
from action_service_demo.core import add

def test_add():
    assert add(2, 3) == 5