import pprint

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    yield TestClient(app)

@pytest.mark.asyncio
async def test_get_advertisements(client):
    params = {
        "request": ['a','b','c']
    }
    resp = client.get(url='http://localhost:8082/repository', params=params)
    result = resp.json()
    pprint.pprint(result)
