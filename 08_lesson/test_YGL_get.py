import requests
from config import api_token

base_url = "https://ru.yougile.com/api-v2/"
heders = {
    "Authorization": f'Bearer {api_token}'
}
heders_my = heders


def test_get_project():
    # Создаём проект для теста
    resp_create = requests.post(base_url + 'projects',
                                json={"title": "Test get project"},
                                headers=heders_my)
    assert resp_create.status_code == 201
    project_id = resp_create.json().get("id")
    # Получаем проект
    resp_get = requests.get(f"{base_url}projects/{project_id}",
                            headers=heders_my)
    assert resp_get.status_code == 200
    data = resp_get.json()
    assert data["id"] == project_id


# Получение несуществующего проекта (негативная проверка)
def test_get_nonexistent_project():
    resp = requests.get(f"{base_url}projects/nonexistent-id",
                        headers=heders_my)
    assert resp.status_code == 404
