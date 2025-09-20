import pytest
import requests
from data import *

@pytest.fixture(scope='function')
def courier_generate():
    courier = CourierGeneratedData.correctly_generated
    yield courier
    courier_login = CourierGeneratedData.login_data[0]
    login_result = requests.post(f'{Url.main_url}{Url.login_courier}', data = courier_login)
    r = login_result.json()
    requests.delete(f'{Url.main_url}{Url.delete_courier}/{r["id"]}', data = login_result)


@pytest.fixture(scope='function')
def courier_generate_and_create():
    courier = CourierGeneratedData.correctly_generated
    requests.post(f'{Url.main_url}{Url.create_courier}', data = courier)
    courier_login = CourierGeneratedData.login_data
    yield courier_login
    login_result = requests.post(f'{Url.main_url}{Url.login_courier}', data = CourierGeneratedData.login_data[0])
    r = login_result.json()["id"]
    requests.delete(f'{Url.main_url}{Url.delete_courier}/{r}', data = login_result)


