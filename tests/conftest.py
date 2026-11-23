import copy

import pytest
from fastapi.testclient import TestClient

import src.app


BASELINE_ACTIVITIES = copy.deepcopy(src.app.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange shared state: restore in-memory activities before each test
    src.app.activities = copy.deepcopy(BASELINE_ACTIVITIES)
    yield


@pytest.fixture
def client():
    return TestClient(src.app.app)
