import random

import pytest


@pytest.fixture
def simple_rand():
    return random.random()


@pytest.fixture
def rand():
    def f():
        return random.random()
    return f


@pytest.fixture
def fixture_1(rand):
    return rand()


def test_1(simple_rand):
    assert simple_rand == simple_rand


def test_2(rand):
    assert rand() != rand()