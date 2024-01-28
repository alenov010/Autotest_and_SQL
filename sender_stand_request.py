# Новиков Александр 12-когорта дипломный проект

import configuration
import requests
import data

def create_order(body):
    """
    Отправка POST запроса на создание заказа.
    """
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.HEADERS)


def get_order_info(track):
    """
    Отправка GET запроса на получение информации о заказе.
    """
    params = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=params,
                        headers=data.HEADERS)