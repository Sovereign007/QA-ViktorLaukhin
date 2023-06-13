import data
import sender_stand_request


def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body = data.kit_body.copy()
    # изменение значения в поле Name
    current_kit_body['name'] = name
    # возвращается новый словарь с нужным значением Name
    return current_kit_body


def positive_assert_quantity(kit_name):
    # В переменную kit_body сохраняется новое тело запроса
    kit_body = get_kit_body(kit_name)
    # В переменную kit_response сохраняется результат создания набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # В переменную kit_table_response сохраняется результат запроса на получение данных из таблицы kit_table
    kit_table_response = sender_stand_request.get_kit_table()
    # Проверка, что имя в ответе совпадает с таковым в тесте
    assert kit_response.json()['name'] == kit_name


def negative_assert_quantity(kit_name):
    # В переменную kit_body сохраняется новое тело запроса
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400


def negative_assert_no_kit_name(kit_name):
    kit_response = sender_stand_request.post_new_client_kit(kit_name)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400


# Позитивный тест 1 символ в названии
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert_quantity('И')


# Позитивный тест 511 символов в названии
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert_quantity("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" \
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" \
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Негативный тест 0 символов в названии
def test_create_kit_zero_letters_in_kit_name_get_error_response():
    negative_assert_quantity('')


# Негативный тест 512 символов в названии
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_quantity("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" \
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" \
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Позитивный тест латиница в названии
def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert_quantity('QWErty')


# Позитивный тест кириллица в названии
def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert_quantity('Мария')


# Позитивный тест спецсимволы в названии
def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert_quantity('\"№%@\",')


# Позитивный тест пробелы в названии
def test_create_kit_space_in_kit_name_get_success_response():
    positive_assert_quantity('Человек и КО')


# Позитивный тест числа в названии
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert_quantity('123')

# Негативный тест параметр не передан в запросе
def test_create_kit_no_kit_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    current_kit_body = data.kit_body.copy()
    # Удаление параметра kit_name из запроса
    current_kit_body.pop('name')
    negative_assert_no_kit_name(current_kit_body)

# Негативный тест другой тип (число) параметра в названии
def test_create_kit_number_type_in_kit_name_get_error_response():
    negative_assert_quantity(123)