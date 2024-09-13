import os
import requests
from dotenv import load_dotenv
import pathlib

current_dir = pathlib.Path(__file__).parent
dotenv_path = current_dir / 'data.env'
load_dotenv(dotenv_path)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')

assert GITHUB_TOKEN is not None, "GITHUB_TOKEN не установлен!"
assert GITHUB_USERNAME is not None, "GITHUB_USERNAME не установлен!"
assert REPO_NAME is not None, "REPO_NAME не установлен!"

BASE_URL = f"https://api.github.com/user/repos"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repo():
    print(f"Создание репозитория {REPO_NAME}...")
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(BASE_URL, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Репозиторий {REPO_NAME} успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.status_code} - {response.text}")

def check_repo_exists():
    print(f"Проверка существования репозитория {REPO_NAME}...")
    repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(repo_url, headers=headers)
    if response.status_code == 200:
        print(f"Репозиторий {REPO_NAME} существует.")
    else:
        print(f"Репозиторий {REPO_NAME} не найден: {response.status_code} - {response.text}")

def delete_repo():
    print(f"Удаление репозитория {REPO_NAME}...")
    repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(repo_url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий {REPO_NAME} успешно удалён.")
    else:
        print(f"Ошибка при удалении репозитория: {response.status_code} - {response.text}")

if __name__ == "__main__":
    create_repo()
    check_repo_exists()
    delete_repo()
    check_repo_exists()
