import psycopg2


class DBManager:
    """
    Класс для подключения к БД PostgreSQL
    """
    conn = psycopg2.connect(host='localhost', database='course_work_5', user='postgres', password='1432')

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        with self.conn.cursor() as cur:
            cur.execute('''SELECT employers.employer_name, COUNT(vacancies.employer_id)
                        FROM employers JOIN vacancies USING(employer_id) 
                        GROUP BY employers.employer_name;''')

            result = cur.fetchall()

        for res in result:
            print(res)

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn.cursor() as cur:
            cur.execute('''SELECT employers.employer_name, vacancies.vacancy_name,
            vacancies.salary_from, vacancies.salary_to, vacancies.vacancy_url
            FROM employers
            JOIN vacancies USING(employer_id);''')

            result = cur.fetchall()

        for res in result:
            print(res)

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        with self.conn.cursor() as cur:
            cur.execute('SELECT AVG(salary_to) AS avg_salary FROM vacancies;')

            result = cur.fetchall()

        print(result)

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        with self.conn.cursor() as cur:
            cur.execute('''SELECT vacancy_name, salary_to 
            FROM vacancies
            WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)
            ORDER BY salary_to DESC;''')

            result = cur.fetchall()

        for res in result:
            print(res)

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержится переданное в метод слово
        """
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT vacancy_name FROM vacancies WHERE vacancy_name LIKE '%{keyword}%'")

            result = cur.fetchall()
            if not result:
                result = "Переданное в метод слово не содержится в вакансии"

        print(result)
