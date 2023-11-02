import requests


# Тинькофф employer_id = 78638
# Сбер employer_id = 3529
# Спортмастер employer_id = 2343
# FESCO employer_id = 23537
# unifrost employer_id = 3565309
# АВТОВАЗ employer_id = 193400
# Сибирская генерирующая Компания employer_id = 876195
# Россельхозбанк employer_id = 58320
# Химсталькон-Инжиниринг employer_id = 992978
# САЛАИР employer_id = 3698181


list_employer_id = [78638, 3529, 2343, 23537, 3565309, 193400, 876195, 58320, 992978, 3698181]
url = "https://api.hh.ru/vacancies"
url_employer = "https://api.hh.ru/employers"


def get_employer_name(employer_id):
    """
    Получает имя работадателя по его id
    """
    response = requests.get(f'{url_employer}/{employer_id}').json()

    return response['name']


def get_info_vacancies(employer_id: int):
    """
    Выводит информацию о вакансиях работодателя по его id
    """
    headers = {
              'User-Agent': 'kirillOreshchuk'
              }
    params = {
              'employer_id': employer_id,
              'only_with_vacancies': True,
              'only_with_salary': True,
              'per_page': 100
              }
    response = requests.get(url, headers=headers, params=params).json()

    return response
