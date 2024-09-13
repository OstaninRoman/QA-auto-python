# QA-auto-python
автоматический тест для работы с GitHub API на Python

1. Установите зависимости(requests, python-dotenv):
     pip install -r requirements.txt
2. В файле data.env задайте переменным окружения значения:
     GITHUB_TOKEN: Ваш GitHub токен с правами на создание и удаление репозиториев.
     GITHUB_USERNAME: Ваш GitHub логин.
     REPO_NAME: Имя репозитория, который будет создан во время теста.
3. Запустите тест с помощью Python-скрипта:
     python test_api.py
