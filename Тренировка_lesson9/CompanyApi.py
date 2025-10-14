import requests
import allure


class CompanyApi:
    # Инициализация
    def __init__(self, url):
        self.url = url

    @allure.step("api. Получить список компаний через API")
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url+'/company/list', params=params_to_add)
        return resp.json()

    # Передаем параметры в название степа — имя и пароль пользователя
    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["user_token"]

    @allure.step("api. Получить компанию по {id}") #Передаем id из параметра
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    # Передаем в название степа название компании и в скобках — ее описание
    @allure.step("api. Создать компанию {name} ({description})")
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company/create', json=company)
        return resp.json()

    # Передаем параметры в название степа — id компанинии, название и описание   
    @allure.step("api. Редактировать компанию {new_id}. {new_name} ({new_descr})")
    def edit_company(self, new_id, new_name, new_descr):
        # Получаем токен
        client_token = self.get_token()

        # Формируем URL с параметром client_token
        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"

        # Вызываем словарь и кладем в него описание компании
        company = {
            "name": new_name,
            "description": new_descr
        }
        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.patch(url_with_token, json=company)

        # Результат вернется в JSON, мы его прокинем в тест
        return resp.json()

    @allure.step("api. Удалить компанию {id}")
    def delete_company(self, id):
        client_token = self.get_token()

        # Формируем URL с параметром client_token
        url_with_token = f"{self.url}/company/{id}?client_token={client_token}"

        # Метод отправляет DELETE-запрос
        resp = requests.delete(url_with_token)

        # Возвращаем JSON-ответ
        return resp.json()

    # В названии степа — id (де)активированной компании и ее статус
    @allure.step("api. (Де)активировать компанию {id} -> {is_active}")
    def set_active_state(self, id, is_active):
        client_token = self.get_token()

        url_with_token = f"{self.url}/company/status_update/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token,
                              json={"is_active": is_active})        
        return resp.json()

