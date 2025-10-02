import requests
import os
from dotenv import load_dotenv

load_dotenv()  # загружаем .env


class ProjectApi:
    def __init__(self, url):
        self.url = url
        self.token = os.getenv("API_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_list_projects(self):
        resp = requests.get(f"{self.url}/projects", headers=self.headers)
        return resp.json()

    def create_progect(self, title: str):
        project = {
            "title": title,
            "users": {
                "acc0b8b1-3000-47e0-a767-7a06333c426a": "admin"
            }
        }
        resp = requests.post(f"{self.url}/projects", json=project, headers=self.headers)
        return resp.json()  # сразу возвращай весь json

    def edit_project(self, project_id: str, new_title: str):
        project = {"title": new_title}
        resp = requests.put(f"{self.url}/projects/{project_id}", json=project, headers=self.headers)
        return resp.json()

    def get_project_by_id(self, project_id: str):
        resp = requests.get(f"{self.url}/projects/{project_id}", headers=self.headers)
        return resp.json()