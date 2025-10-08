from UsersTable import UsersTable

db = ("postgresql://postgres:oatkorg13@localhost:5432/postgres")


def test_insert(insert):
    user_email = insert
    assert user_email is not None


def test_update(update):
    user_email = update
    assert user_email == "aaa@aaa.com"


def test_delete(delete):
    user_email = delete
    assert user_email is None
