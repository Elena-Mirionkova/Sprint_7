import requests
import pytest
import allure
from data import *

class TestCreateNewCourier:

    @allure.title('Тестируем успешное создание нового курьера. Ручка /v1/courier')
    def test_create_courier_success(self, courier_generate):
        registration_result = requests.post(f'{Url.main_url}{Url.create_courier}', json = courier_generate)
        assert registration_result.status_code == ResponseCodes.created and registration_result.json() == Responses.courier_created

    @allure.title('Тестируем ошибку повторного создания курьера с теми же данными. Ручка /v1/courier')
    def test_create_courier_duplicate(self, courier_generate):
        registration1_result = requests.post(f'{Url.main_url}{Url.create_courier}', json = courier_generate)
        registration2_result = requests.post(f'{Url.main_url}{Url.create_courier}', json = courier_generate)
        assert registration1_result.status_code == ResponseCodes.created and registration2_result.status_code == ResponseCodes.conflict and registration2_result.json() == Responses.courier_already_exists
    
    @allure.title('Тестируем ошибку создания нового курьера с неполными данными. Ручка /v1/courier')
    @pytest.mark.parametrize('generated_courier_missing_data', CourierGeneratedData.insufficient_params)
    def test_create_courier_missing_data(self, generated_courier_missing_data):
        registration_result = requests.post(f'{Url.main_url}{Url.create_courier}', json = generated_courier_missing_data)
        assert registration_result.status_code == ResponseCodes.bad_request and registration_result.json() == Responses.courier_missing_data
