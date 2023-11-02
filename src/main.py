import psycopg2

from utils_api_hhru import list_employer_id, get_employer_name, get_info_vacancies
from DBManager import DBManager

conn = psycopg2.connect(host='localhost', database='course_work_5', user='postgres', password='1432')


def fill_table_employers():
    """
    Заполняет таблицу employers данными
    """
    try:
        with conn:
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
        with conn:
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


dbmanager = DBManager()

# print(dbmanager.get_vacancies_with_higher_salary())
# print(dbmanager.get_companies_and_vacancies_count())
# print(dbmanager.get_avg_salary())
# print(dbmanager.get_vacancies_with_higher_salary())
# print(dbmanager.get_vacancies_with_keyword('Python'))

