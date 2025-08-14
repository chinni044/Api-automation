import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """Fixture to initialize API client once per test session."""
    return APIClient()
