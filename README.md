# QA-auto-python
на ветке e2e-test - решение задачи E2E
на ветке github-api-test - решение задачи Github Api

Тестовое задание QA 
E2E UI

Цель:
Создать автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium или Playwright. Тест должен проверять процесс от авторизации до завершения покупки, с возможностью легко воспроизвести его на любом компьютере.
Требования:
1. Сценарий теста:
Тест должен выполнять следующие действия на сайте saucedemo.com:
Авторизация: Использовать тестовый аккаунт:
Логин: standard_user
Пароль: secret_sauce
Выбор товара: Выбрать один товар (например, "Sauce Labs Backpack") и добавить его в корзину.
Оформление покупки:
Перейти в корзину и убедиться, что товар добавлен.
Оформить покупку, заполнив поля
Завершить покупку.
Проверка: Убедиться, что покупка завершена успешно.
Ожидаемый результат:
Кандидат должен предоставить готовый репозиторий с проектом, который можно развернуть и запустить по инструкции в README.md. Тест должен корректно авторизоваться на сайте, выбрать товар, оформить покупку и проверить успешное завершение покупки.


GitHub API

Цель
Создать автоматический тест для проверки работы с GitHub API на языке Python. Тест должен уметь создавать, проверять наличие и удалять репозиторий на GitHub. Необходимо предоставить решение, которое легко воспроизводимо на любом компьютере.

Требования
Использование GitHub API:
Скрипт должен использовать API GitHub для выполнения следующих операций:
Создание нового публичного репозитория.
Проверка списка репозиториев для подтверждения создания.
Удаление репозитория.
Использование переменных окружения:
Входные данные (имя пользователя GitHub, токен API и имя репозитория) должны передаваться через переменные окружения или файл конфигурации .env.
Зависимости:
Зависимости должны быть описаны в файле requirements.txt.
Необходимые библиотеки (пример): requests и python-dotenv.
Инструкция по запуску:
Проект должен содержать файл README.md с подробной инструкцией, как установить зависимости, настроить переменные окружения и запустить тест.
Структура проекта:
Проект должен содержать следующие файлы:
test_api.py — основной скрипт с тестом.
.env — файл с переменными окружения (необходимо указать пример).
requirements.txt — файл с зависимостями.
README.md — инструкция по установке и запуску.
Ожидаемый результат
Кандидат должен предоставить готовый репозиторий с проектом, который можно развернуть и запустить по инструкции в README.md. Тест должен корректно создавать, проверять и удалять репозиторий на GitHub.
