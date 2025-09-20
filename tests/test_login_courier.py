import requests
import pytest
import allure
from data import *

class TestLoginCourier:

    @allure.title('Тестируем логин курьера. Ручка /v1/courier/login')
    def test_login_courier_success(self, courier_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_courier}', json = courier_generate_and_create[0])
        assert login_result.status_code == ResponseCodes.ok and login_result.json()["id"] > 0

    @allure.title('Тестируем ошибку входа без логина. Ручка /v1/courier/login')
    def test_login_courier_no_login(self, courier_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_courier}', json = courier_generate_and_create[1])
        assert login_result.status_code == ResponseCodes.bad_request and login_result.json() == Responses.login_missing_data
    
    @allure.title('Тестируем ошибку входа без пароля. Ручка /v1/courier/login')
    def test_login_courier_no_password(self, courier_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_courier}', json = courier_generate_and_create[2])
        assert login_result.status_code == ResponseCodes.bad_request and login_result.json() == Responses.login_missing_data

    @allure.title('Тестируем ошибку входа с неправильным логином. Ручка /v1/courier/login')
    def test_login_courier_wrong_login(self, courier_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_courier}', json = courier_generate_and_create[3])
        assert login_result.status_code == ResponseCodes.not_found and login_result.json() == Responses.login_wrong_login

    @allure.title('Тестируем ошибку входа с неправильным паролем. Ручка /v1/courier/login')
    def test_login_courier_wrong_password(self, courier_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_courier}', json = courier_generate_and_create[4])
        assert login_result.status_code == ResponseCodes.not_found and login_result.json() == Responses.login_wrong_login