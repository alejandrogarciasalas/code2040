import requests


def get_prefix_arr(token, request_endpoint):
    authentication = {
        'token': token
    }
    r = requests.post(request_endpoint, json=authentication)
    d = r.json()
    prefix = d['prefix']
    arr = d['array']
    return prefix, arr


def get_strings_starting_with_prefix(prefix, arr):
    # one liner using list comprehensions still pretty clear if you are
    # familiar with Python
    return [str for str in arr if str[0:len(prefix)] != prefix]


def validate(token, arr, validation_endpoint):
    solution = {
        'token': token,
        'array': arr
    }
    r = requests.post(validation_endpoint, json=solution)
    return r.text


def main():
    token = '055755d0bef8118fe9960bcf4f12b2be'
    request_endpoint = 'http://challenge.code2040.org/api/prefix'
    validation_endpoint = 'http://challenge.code2040.org/api/prefix/validate'
    prefix, arr = get_prefix_arr(token, request_endpoint)
    ans = get_strings_starting_with_prefix(prefix, arr)
    validation = validate(token, ans, validation_endpoint)
    print(validation)


if __name__ == "__main__":
    main()
