# course_work_5
Создаем список id 10 работодателей (в дальнейшем будем использовать их для связи таблиц "employers" и "vacancies")
С помощью API сайта hh.ru в файле "utils_api_hhru.py" получаем данныые о работодателях и вакансиях,
используя библиотеку requests.
С помощью pdAdmin создаем базу данных PostgreSQL "course_work_5",
таблицы "employers" и "vacancies" (все sql - команды прописаны в файле sql_commands).
Для работы с БД используем библиотеку "psycopg2".
В файле "main.py" реализован код для заполнения таблиц "employers" и "vacancies" данными.
В файле "DBManager.py" создаем класс DBManager для работы с данными в БД.