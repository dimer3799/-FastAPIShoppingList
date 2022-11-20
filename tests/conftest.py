# -*- coding: utf-8 -*-
from pytest import fixture
from starlette.testclient import TestClient


@fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client
