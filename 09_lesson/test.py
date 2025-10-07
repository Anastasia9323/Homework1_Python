from UsersTable import UsersTable
import pytest

db = ("postgresql://postgres:oatkorg13@localhost:5432/postgres")

@pytest.fixture
def test_insert():
    user_id = 111
    user_email = "abc@abc.ru"
    db.create(user_id, user_email)

    assert user_id == 111
    assert user_email == "abc@abc.ru"


def test_update():
    user_email = "aaa@aaa.com"
    user_id = 111
    db.update(user_email, user_id)

    assert user_email == "aaa@aaa.com"

def test_delete():
    user_email = "abc@abc.ru"
    db.create(user_email)
    db.delete(user_email)

    assert 
