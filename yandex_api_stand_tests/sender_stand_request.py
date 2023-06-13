import requests
import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body);

print(response.status_code)
print(response.json())


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = get_users_table()
print(response.status_code)


# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # тело
                         headers=data.headers)  # заголовки


# Получение токена авторизации
def get_user_auth_token():
    response = post_new_user(data.user_body)
    return response.json().get('authToken')


a_token = get_user_auth_token()

autorization_headers = {"Content-Type": "application/json", "Authorization": "Bearer " + a_token}


# Создание личного набора
def post_new_client_kit(kit_body):
#    kit_body = data.kit_body.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=autorization_headers)


# Проверка факта создания нового набора в таблице kit_model
def get_kit_table():
    return requests.get(configuration.URL_SERVICE + configuration.KIT_TABLE_PATH)