import psycopg2

from utils_api_hhru import list_employer_id, get_employer_name, get_info_vacancies


def fill_table_employers():
    """
    Заполняет таблицу employers данными
    """
    try:
        with psycopg2.connect(host='localhost',
                              database='course_work_5',
                              user='postgres',
                              password='1432') as conn:
            with conn.cursor() as cur:
                for employer_id in list_employer_id:
                    cur.execute('INSERT INTO employers Values(%s, %s)', (employer_id, get_employer_name(employer_id)))

    finally:
        conn.close()


def fill_vacancies_table():
    """
    Заполняет таблицу vacancies данными
    """
    try:
        with psycopg2.connect(host='localhost',
                              database='course_work_5',
                              user='postgres',
                              password='1432') as conn:
            with conn.cursor() as cur:
                count_vacancy = 0
                for employer_id in list_employer_id:
                    for vacancy in get_info_vacancies(employer_id)['items']:
                        cur.execute('INSERT INTO vacancies VALUES(%s, %s, %s, %s, %s, %s)',
                                    (
                                                                            count_vacancy + 1,
                                                                            employer_id,
                                                                            vacancy['name'],
                                                                            vacancy['salary']['from'],
                                                                            vacancy['salary']['to'],
                                                                            vacancy['alternate_url']
                                    )
                                    )

                        count_vacancy += 1

    finally:
        conn.close()


def truncate_tables():
    """
    Удаляет данные из таблиц 'employers' и 'vacancies'
    """
    try:
        with psycopg2.connect(host='localhost',
                              database='course_work_5',
                              user='postgres',
                              password='1432') as conn:
            with conn.cursor() as cur:
                cur.execute('TRUNCATE TABLE employers RESTART IDENTITY CASCADE;')

    finally:
        conn.close()
