import pytest

db = ("postgresql://postgres:oatkorg13@localhost:5432/postgres")


@pytest.fixture
def insert():
    user_id = 111
    user_email = "abc@abc.ru"
    db.create(user_id, user_email)
    yield user_email


@pytest.fixture
def update():
    user_email = "aaa@aaa.com"
    user_id = 111
    db.update(user_email, user_id)


@pytest.fixture
def delete():
    user_email = "abc@abc.ru"
    db.create(user_email)
    db.delete(user_email)