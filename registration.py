import requests


def registration(token, github):
    authentication = {
        'token': token,
        'github': github
    }
    r = requests.post(
        'http://challenge.code2040.org/api/register', json=authentication)
    return r.text


def main():
    token = '055755d0bef8118fe9960bcf4f12b2be'
    github = 'https://github.com/alejandrogarciasalas/code2040'
    validation = registration(token, github)
    print(validation)

if __name__ == "__main__":
    main()
