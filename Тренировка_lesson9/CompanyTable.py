from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    __scripts = {
		"select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
		"select_active": text("SELECT * FROM company "
                        "WHERE \"is_active\" = true AND deleted_at IS NULL"),
		"delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
		"insert_new": text("INSERT INTO company(\"name\") values (:new_name)"),
		"get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
		"select by id": text("SELECT * FROM company "
                        "WHERE id =:select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select_active"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    def create(self, name):
        self.__db.execute(self.__scripts["insert_new"], new_name=name)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]
    
    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall()
    
    