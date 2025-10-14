import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

@allure.epic("компании") 
@allure.severity("blocker")
@allure.id("SKYPRO-1")
@allure.story("Получение компаний")
@allure.feature("READ")
@allure.title("Получение полного списка организаций")
def test_get_companies():
    with allure.step("Получить список компаний через API"):
        api_result = api.get_company_list()
    with allure.step("Получить список компаний через БД"):
        db_result = db.get_companies()
    with allure.step("Сравнить размеры 2х списков"):
        assert len(api_result) == len(db_result)


@allure.epic("компании") 
@allure.severity("blocker")
@allure.id("SKYPRO-2")
@allure.story("Получение компаний")
@allure.feature("READ")
@allure.title("Получение полного списка активных организаций")
@allure.description("Запрос организаций с параметром active = true")
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)


@allure.epic("компании") 
@allure.severity("blocker")
@allure.id("SKYPRO-3")
@allure.story("Создание компаний")
@allure.feature("CREATE")
@allure.title("Получение организации по id")
def test_add_new():
    with allure.step("Получить количество организаций ДО"):
        body = api.get_company_list()
        len_before = len(body)
    with allure.step("Создать организацию"):
        with allure.step("Сгенерировать название"):
            name = "Autotest"
            descr = "Descr"

    with allure.step("Вызвать API-метод для создания"):
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("Проверить поля новой организации. Корректно заполнены"):
        for company in body:
            if company["id"] == new_id:
                assert company["name"] == name
                assert company["description"] == descr
                assert company["id"] == new_id
    
    with allure.step("Получить количество организаций после"):
        body = api.get_company_list()
        len_after = len(body)

    with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
        assert len_after - len_before == 1

    with allure.step("Удалить из БД новую организацию"):
        db.delete(new_id)


@allure.epic("компании") 
@allure.severity("blocker")
@allure.id("SKYPRO-4")
@allure.story("Получение компании по id")
@allure.feature("UPDATE")
def test_get_one_company():
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()
    new_company = api.get_company(max_id)
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["isActive"] is True


@allure.epic("компании") 
@allure.severity("blocker")
@allure.id("SKYPRO-5")
# изменить информацию о компании
def test_edit():
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit_company(max_id, new_name, new_descr)

    db.delete(max_id)

    assert edited["name"] == new_name
    assert edited["description"] == new_descr


@allure.id("SKYPRO-6")
# удалить компанию
def test_delete():
    # Добавили компанию через базу:
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    # Проверили по ID, что компании нет в базе:
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0


@allure.id("SKYPRO-7")
# деактивировать компанию
def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False


@allure.id("SKYPRO-8")
# деактивировать и снова активировать компанию
def test_deactivate_and_activate_back():
    # Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(new_id, False)
    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)
    
    # Проверяем, что компания активная
    assert body_a["is_active"] is True
