# Task Management

Простое REST API для управления задачами, построенное на FastAPI и SQLAlchemy с асинхронной поддержкой.

## 🛠 Технологии
- **Python 3.12+**
- **FastAPI** - веб-фреймворк
- **SQLAlchemy 2.0** - ORM
- **SQLite** (с асинхронным драйвером aiosqlite)
- **Pydantic v2** - валидация данных

## ⚙️ Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/название-репозитория.git

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
   
## 🚀 Запуск
      python3 main.py


## 🔍 API Endpoints

| Метод | Эндпоинт | Описание                | Пример запроса                      |
|-------|----------|-------------------------|-------------------------------------|
| POST  | `/tasks` | Добавление новой задачи | `{"name": "Сделать ДЗ", "description": "По математике"}` |
| GET   | `/tasks` | Получение списка задач  | Не требуется                        |

## 📁 Структура проекта

🗄 Структура проекта

📦# 🏗️ Структура проекта

```bash
├── main.py
├── database.py
├── schemas.py
├── repository.py
├── router.py
└── requirements.txt
