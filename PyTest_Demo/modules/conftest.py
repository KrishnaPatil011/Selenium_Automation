import pytest

@pytest.fixture()  # decorator
def setup():
    print("launching browser")
    print("open application")
    yield
    print("closing browser")