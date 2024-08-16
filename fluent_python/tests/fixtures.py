import pytest

from fluent_python.card_deck import FrenchDeck


@pytest.fixture
def create_deck():
    return FrenchDeck()


@pytest.fixture(params='spades diamonds clubs hearts'.split())
def suit(request):
    return request.param


@pytest.fixture(params=[str(n) for n in range(2, 11)] + list('JQKA'))
def rank(request):
    return request.param
