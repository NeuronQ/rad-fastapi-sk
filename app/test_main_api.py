from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app
from app.config import *


class ATestClient(TestClient):
    auth_token_ = None

    def get(self, url, **kwargs):
        self._add_token_if_any(kwargs)
        return super().get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        self._add_token_if_any(kwargs)
        return super().post(url, data=None, json=None, **kwargs)

    def patch(self, url, data=None, **kwargs):
        self._add_token_if_any(kwargs)
        return super().patch(url, data=None, **kwargs)

    def put(self, url, data=None, **kwargs):
        self._add_token_if_any(kwargs)
        return super().put(url, data=None, **kwargs)

    def delete(self, url, **kwargs):
        self._add_token_if_any(kwargs)
        return super().delete(url, **kwargs)

    def _add_token_if_any(self, kwargs):
        headers = kwargs.get("headers", {})
        if self.auth_token_:
            headers["Authorization"] = f"Bearer {self.auth_token_}"
        kwargs["headers"] = headers


def test_api_test():
    with TestClient(app) as client:
        res = client.get("/api/test")
        assert res.status_code == 200
        assert "All you need" in res.text


def test_auth_obtain_token():
    with TestClient(app) as client:
        res = client.post(
            "/api/v1/auth/token",
            data={"username": API_TEST_USER, "password": API_TEST_PASSWORD,},
        )
        rdata = res.json()
        assert rdata["access_token"]
        assert res.status_code == 200
        # auth_token = rdata['access_token']
        ATestClient.auth_token_ = rdata["access_token"]


def test_get_items_count_total():
    with ATestClient(app) as client:
        res = client.get("/api/v1/items/count")
        assert "total" in res.json()
        assert res.status_code == 200


def test_get_items_count_by():
    with ATestClient(app) as client:
        res = client.get("/api/v1/items/count", params={"by": "c_dchan_type"})
        rdata = res.json()
        assert "c_dchan_type" in rdata[0]
        assert "count" in rdata[0]
        assert res.status_code == 200


def test_get_items_list():
    with ATestClient(app) as client:
        res = client.get("/api/v1/items", params={
            "when": "today",
            "limit": 10,
            "utc_offset_h": 2,
            "dchan_type": "feed",
            "dchan_tags": "world news",
        })
        rdata = res.json()
        assert "total" in rdata
        assert len(rdata["entities"]) > -1
        assert res.status_code == 200
