import configuration
import requests
import data


def post_new_order(new_order_body): #новый заказ
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=new_order_body, headers=data.headers)


response = post_new_order(data.new_order_body)
track_order = response.json()['track']


def get_order_track(track_order): #получение заказа по номеру заказа
    url = configuration.URL_SERVICE + configuration.ORDER_INFO
    return requests.get(url, params={'t': track_order})
