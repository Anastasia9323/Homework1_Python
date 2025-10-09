from UsersTable import UsersTable

db = ("postgresql://postgres:oatkorg13@localhost:5432/postgres")


def test_insert(insert):
    user_email = insert
    email_in_db = db.get_user_by_email(user_email)
    assert email_in_db == user_email


def test_update(update):
    user_email = update
    email_in_db = db.get_user_by_email(user_email)
    assert email_in_db == "aaa@aaa.com"


def test_delete(delete):
    user_email = delete
    email_in_db = db.get_user_by_email(user_email)
    assert email_in_db is None
    
