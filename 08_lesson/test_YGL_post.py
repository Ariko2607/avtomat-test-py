import requests
from config import api_token

base_url = "https://ru.yougile.com/api-v2/"
heders = {
    "Authorization": f'Bearer {api_token}'
}
heders_my = heders


# создание проекта (позитивная проверка)
def test_create_project():
    creads = {
        "title": "Test Project"
        }
    resp = requests.post(base_url+'projects', json=creads, headers=heders_my)
    assert resp.status_code == 201


# создание проекта с пустым названием (неготивная проверка)
def test_create_project_negotiv():
    creads = {
        "title": ""
        }
    resp = requests.post(base_url+'projects', json=creads, headers=heders_my)
    assert resp.status_code == 400
