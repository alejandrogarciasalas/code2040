import requests


def get_string(token, request_endpoint):
    authentication = {
        'token': token
    }
    r = requests.post(request_endpoint	, json=authentication)
    return r.text


def reverse_string(str):
    return str[::-1]


def validate(token, str, validation_endpoint):
    solution = {
        'token': token,
        'string': str
    }
    r = requests.post(validation_endpoint, json=solution)
    return r.text


def main():
    token = '055755d0bef8118fe9960bcf4f12b2be'
    request_endpoint = 'http://challenge.code2040.org/api/reverse'
    validation_endpoint = 'http://challenge.code2040.org/api/reverse/validate'
    str = get_string(token, request_endpoint)
    ans = reverse_string(str)
    validation = validate(token, ans, validation_endpoint)
    print(validation)


if __name__ == "__main__":
    main()
