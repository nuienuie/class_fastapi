import requests


def login_test():
    data = {
        'id': 'test',
        'pw': '111'
    }
    response = requests.post('http://127.0.0.1:8000/login', params=data)
    print('response 전부 틀리기 1 :', response.status_code)
    data = {
        'id': 'admin',
        'pw': '5678'
    }
    response = requests.post('http://127.0.0.1:8000/login', params=data)
    print('response 비번 틀리게 2 :', response.status_code)
    data = {
        'id': 'admin',
        'pw': '1234'
    }
    response = requests.post('http://127.0.0.1:8000/login', params=data)
    print('response 정확하게 3 :', response.status_code)