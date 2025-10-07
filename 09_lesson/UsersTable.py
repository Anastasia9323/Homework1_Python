from sqlalchemy import create_engine
from sqlalchemy.sql import text


class UsersTable:
    __scripts = {
        "insert_new": text("INSERT INTO users (\"user_id\", \"user_email\") values (:new_user_id, :new_user_email)"),
        "update": text("UPDATE users SET (\"user_email\") WHERE user_id = :new_user_id"),
        "deleted_by_user_email": text("DELETE FROM users WHERE user_email = :new_user_email")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, user_id, user_email):
        self.__db.execute(self.__scripts["insert_new"], new_user_id=user_id, new_user_email=user_email)

    def update(self, user_email, user_id):
        self.__db.execute(self.__scripts["update"], new_user_email=user_email, new_user_id=user_id)

    def delete(self, user_email):
        self.__db.execute(self.__scripts["deleted_by_user_email"], new_user_email=user_email)
        