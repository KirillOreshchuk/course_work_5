from DBManager import DBManager
from sql_tables import truncate_tables, fill_table_employers, fill_vacancies_table


def main():
    """
    Основная пользовательсквя функция
    """
    truncate_tables()
    fill_table_employers()
    fill_vacancies_table()

    print('База данных работодателей и вакансий созданы')
    while True:
        try:
            user_input = int(input('1 - Получить список всех компаний и количество вакансий у каждой компании;\n'
                                   '2 - Получить список всех вакансий с указанием названия компании,'
                                   ' названия вакансии и зарплаты и ссылки на вакансию;\n'
                                   '3 - Получить среднюю зарплату по вакансиям;\n'
                                   '4 - Получить список всех вакансий,'
                                   ' у которых зарплата выше средней по всем вакансиям;\n'
                                   '5 - Получить список всех вакансий по ключевому слову;\n'
                                   '0 - Завершить программу.\n'
                                   'Введите команду: '))
        except ValueError:
            print('Вы ввели неправильную команду')
            continue

        dbmanager = DBManager()

        if user_input == 1:
            dbmanager.get_companies_and_vacancies_count()
        elif user_input == 2:
            dbmanager.get_all_vacancies()
        elif user_input == 3:
            dbmanager.get_avg_salary()
        elif user_input == 4:
            dbmanager.get_vacancies_with_higher_salary()
        elif user_input == 5:
            keyword = input("Введите ключевое слово: ")
            dbmanager.get_vacancies_with_keyword(keyword)
        elif user_input == 0:
            print('Спасибо за использование программы!')
            break
        else:
            print('Вы ввели неправильную команду')
            continue


main()
