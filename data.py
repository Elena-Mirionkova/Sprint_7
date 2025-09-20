from generators import *

class Url:
    main_url = "http://qa-scooter.praktikum-services.ru"
    create_courier = "/api/v1/courier"
    login_courier = "/api/v1/courier/login"
    delete_courier = "/api/v1/courier"
    create_order = "/api/v1/orders"
    get_orders =  "/api/v1/orders"

class ResponseCodes:
    created = 201
    bad_request = 400
    conflict = 409
    ok = 200
    not_found = 404

class Responses:
    courier_created = {"ok": True}
    courier_already_exists = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    courier_missing_data = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    login_missing_data = {"code": 400, "message": "Недостаточно данных для входа"}
    login_wrong_login = {"code": 404, "message": "Учетная запись не найдена"}
    order_list_entry = "orders"
 
class CourierGeneratedData:
    correctly_generated = {
        "login": generate_login(),
        "password": generate_password(),
        "firstName": generate_name()
    }

    login_data = [
        {           # корректные данные логина
        "login": correctly_generated["login"],
        "password": correctly_generated["password"]
        },
        {           # данные входа без логина
        "login": "",
        "password": correctly_generated["password"]
        },
        {           # данные входа без пароля 
        "login": correctly_generated["login"],
        "password": ""
        },
        {           # данные входа с неправильным логином
        "login": generate_login(),
        "password": correctly_generated["password"]
        },
        {           # данные входа с неправильным паролем
        "login": correctly_generated["login"],
        "password": generate_password()
        }
    ]

    insufficient_params = [
        {           # данные регистрации без пароля
        "login": generate_login(),
        "password": "",
        "firstName": generate_name()
        },
        {           # данные регистрации без логина
        "login": "",
        "password": generate_password(),
        "firstName": generate_name()
        }
    ]

class OrderGeneratedData:
    order_data = {
        "firstName": generate_name(),
        "lastName": generate_last_name(),
        "address": generate_address(),
        "metroStation": generate_metro(),
        "phone": generate_phone(),
        "rentTime": generate_time(),
        "deliveryDate": generate_date(),
        "comment": generate_comment()
        }

    order_color = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [""]
    ]