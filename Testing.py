# Testing.py
# Reference Guide: Unit Testing with pytest, fixtures, and mocking in Python

# ==========================================
# 1. INTRODUCTION TO PYTEST
# ==========================================
# To run tests, install pytest: `pip install pytest`
# Test files must be named `test_*.py` or `*_test.py`.
# Functions to test must be prefixed with `test_`.

def add(a, b):
    return a + b

# Basic assertion test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# ==========================================
# 2. FIXTURES
# ==========================================
# Fixtures provide a fixed baseline (setup/teardown data) for tests to run on.
try:
    import pytest
    
    @pytest.fixture
    def sample_user_data():
        return {"username": "alice", "role": "admin"}

    def test_user_role(sample_user_data):
        assert sample_user_data["username"] == "alice"
        assert sample_user_data["role"] == "admin"
except ImportError:
    # Safe fallback if pytest is not installed locally
    pass

# ==========================================
# 3. MOCKING
# ==========================================
# Mocking replaces parts of your system under test with mock objects 
# to isolate it from external interfaces (like API requests or DB).
from unittest.mock import Mock

def test_api_call():
    # Create a mock api client
    mock_client = Mock()
    # Configure return value for a method
    mock_client.get_status.return_value = "Success"
    
    # Assertions
    status = mock_client.get_status()
    assert status == "Success"
    mock_client.get_status.assert_called_once()

# Running the file directly triggers pytest if installed
if __name__ == "__main__":
    print("Testing documentation references configured! Run using `pytest Testing.py` in your terminal.")
