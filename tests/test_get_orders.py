import requests
import pytest
import allure
from data import *

class TestCreateOrder:

    @allure.title('Тестируем получение списка заказов. Ручка /v1/order')
    def test_order_create(self):
        orders_get_result = requests.get(f'{Url.main_url}{Url.get_orders}')
        assert orders_get_result.status_code == ResponseCodes.ok and Responses.order_list_entry in orders_get_result.json()