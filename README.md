## Описание проекта
Yatube - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

### Функционал
Тестовый проект. Как работают формы в Django. 
Добавлены следующие функциональные возможности:

1. Добавлена форма для публикации новых записей
2. Добавлена страница редактирования записи

## Запуск проекта
1. Клонировать репозиторий:
```bash
git clone https://github.com/Ogyrecheg/hw03_forms.git
```

2. Создать и активировать виртуальное окружение:
```bash
py -3.7 -m venv venv

bash/zsh
source venv/bin/activate

Windows:
venv\Scripts\activate.bat
```
3. Обновить pip и установить зависимости из ```requirements.txt```
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции на уровне проекта:
```
cd yatube
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Запустить проект локально:
```
python3 manage.py runserver
```
7. Зарегистирировать суперпользователя Django:
```
python3 manage.py createsuperuser
```

**Технологии:**
- Python
- Django

### Автор проекта:
[Шевченко Александр](https://github.com/Ogyrecheg)
