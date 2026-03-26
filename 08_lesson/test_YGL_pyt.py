import requests
from config import api_token

base_url = "https://ru.yougile.com/api-v2/"
heders = {
    "Authorization": f'Bearer {api_token}'
}
heders_my = heders


# Обновление существующего проекта (позитивная проверка)
def test_update_project():
    # Создаем проект
    resp_create = requests.post(base_url + 'projects',
                                json={"title": "Проект для обновления"},
                                headers=heders_my)
    assert resp_create.status_code == 201
    project_id = resp_create.json().get("id")
    # Обновляем проект
    update_data = {
        "title": "Обновленный проект",
        "deleted": False
    }
    resp_update = requests.put(f"{base_url}projects/{project_id}",
                               json=update_data, headers=heders_my)
    assert resp_update.status_code == 200
    # Проверяем обновление
    resp_get = requests.get(f"{base_url}projects/{project_id}",
                            headers=heders_my)
    assert resp_get.json()["title"] == "Обновленный проект"


# Удаление проекта (негативная проверка)
def test_delete_nonexistent_project():
    resp = requests.delete(f"{base_url}projects/nonexistent-id",
                           headers=heders_my)
    assert resp.status_code == 404
