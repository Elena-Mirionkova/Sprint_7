import requests
import pytest
import allure
from data import *

class TestCreateOrder:

    @allure.title('Тестируем создание заказа. Ручка /v1/order')
    @pytest.mark.parametrize('color', OrderGeneratedData.order_color)
    def test_order_create(self, color):
        payload = OrderGeneratedData.order_data
        payload["color"] = color
        order_create_result = requests.post(f'{Url.main_url}{Url.create_order}', json = payload)
        assert order_create_result.status_code == ResponseCodes.created and order_create_result.json()["track"] > 0