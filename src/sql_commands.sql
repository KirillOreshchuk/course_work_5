CREATE DATABASE course_work_5;

CREATE TABLE employers
(
	employer_id int PRIMARY KEY,
	employer_name varchar(100)
);

CREATE TABLE vacancies
(
	vacancy_id int PRIMARY KEY,
	employer_id int REFERENCES employers(employer_id),
	vacancy_name varchar(100),
	salary_from int,
	salary_to int,
	vacancy_url varchar(200)
);

# get_companies_and_vacancies_count
SELECT employers.employer_name, COUNT(vacancies.employer_id)
FROM employers
JOIN vacancies
USING(employer_id)
GROUP BY employers.employer_name
ORDER BY COUNT(vacancies.employer_id) DESC;

# all_vacancies
SELECT employers.employer_name, vacancies.vacancy_name,
vacancies.salary_from, vacancies.salary_to, vacancies.vacancy_url
FROM employers
JOIN vacancies USING(employer_id);

# avg_salary
SELECT AVG(salary_to) AS avg_salary
FROM vacancies;

# get_vacancies_with_higher_salary
SELECT *
FROM vacancies
WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)
ORDER BY salary_to DESC;

# get_vacancies_with_keyword
SELECT vacancy_name FROM vacancies WHERE vacancy_name LIKE '%keyword%';