from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com/api-v2")


def test_positive_create_project():
    project = api.create_progect("Тестовый проект")
    project_id = project["id"]

    got = api.get_project_by_id(project_id)
    assert got["title"] == "Тестовый проект"


def test_negative_create_project():
    bad_project = {"title": ""}  # пустое название
    resp = requests.post(f"{base_url}/projects", json=bad_project, headers=headers)
    assert resp.status_code == 400


def test_positive_edit_project():
    project = api.create_progect("Тестовый проект")
    project_id = project["id"]

    edited = api.edit_project(project_id, "Домашняя работа")
    assert edited["title"] == "Домашняя работа"


def test_negative_edit_project():
    fake_id = "123"
    resp = requests.put(f"{base_url}/projects/{fake_id}", json={"title": "abc"}, headers=headers)
    assert resp.status_code == 404                                                        


def test_positive_get_project_by_id():
    project = api.create_progect("Домашняя работа")
    project_id = project["id"]

    got = api.get_project_by_id(project_id)
    assert got["id"] == project_id


def test_negative_get_project_by_id():
    fake_id = "123"
    resp = requests.get(f"{base_url}/projects/{fake_id}", headers=headers)
    assert resp.status_code == 404