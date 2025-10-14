from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class CompanyTable:
    __scripts = {
		"select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
		"select_active": text("SELECT * FROM company "
                        "WHERE \"is_active\" = true AND deleted_at IS NULL"),
		"delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
		"insert_new": text("INSERT INTO company(\"name\") values (:new_name)"),
		"get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
		"select by id": text("SELECT * FROM company WHERE id =:select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Запросить список организаций")
    def get_companies(self):
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("БД. Запросить организацию по {id}") # Добавили ID из параметра
    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall() 
    
    @allure.step("БД. Запросить список ативных организаций")
    def get_active_companies(self):
        query = self.__db.execute(self.__scripts["select_active"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("БД. Удалить организацию по {id}") # Добавили ID из параметра
    def delete(self, id):
        query = self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Создать организацию с названием {name}")
    def create(self, name):
        query = self.__db.execute(self.__scripts["insert_new"], new_name=name)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Получить максимальный id организации")
    def get_max_id(self):
        query = self.__db.execute(self.__scripts["get_max_id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]
    
    
    